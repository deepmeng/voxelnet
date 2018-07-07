# crooped gt dir
GT_DIR=/home1/liumeng/object_detect/voxelnet/data/object/testing/label_2
# pred dir
PRED_DIR=$1

# output log
OUTPUT=$2
# start test
nohup `pwd`/kitti_eval/evaluate_object_3d_offline $GT_DIR $PRED_DIR > $OUTPUT 2>&1 &
