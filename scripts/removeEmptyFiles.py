
import os
import re

# remove all empty txt files


def removeTxtFiles():
    txt = re.compile(".*[.]txt")
    for filename in os.listdir("data1"):
        if re.match(txt, "data1/"+filename) and os.stat("data1/"+filename).st_size == 0:
            os.remove("data1/" + filename)  # remove the txt file
            # name = filename[:-4]  # take away the .txt part
            # matchName = re.compile(filename+"[.].*")


# Driver Code
if __name__ == '__main__':

    removeTxtFiles()
