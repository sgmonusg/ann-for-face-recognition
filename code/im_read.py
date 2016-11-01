import cv2
import numpy as np

f = open('an2i_left_angry_open.pgm', 'r')
fw = open('xy.txt','w')

w = 352
h = 288
size = 352*288*3/2

while True:
    try:
        yuv = f.read()
        f.close()
        for x in yuv:
            print(x)
        fw.write(yuv)
        #print("ss")
        fw.close()
    except:
        break

class List(object):
    li=list()

    def __init__(self , li):
        self.li=li


class Image(object):
    numrow = 0
    numcol = 0
    data= ""
    name= ""

    # The class "constructor" - It's actually an initializer 
    def __init__(self, data, numrow, numcol , name):
        self.data = data
        self.numrow = numrow
        self.numcol = numcol
        self.name=name

def create_image(data, numrow, numcol,name):
    image = Image(data,numrow,numcol,name)
    return image


def im_read(filename):
    try:
        f.open(filename,"r")
        data=f.read()
        f.close()
    except:
        print("could not open the file")
        return NULL
    for line in data:

def rows(image):
    return image.numrow

def col(image):
    return image.numcol

def name(image):
    return image.name

def get_pixel(image , row , col):
    nr=image.numrow
    pixel_value=data[(nr*(row-1))+(col)]
    return pixel_value

def set_pixel(image , row, col , pixel_value):
    nr=image.numrow
    data[(nr*(row-1))+col]=pixel_value
    return image

def add_to_img_list(filename, li):
    li.append(filename)

def Del_from_img_list(filenaem , li):
    if filename in li:
        i=li.index(filename)
        del li[i]
        return li
    else:
        print("error file not found in list")
        return li

def load_img_frm_textfile(li,textfilename):
    f.open(textfilename+"txt","r")
    data=f.read()
    for line in data:
        im_read(line)
        add_to_img_list(filename, li)








