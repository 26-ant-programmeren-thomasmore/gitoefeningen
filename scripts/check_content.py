import os
import re

forbidden_patterns = [
    r'\bretourneer\w*',
    r'\bretourneren\b',
    r'\brouteer\w*',
    r'\brouteren\b',
    r'\bcommitteer\w*',
    r'\bcommitteren\b',
    r'\bgecommitteerd\w*',
    r'\bextraheer\w*',
    r'\bextraheren\b',
    r'\bgedestructureer\w*'
]

todos = [r'\bTODO\b', r'\bFIXME\b', r'\bTBD\b', r'\bXXX\b', r'\bLOREM\b']

md_files = []
for root, dirs, files in os.walk('.'):
    if any(p in root for p in ['temp', '.git', '.idea']):
        continue
    for f in files:
        if f.endswith('.md'):
            md_files.append(os.path.normpath(os.path.join(root, f)).replace('\\', '/'))

md_files.sort()
print(f"Controleren van {len(md_files)} markdown bestanden...\n")

found_forbidden = []
found_todos = []
unlabeled_codeblocks = []
unclosed_codeblocks = []
empty_files = []
heading_issues = []

for path in md_files:
    with open(path, 'r', encoding='utf-8', errors='replace') as fp:
        lines = fp.readlines()

    if not lines or not ''.join(lines).strip():
        empty_files.append(path)
        continue

    in_code = False
    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith('```'):
            if not in_code:
                in_code = True
                lang = stripped[3:].strip()
                if not lang:
                    unlabeled_codeblocks.append((path, idx))
            else:
                in_code = False

        # Alleen buiten pure inline/block code of in zinnen controleren
        for pat in forbidden_patterns:
            m = re.findall(pat, line, re.IGNORECASE)
            if m:
                found_forbidden.append((path, idx, m, stripped))

        for pat in todos:
            m = re.findall(pat, line, re.IGNORECASE)
            if m:
                found_todos.append((path, idx, m, stripped))

    if in_code:
        unclosed_codeblocks.append(path)

print("=== 1. VERBODEN WOORDEN (GEMINI.md regels) ===")
for item in found_forbidden:
    print(f"[{item[0]}:{item[1]}] Matches: {item[2]} -> '{item[3]}'")
print(f"Totaal matches: {len(found_forbidden)}\n")

print("=== 2. TODOS / PLACEHOLDERS ===")
for item in found_todos:
    print(f"[{item[0]}:{item[1]}] Matches: {item[2]} -> '{item[3]}'")
print(f"Totaal matches: {len(found_todos)}\n")

print("=== 3. ONGESPECIFICEERDE TAAL IN CODEBLOCKS (``` zonder bash/markdown/etc) ===")
for item in unlabeled_codeblocks:
    print(f"[{item[0]}:{item[1]}]")
print(f"Totaal unlabeled: {len(unlabeled_codeblocks)}\n")

print("=== 4. ONGESLOTEN CODEBLOCKS ===")
for item in unclosed_codeblocks:
    print(f"[{item}]")
print(f"Totaal unclosed: {len(unclosed_codeblocks)}\n")
