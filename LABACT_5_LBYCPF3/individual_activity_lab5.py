# Import necessary packages
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

# Set up argument parser to accept the image path
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the satellite image")
args = vars(ap.parse_args())

# Load the satellite image in grayscale
image_path = args["image"]
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Display the original image
plt.figure(figsize=(10, 10))
plt.title("Original Image")
plt.imshow(image, cmap="gray")
plt.show()

# 1. Apply Laplacian Edge Detection
laplacian = cv2.Laplacian(image, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

# 2. Apply Sobel Edge Detection
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
sobel_combined = cv2.bitwise_or(np.uint8(np.absolute(sobelX)), np.uint8(np.absolute(sobelY)))

# 3. Apply Gaussian Blur (for noise reduction) and Canny Edge Detection
# You can experiment with different kernel sizes for Gaussian blur
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
canny_edges = cv2.Canny(blurred_image, 100, 200)  # Adjust thresholds as needed

# Plotting results for comparison
fig, axes = plt.subplots(2, 2, figsize=(15, 15))
axes[0, 0].imshow(image, cmap="gray")
axes[0, 0].set_title("Original Image")
axes[0, 1].imshow(laplacian, cmap="gray")
axes[0, 1].set_title("Laplacian Edge Detection")
axes[1, 0].imshow(sobel_combined, cmap="gray")
axes[1, 0].set_title("Sobel Edge Detection (Combined X and Y)")
axes[1, 1].imshow(canny_edges, cmap="gray")
axes[1, 1].set_title("Canny Edge Detection with Gaussian Blur")
for ax in axes.ravel():
    ax.axis("off")
plt.show()
