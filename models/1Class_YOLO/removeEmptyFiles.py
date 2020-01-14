
import os
import re

# remove all empty txt files


def removeTxtFiles():
    txt = re.compile(".*[.]txt")
    for filename in os.listdir("train_test_conversion"):
        if re.match(txt, "train_test_conversion/"+filename) and os.stat("train_test_conversion/"+filename).st_size == 0:
            # remove the txt file
            os.remove("train_test_conversion/" + filename)
            # name = filename[:-4]  # take away the .txt part
            # matchName = re.compile(filename+"[.].*")


# Driver Code
if __name__ == '__main__':

    removeTxtFiles()
