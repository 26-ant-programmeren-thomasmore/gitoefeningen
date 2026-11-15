import os
import re
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

md_files = []
for root, dirs, files in os.walk('.'):
    if any(p in root for p in ['temp', '.git', '.idea']):
        continue
    for f in files:
        if f.endswith('.md'):
            md_files.append(os.path.normpath(os.path.join(root, f)).replace('\\', '/'))

md_files.sort()

corrupt_chars = []
dash_in_command_issues = []
triple_backtick_inlines = []
broken_quotes = []

for path in md_files:
    with open(path, 'r', encoding='utf-8', errors='replace') as fp:
        lines = fp.readlines()

    for idx, line in enumerate(lines, 1):
        # 1. Corrupt character replacement \ufffd ()
        if '\ufffd' in line:
            corrupt_chars.append((path, idx, line.strip()))

        # 2. Triple backticks on one line: e.g. ```cmd```
        m_inline = re.findall(r'```([^`\n]+)```', line)
        if m_inline:
            triple_backtick_inlines.append((path, idx, m_inline, line.strip()))

        # 3. En-dash or em-dash where double dash might be intended
        # e.g. –install, –global, etc.
        m_dash = re.findall(r'[–—][a-zA-Z0-9_-]+', line)
        if m_dash:
            dash_in_command_issues.append((path, idx, m_dash, line.strip()))

print(f"=== CORRUPTE KARAKTERS (\\ufffd / REPLACEMENT CHAR) ===")
print(f"Aantal regels: {len(corrupt_chars)}")
for item in corrupt_chars:
    print(f"[{item[0]}:{item[1]}] {repr(item[2])}")

print(f"\n=== EN-DASH / EM-DASH IN COMMANDS (– ipv --) ===")
print(f"Aantal regels: {len(dash_in_command_issues)}")
for item in dash_in_command_issues:
    print(f"[{item[0]}:{item[1]}] Matches: {item[2]} -> {repr(item[3])}")

print(f"\n=== DRIEVOUDIGE BACKTICKS OP 1 REGEL (```cmd``` ipv `cmd`) ===")
print(f"Aantal regels: {len(triple_backtick_inlines)}")
for item in triple_backtick_inlines:
    print(f"[{item[0]}:{item[1]}] Matches: {item[2]} -> {repr(item[3])}")
