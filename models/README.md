# how to train a custom data set on YOLO

## dataset preparation
    - annotate all images using VOTT v1.7.2 software and export to YOLO format
    - aggregate all images into train_test_conversion and run `python3 process.py` to split up images into training and testing sets. default is a 90/10 split but this can be updated

## anchors calculation
    - update train.txt path in anchors.py based on the txt files output by process.py in train_test_conversion
    - run `python3 anchors.py`

## update config file
    - update configuration file in data_for_colab to have the updated weights outputted by anchors.py, the correct number of classes, and the number of filters using the equation (n + 5) * 3, where n = number of classes
    - update obj.data and obj.names to have the correct number of classes, correct paths, and correct names of classes
