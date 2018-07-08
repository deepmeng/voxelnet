import os

path = "/home1/liumeng/object_detect/voxelnet/data/object/training/velodyne/"

for f in os.listdir(path):
    ff = f.strip(".bin")
    n = (int)(ff)

    name = "%06d.bin"%n
    os.rename(os.path.join(path,f), os.path.join(path, name) )

