#!/usr/bin/env bash

OUTPUT_MD="temp/all_pages.md"
mkdir -p temp
rm -f "$OUTPUT_MD"

current_dir=""

# README eerst, daarna cursusbestanden uit submappen gesorteerd toevoegen
for f in README.md $(find [0-9]* -name "*.md" | sort); do
  dir="${f%/*}"
  if [ "$f" != "README.md" ] && [ "$dir" != "$current_dir" ]; then
    current_dir="$dir"
    title=$(echo "$dir" | sed -E 's/^[0-9]+_//; s/_/ /g' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) tolower(substr($i,2)); print}')
    echo "# $title" >> "$OUTPUT_MD"
    echo "" >> "$OUTPUT_MD"
  fi

  awk '
    /\[([Pp]rev|[Nn]ext)\]/ { next }
    {
      while (match($0, /\[([^]]+)\]\(([^)]*(\.md|push_and_pull))\)/)) {
        s = substr($0, RSTART, RLENGTH)
        sub(/^\[/, "", s); split(s, p, /\]\(/)
        txt = p[1]; slug = tolower(txt)
        gsub(/[^a-z0-9 -]/, "", slug); gsub(/[ _]+/, "-", slug)
        $0 = substr($0, 1, RSTART - 1) "[" txt "](#" slug ")" substr($0, RSTART + RLENGTH)
      }
      print
    }
  ' "$f" >> "$OUTPUT_MD"
  echo "" >> "$OUTPUT_MD"
done
