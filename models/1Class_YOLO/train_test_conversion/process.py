import glob
import os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# print(current_dir)

# current_dir = '/Users/anabelle/Desktop/Yolo-Training-GoogleColab/train_test_conversion'

# Directory where the data will reside, relative to 'darknet.exe'
path_data = '/Users/christylee/desktop/_COS429/FinalProject/Yolo-Training-GoogleColab/train_test_conversion'

# Percentage of images to be used for the test set
percentage_test = 10

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
# print(file_train)
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(path_data, "*.jpeg")):
    # print(pathAndFilename)
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write(current_dir + "/" + title + '.jpeg' + "\n")
    else:
        file_train.write(current_dir + "/" + title + '.jpeg' + "\n")
        counter = counter + 1
