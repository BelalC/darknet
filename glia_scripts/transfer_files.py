import os
import glob
import shutil

dst_dir = "/home/ubuntu/single_class/data/"

for root, dirs, files in os.walk("."):
    for names in files:
        if names.endswith(".jpg"):
            print(os.path.join(root,names))
            shutil.copy(os.path.join(root,names), dst_dir)
