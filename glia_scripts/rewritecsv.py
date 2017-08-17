import cv2
import csv
import sys
import shutil
import os

dst_dir = "/home/ubuntu/only_cancers/data/"

csvfile=open(sys.argv[1],'rt')
read=csv.reader(csvfile)
read.next()
#line=read.next()
for line in read:
    path=line[0]
    path=path[:-4]+'jpg'
    tempimage=cv2.imread(path,0)
    if(tempimage!=None):
        shutil.copy(path, dst_dir)
        image_width,image_height=tempimage.shape[:2]
        absolute_width=float(line[5])-float(line[4])
        absolute_height=float(line[7])-float(line[6])
        absolute_center_x=float(line[4])+absolute_width/2
        absolute_center_y=float(line[6])+absolute_height/2
        x=absolute_center_x/image_width
        y=absolute_center_y/image_height
        width=absolute_width/image_width
        height=absolute_height/image_height
        if path[27]=='b':
            typee=1
        else:
            typee=0
        #image_name=path.rsplit('.',1)[-2]
        image_path=path.rsplit('/',1)
        image_name=image_path[1][:-3]
        filename=dst_dir+image_name+'.txt'
        with open(filename,'w') as textfile:
            textfile.write("%f,%f,%f,%f,%f" % (typee,x,y,width,height))
            textfile.close()
    #print typee,x,y,width,height
csvfile.close()
