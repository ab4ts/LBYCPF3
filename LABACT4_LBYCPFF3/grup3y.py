# Import the necessary packages
from __future__ import print_function
import cv2
import numpy as np
import argparse
# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the grayscale image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# Load the image in grayscale mode
image = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)
# Loop through a set of threshold values to apply simple thresholding
for T in range(50, 251, 50):
    _, thresh = cv2.threshold(image, T, 255, cv2.THRESH_BINARY)
    
    # Display the thresholded image
    cv2.imshow(f"Threshold {T}", thresh)
    cv2.waitKey(0)
cv2.destroyAllWindows()
