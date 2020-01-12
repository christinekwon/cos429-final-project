import glob
import os

all_txt = glob.glob("*.txt")

for file in glob.glob("*.jpeg"):
    txt_name = file[:-5] + ".txt"
    if txt_name not in all_txt:
        os.remove(file)
