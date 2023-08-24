#!/usr/bin/env python3
# A simple tool to merge multiple xml files 


import os
import sys
import xml.etree.ElementTree as ET

def merge_xml_files(input_folder, output_path):
    merged_root = None

    for filename in os.listdir(input_folder):
        if filename.endswith(".xml"):
            file_path = os.path.join(input_folder, filename)
            tree = ET.parse(file_path)
            root = tree.getroot()

            if merged_root is None:
                merged_root = root
            else:
                for element in root:
                    merged_root.append(element)

    if merged_root is not None:
        merged_tree = ET.ElementTree(merged_root)
        merged_tree.write(output_path, encoding="utf-8", xml_declaration=True)
        print("XML files merged and saved to", output_path)
    else:
        print("No XML files found in the input folder.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_folder output_file")
    else:
        input_folder = sys.argv[1]
        output_path = sys.argv[2]
        merge_xml_files(input_folder, output_path)
