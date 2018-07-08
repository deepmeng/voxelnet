# -*- coding: utf-8 -*-
#!/usr/bin/python

import os, shutil

train_src_dir = "./object/training/velodyne/"
train_dest_dir = "./object/training/velodyne-choose/"
val_src_dir = "./object/validation/velodyne/"
val_dest_dir = "./object/validation/velodyne-choose/"
srcfile = ""
destfile = ""

def move_train_files_velodyne():
    train_txt = "./object/train.txt"

    train_fd = open(train_txt, "r")
    train_lines = train_fd.readlines()
    for line in train_lines:
        line = line.strip("\n")
        srcfile  = train_src_dir + line + ".bin"
        destfile = train_dest_dir + line + ".bin"

        shutil.move(srcfile, destfile)

def move_val_files_velodyne():
    val_txt = "./object/val.txt"
    val_fd = open(val_txt, "r")
    val_lines = val_fd.readlines()
    for line in val_lines:
        line = line.strip("\n")
        srcfile  = val_src_dir + line + ".bin"
        destfile = val_dest_dir + line + ".bin"

        shutil.move(srcfile, destfile)

def move_train_files_images():
    train_txt = "./object/train.txt"
    src_dir = "./object/training/image_2/"
    dest_dir = "./object/training/image_2-choose/"

    train_fd = open(train_txt, "r")
    train_lines = train_fd.readlines()
    for line in train_lines:
        line = line.strip("\n")
        srcfile  = src_dir  + line + ".png"
        destfile = dest_dir + line + ".png"

        shutil.move(srcfile, destfile)

def move_val_files_images():
    val_txt = "./object/val.txt"
    src_dir = "./object/validation/image_2/"
    dest_dir = "./object/validation/image_2-choose/"

    val_fd = open(val_txt, "r")
    val_lines = val_fd.readlines()
    for line in val_lines:
        line = line.strip("\n")
        srcfile  = src_dir  + line + ".png"
        destfile = dest_dir + line + ".png"
        print("srcfile:",srcfile)

        shutil.move(srcfile, destfile)




if __name__=="__main__":
    #move_train_files()
    move_val_files_velodyne()
    #move_train_files_images()
    #move_val_files_images()

