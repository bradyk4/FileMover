import glob
import os
import shutil
from pathlib import Path

image_destDir = "D:\OneDrive\Pictures\Downloaded Pictures";
txt_destDir = "D:\Downloads\TxtFiles";
docx_destDir = "D:\Downloads\DocxFiles";
pptx_destDir = "D:\Downloads\PptxFiles";
src_dir = Path("D:\Downloads");

for file_name in src_dir.glob('*.jpg'): # list all jpg files in source directory
    shutil.move(file_name, image_destDir);

for file_name in src_dir.glob(*.txt): # list all txt files in source directory
    shutil.move(file_name, txt_destDir);

for file_name in src_dir.glob(*.docx): # list all docx files in source directory
    shutil.move(file_name, docx_destDir);

for file_name in src_dir.glob(*.pptx): # list all pptx files in source directory
    shutil.move(file_name, pptx_destDir);
