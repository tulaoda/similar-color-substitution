#!/usr/bin/python
# -*- coding: utf-8 -*-
from colorsys import rgb_to_hsv
import re
def to_hsv( color ):
    color=str(color).split(",")
    return rgb_to_hsv(*[float(x)/255.0 for x in color]) 
def color_dist( c1, c2):
    return sum( (a-b)**2 for a,b in zip(to_hsv(c1),to_hsv(c2)) )
def min_color_diff( color_to_match, colors):
    return min( 
        (color_dist(color_to_match, test),test)
        for test in colors
        )
def RGB_to_Hex(rgb):
    RGB = rgb.split(',')          
    color = '#'
    for i in RGB:
        num = int(i)
        color += str(hex(num))[-2:].replace('x', '0')
    return color
def Hex_to_RGB(hex):
    if(len(hex)==3):
        hex+=hex
    r = int(hex[0:2],16)
    g = int(hex[2:4],16)
    b = int(hex[4:6],16)
    rgb = str(r)+','+str(g)+','+str(b)
    return rgb
f1 = open("src/css/common/_variables.scss",'r')
f2 = open("src/css/common/_variables3.scss",'w')
line = f1.readline()
arr=[]
arr2=[]
flag=1
while line:
        line = f1.readline()
        if(len(re.findall(r'//over', line))>0):
                flag=2
        res=re.findall(r'#(\w*)', line)
        if(flag==1):
                f2.writelines(line)
                for i in res:
                        arr.append(Hex_to_RGB(i))
        if(flag==2):
                if(len(res)>0):
                        for item in res:
                                result=min_color_diff(Hex_to_RGB(item),arr)
                                result=str(result).split("'")[1]
                                result=RGB_to_Hex(result)
                                res=re.sub(r'#(\w*)', result,line)
                                f2.writelines(res)
                                print res
                else:
                        f2.writelines(line)
f1.close()
f2.close()



