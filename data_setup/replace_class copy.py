import glob, os
import sys

# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))
# print ('Argument0:', str(sys.argv[0]))
# print ('Argument1:', str(sys.argv[1]))


if (len(sys.argv) < 2):
    print("\tusage: python3 replace_class.py newClassValue")
    sys.exit()

classValue = str(sys.argv[1])

for file in glob.glob("*.txt"):
    
    # open file to read
    fo = open(file, "r+")
    print("updating:", fo.name)

    # read lines
    lines = fo.readlines()
    replace = ""
    for line in lines:
        # print(classValue + line[1:-1])
        replace += (classValue + line[1:-1] + "\n")
    # remove trailing white space
    replace = replace[:-1]
    # close opened file
    fo.close()

    # open file to write
    f1 = open(file, "w+")
    f1.write(replace)
    # close opened file
    f1.close()