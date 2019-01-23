#!/usr/bin/bash
mkdir -p download
python3 crawl_materials.py
cd download
cp ../file_names.txt ./
filename="file_names.txt"
while read -r line; do
    name=$line
    wget $name -q
done < "$filename"
