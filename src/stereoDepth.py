"""
Date: 16.Nov.2024
Author: Harish Natarajan Ravi
Email: harrish.nr@gmail.com
"""

import numpy as np
import pandas as pd
import matplotlib
import cv2
from matplotlib import pyplot as plt
from matplotlib import patches

import importlib
import sys
from importlib import reload
matplotlib.use('TkAgg')

# Set display precision for floating point numbers
np.set_printoptions(precision=2, suppress=True)
pd.set_option('display.precision', 2)

import files_management
import algo_defs

# Read the stereo-pair of images# 
img_left = files_management.read_left_image()
img_right = files_management.read_right_image()

# Use matplotlib to display the two images
_, image_cells = plt.subplots(1, 2, figsize=(20, 20))
image_cells[0].imshow(img_left)
image_cells[0].set_title('left image')
image_cells[1].imshow(img_right)
image_cells[1].set_title('right image')
#plt.show()

# Large plot of the left image
# plt.figure(figsize=(16, 12), dpi=100)
# plt.imshow(img_left)
# plt.show()

# Read the calibration
p_left, p_right = files_management.get_projection_matrices()
 
np.set_printoptions(suppress=True)

#print("p_left \n", p_left)
#print("\np_right \n", p_right)

#Estimating Depth

#Disparity

# Compute the disparity map using the fuction above
disp_left = algo_defs.compute_left_disparity_map(img_left, img_right)

# Show the left disparity map
plt.figure(figsize=(10, 10))
plt.imshow(disp_left)
plt.title("Disparity Map")
#plt.show()

# Decompose Projection Matrices P = K[R|t]

k_left, r_left, t_left = algo_defs.decompose_projection_matrix(p_left)
k_right, r_right, t_right = algo_defs.decompose_projection_matrix(p_right)

# Generate depth map
depth_map_left = algo_defs.calc_depth_map(disp_left, k_left, t_left, t_right)

# Display the depth map
plt.figure(figsize=(8, 8), dpi=100)
plt.imshow(depth_map_left, cmap='flag')
plt.title("Depth Map")
#plt.show()

# Distance to Collision

# Get the image of the obstacle
obstacle_image = files_management.get_obstacle_image()

# Show the obstacle image
plt.figure(figsize=(4, 4))
plt.imshow(obstacle_image)
plt.title("Obstacle Image")
#plt.show()

# Gather the cross correlation map and the obstacle location in the image
cross_corr_map, obstacle_location = algo_defs.locate_obstacle_in_image(img_left, obstacle_image)

# Display the cross correlation heatmap 
plt.figure(figsize=(10, 10))
plt.imshow(cross_corr_map)
plt.title("Cross correlation heatmap")
#plt.show()

# Print the obstacle location
print("obstacle_location \n", obstacle_location)

# Use the developed nearest point function to get the closest point depth and obstacle bounding box
closest_point_depth, obstacle_bbox = algo_defs.calculate_nearest_point(depth_map_left, obstacle_location, obstacle_image)

# Display the image with the bounding box displayed
fig, ax = plt.subplots(1, figsize=(10, 10))
ax.imshow(img_left)
ax.add_patch(obstacle_bbox)
plt.title("Obstacle_BoundingBox")
#plt.show()

# Print the depth of the nearest point
print("closest_point_depth {0:0.3f}".format(closest_point_depth))

print("Done!!")

plt.show()