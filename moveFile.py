import glob
import os
import shutil
from pathlib import Path

class moveFile:
    def jpgFiles():
        src_dir = Path("D:\Downloads");
        jpg_destDir = "D:\OneDrive\Pictures\Downloaded Pictures";
        for file_name in src_dir.glob('*.jpg'): # list all jpg files in source directory
            shutil.move(file_name, image_destDir);

    def txtFiles():
        src_dir = Path("D:\Downloads");
        txt_destDir = "D:\Downloads\TxtFiles";
        for file_name in src_dir.glob('*.txt'): # list all txt files in source directory
            shutil.move(file_name, txt_destDir);

    def docxFiles():
        src_dir = Path("D:\Downloads");
        docx_destDir = "D:\Downloads\DocxFiles";
        for file_name in src_dir.glob('*.docx'): # list all docx files in source directory
            shutil.move(file_name, docx_destDir);

    def pptxFiles():
        src_dir = Path("D:\Downloads");
        pptx_destDir = "D:\Downloads\PptxFiles";
        for file_name in src_dir.glob('*.pptx'): # list all pptx files in source directory
            shutil.move(file_name, pptx_destDir);

    jpgFiles();
    txtFiles();
    docxFiles();
    pptxFiles();
