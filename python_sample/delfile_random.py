# -*- coding: utf-8 -*-
#4000ファイルをランダムで消す。
import os
import sys
import cv2
import glob
import random
import shutil
import numpy as np

# base_folder = "hogehoge"
base_folder = " folder here "

files = os.listdir(base_folder)

for file in random.sample(files, 4000):
    print(file)
    os.remove(os.path.join(base_folder, file))






