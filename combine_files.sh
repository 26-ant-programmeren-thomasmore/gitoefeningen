OUTPUT_MD="temp/all_pages.md"

rm -f $OUTPUT_MD
for f in $(find . -name "*.md" -not -wholename "$OUTPUT_MD"| sort); do
  sed -E '/\[([Pp]rev|[Nn]ext)\]\([^)]+\)/d' "$f" >> "$OUTPUT_MD"
done 