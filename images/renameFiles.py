# Python3 code to rename multiple files in a directory or folder
# source: https://www.geeksforgeeks.org/rename-multiple-files-using-python/

# importing os module
import os
import re

# Function to rename multiple files


def rename():
    i = 0
    jpeg = re.compile(".*[.]jpeg")
    jpg = re.compile(".*[.]jpg")
    png = re.compile(".*[.]png")
    appendType = ""
    for filename in os.listdir("tropicana_probiotics"):
        if re.match(jpeg, filename) or re.match(jpg, filename):
            appendType = ".jpeg"
        if re.match(png, filename):
            appendType = ".png"
        dst = "tropicana_probiotics/" + \
            "tropicana_probiotics_" + str(i) + appendType
        src = "tropicana_probiotics/" + filename
        dst = dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)
        i += 1


# Driver Code
if __name__ == '__main__':

    # Calling main() function
    rename()
