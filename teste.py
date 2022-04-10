import py360convert
import argparse
import numpy as np
from PIL import Image
import cv2
import time


h_fov=60
v_fov=60
u_deg=0
v_deg=0
h=576
w=1024
rot=0
mode='bilinear'
#src='assert/example_input.png'
src='/Users/jcarreira/Work/motoxtremeV4/PythonScripts/v360/Equirec2Perspec/src/image.jpg'
img = np.array(Image.open(src))
if len(img.shape) == 2:
    img = img[..., None]


for i in range(10):
    start = time.time()
    out = py360convert.e2p(img, fov_deg=(h_fov, v_fov), u_deg=u_deg, v_deg=v_deg,
                           out_hw=(h, w), in_rot_deg=rot, mode=mode)
    end = time.time()
    print( end-start )

cv2.imshow('image', out)
cv2.waitKey(0)
