import os
from os import walk, getcwd
from PIL import Image

classes = ["fish","Jelly","shark","tuna"]

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
    
    
 
mypath = "Labels/tuna/"

outpath = "Labels/output_tuna/"  




cls = "tuna"   
if cls not in classes:
    exit(0)
cls_id = classes.index(cls)

wd = getcwd()

""" Get input text file list """
txt_name_list = []
for (dirpath, dirnames, filenames) in walk(mypath):
    txt_name_list.extend(filenames)
    break
print(txt_name_list)

for txt_name in txt_name_list:
    
    
    txt_path = mypath + txt_name
    print("Input:" + txt_path)
    txt_file = open(txt_path, "r")
    lines = txt_file.read().split('\n')   
    
    txt_outpath = outpath + txt_name
    print("Output:" + txt_outpath)
    txt_outfile = open(txt_outpath, "w")
    
    
    """ Convert the data to YOLO format """
    for line in lines:
 
        if(len(line) >= 2):
            print(line)
            elems = line.split(',')
            print(elems)
            xmin = elems[2]
            xmax = elems[4]
            ymin = elems[3]
            ymax = elems[5]
            
            img_path = str('%s/Images/%s/%s.JPG'%(wd, cls, os.path.splitext(txt_name)[0]))

            im=Image.open(img_path)
            w= int(im.size[0])
            h= int(im.size[1])

            print(w, h)
            b = (float(xmin), float(xmax), float(ymin), float(ymax))
            bb = convert((w,h), b)
            print(bb)
            txt_outfile.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

      



