#!/home/yosef/anaconda3/bin/python

from PIL import Image
import os
import img2pdf

if os.name == "posix":
    _ = os.system("clear")
else:
    _ = os.system("cls")

print("Convert images in directory to PDF.")
print("The subdirectories in this folder:")
print(next(os.walk("."))[1])

path = input("Enter name of the directory with the png files:")

file_name = input(f"enter pdf file name(default {path}.pdf):")
if file_name == "":
    file_name = path


dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path)
files = os.listdir(dir_path)
# order files by number:
files = sorted(files, key=lambda x: int(x.split(".png")[0]))


imagelist = []
for file in files:
    p = os.path.join(dir_path, file)
    imagelist.append(p)

try:
    with open(f"{file_name}.pdf", "wb") as f:
        f.write(img2pdf.convert(imagelist))
except Exception as e:
    print(e)

