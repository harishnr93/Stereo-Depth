import csv
import numpy as np
import cv2
from matplotlib import pyplot as plt

image_path = "h:\VS_Code\workspace\Stereo Depth\stereo_set"


def get_projection_matrices():
    """Frame Calibration Holder
    3x4    p_left, p_right      Camera P matrix. Contains extrinsic and intrinsic parameters.
    """
    p_left = np.array([[640.0,   0.0, 640.0, 2176.0], 
                       [  0.0, 480.0, 480.0,  552.0], 
                       [  0.0,   0.0,   1.0,    1.4]])
    p_right = np.array([[640.0,   0.0, 640.0, 2176.0], 
                       [   0.0, 480.0, 480.0,  792.0], 
                       [   0.0,   0.0,   1.0,    1.4]])
    return p_left, p_right 

def read_left_image():
    # conversion BGR => RGB
    image_L = image_path + "\img_testL.png"
    image = cv2.imread(image_L)[...,::-1]
    return image

def read_right_image():
    # conversion BGR => RGB
    image_R = image_path + "\img_testR.png"
    image = cv2.imread(image_R)[...,::-1]
    return image


def get_obstacle_image():
    img_left_colour = read_left_image()
    return img_left_colour[479:509, 547:593, :]
