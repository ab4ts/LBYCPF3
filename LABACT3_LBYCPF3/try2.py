import cv2
import argparse
import numpy as np

# Parse command-line arguments to get the image path
parser = argparse.ArgumentParser(description="Apply blurring techniques and edge detection to an image.")
parser.add_argument("-i", "--image", required=True, help="Path to the input image.")
args = vars(parser.parse_args())

# Load the image from the specified path
image = cv2.imread(args["image"])

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not loaded. Check the file path.")
    exit()

# Display the original image
cv2.imshow("Original Image", image)

# Define a list of kernel sizes to use for blurring
kernel_sizes = [3, 5, 7]

# Function to apply Canny edge detection
def apply_canny(image):
    edges = cv2.Canny(image, 100, 200)
    return edges

# Apply Averaging Blur and perform edge detection
for k in kernel_sizes:
    # Apply averaging blur with the current kernel size
    blurred_avg = cv2.blur(image, (k, k))
    # Perform edge detection on the blurred image
    edges_avg = apply_canny(blurred_avg)
    # Display the blurred image and its edges
    cv2.imshow(f"Averaging Blur {k}x{k}", blurred_avg)
    cv2.imshow(f"Edges after Averaging Blur {k}x{k}", edges_avg)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Apply Gaussian Blur and perform edge detection
for k in kernel_sizes:
    # Apply Gaussian blur with the current kernel size
    blurred_gaussian = cv2.GaussianBlur(image, (k, k), 0)
    # Perform edge detection on the blurred image
    edges_gaussian = apply_canny(blurred_gaussian)
    # Display the blurred image and its edges
    cv2.imshow(f"Gaussian Blur {k}x{k}", blurred_gaussian)
    cv2.imshow(f"Edges after Gaussian Blur {k}x{k}", edges_gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Apply Median Blur and perform edge detection
for k in kernel_sizes:
    # Apply median blur with the current kernel size
    blurred_median = cv2.medianBlur(image, k)
    # Perform edge detection on the blurred image
    edges_median = apply_canny(blurred_median)
    # Display the blurred image and its edges
    cv2.imshow(f"Median Blur {k}x{k}", blurred_median)
    cv2.imshow(f"Edges after Median Blur {k}x{k}", edges_median)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Apply Bilateral Filter and perform edge detection
for k in kernel_sizes:
    # Apply bilateral filter with the current diameter size
    blurred_bilateral = cv2.bilateralFilter(image, k, 75, 75)
    # Perform edge detection on the blurred image
    edges_bilateral = apply_canny(blurred_bilateral)
    # Display the blurred image and its edges
    cv2.imshow(f"Bilateral Filter {k}", blurred_bilateral)
    cv2.imshow(f"Edges after Bilateral Filter {k}", edges_bilateral)

# Wait until a key is pressed to close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
