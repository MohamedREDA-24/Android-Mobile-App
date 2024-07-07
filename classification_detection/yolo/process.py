import glob
import os

current_dir = "Multiple_images"

file_train = open("train.txt", "w")

for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    file_train.write("data" + "/" + current_dir + "/" + title + '.jpg' + "\n")

file_train.close()


current_dir = "val_images"

file_val = open("test.txt", "w")  


for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    file_val.write("data" + "/" + current_dir + "/" + title + '.jpg' + "\n")

file_val.close()