import os
import re

print("=== STARTING AUDIT AGAINST CONVENTIONS.MD ===")

errors = []
warnings = []

# Collect all markdown files
all_md = []
for root, dirs, fnames in os.walk("."):
    norm_root = root.replace("\\", "/")
    if (
        norm_root.startswith("./temp")
        or norm_root == "./temp"
        or norm_root.startswith("./.git")
        or norm_root == "./.git"
    ):
        continue
    for f in fnames:
        if f.endswith(".md") and f != "CONVENTIONS.md":
            all_md.append(os.path.normpath(os.path.join(root, f)).replace("\\", "/"))

all_md.sort()

# Pre-load H1 for every file
file_h1 = {}
for f in all_md:
    with open(f, "rb") as fp:
        raw = fp.read()
    # Check BOM
    if raw.startswith(b"\xef\xbb\xbf"):
        errors.append(f"{f}: [Regel 1] Bevat UTF-8 BOM!")
    # Check H1 on line 1 for README, H2 for course files in subdirectories
    lines = raw.split(b"\n")
    line1 = lines[0].decode("utf-8", errors="replace").rstrip("\r")
    if f == "README.md":
        if not line1.startswith("# "):
            errors.append(f"{f}: [Regel 2] Regel 1 start niet met '# ': {repr(line1)}")
        else:
            title_text = line1[2:].strip()
            file_h1[f] = title_text
            file_h1[os.path.basename(f)] = title_text
    else:
        if not line1.startswith("## "):
            errors.append(f"{f}: [Regel 2] Regel 1 start niet met '## ': {repr(line1)}")
        else:
            title_text = line1[3:].strip()
            file_h1[f] = title_text
            file_h1[os.path.basename(f)] = title_text

# Check shell scripts
for root, dirs, fnames in os.walk("."):
    if "temp" in root or ".git" in root:
        continue
    for f in fnames:
        if f.endswith(".sh"):
            sh_path = os.path.normpath(os.path.join(root, f)).replace("\\", "/")
            with open(sh_path, "rb") as fp:
                raw_sh = fp.read()
            if b"\r\n" in raw_sh:
                errors.append(f"{sh_path}: [Regel 7] Shellscript bevat CRLF regeleinden!")

print(f"Totaal gecontroleerde bestanden: {len(all_md)}")

# Check links and images
for f in all_md:
    file_dir = os.path.dirname(f)
    with open(f, "r", encoding="utf-8") as fp:
        content = fp.read()

    # Rule 4: Images
    img_matches = re.findall(r"!\[(.*?)\]\((.*?)\)", content)
    for alt, img_path in img_matches:
        if " " in os.path.basename(img_path):
            warnings.append(f"{f}: [Regel 4] Afbeeldingsnaam bevat spaties: '{img_path}'")
        resolved_img = os.path.normpath(os.path.join(file_dir, img_path)).replace("\\", "/")
        if not os.path.exists(resolved_img):
            errors.append(f"{f}: [Regel 4] Afbeelding ontbreekt op schijf: '{img_path}' (opgelost naar {resolved_img})")
        if f not in ("README.md", "CONVENTIONS.md") and not img_path.startswith("../images/"):
            warnings.append(f"{f}: [Regel 4] Afbeelding verwijst niet via ../images/: '{img_path}'")

    # Rule 3: Links
    link_matches = re.findall(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)", content)
    for text, target in link_matches:
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        # Prev / Next are handled in Rule 5
        if text.lower() in ("prev", "next"):
            continue

        clean_target = target.split("?")[0].split("#")[0]
        if not clean_target.endswith(".md"):
            errors.append(f"{f}: [Regel 3] Link mist .md extensie: [{text}]({target})")

        resolved_file = os.path.normpath(os.path.join(file_dir, clean_target)).replace("\\", "/")
        if not os.path.exists(resolved_file):
            errors.append(f"{f}: [Regel 3] Link verwijst naar niet-bestaand bestand: [{text}]({target}) -> {resolved_file}")
        else:
            expected_h1 = file_h1.get(resolved_file, file_h1.get(os.path.basename(resolved_file)))
            if expected_h1 and text.strip() != expected_h1.strip():
                errors.append(f"{f}: [Regel 3] Linktekst matcht H1 niet exact: [{text}] vs H1 '{expected_h1}' in {clean_target}")

    # Rule 5: Navigation & Trailing ---
    if f not in ("README.md", "CONVENTIONS.md"):
        trimmed = content.rstrip()
        # Has --- near end
        if not re.search(r"---\s*(\n\s*\[(prev|next)\][^\n]*)*$", trimmed, re.IGNORECASE):
            errors.append(f"{f}: [Regel 5] Bestand eindigt niet met '---' of navigatie voorafgegaan door '---'")

print("\n=== AUDIT RESULTATEN ===")
print(f"Errors: {len(errors)}")
for e in errors:
    print(f"  [FOUT] {e}")

print(f"\nWarnings: {len(warnings)}")
for w in warnings:
    print(f"  [WAARSCHUWING] {w}")

if len(errors) == 0 and len(warnings) == 0:
    print("\nALLES 100% IN OVEREENSTEMMING MET CONVENTIONS.MD!")
