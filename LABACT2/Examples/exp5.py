import cv2
import numpy as np

# Specify the image path (use the correct path for your image)
image_path = r'Examples\test.jpg'  # Replace with your image path

# Load the image and convert it to grayscale
image = cv2.imread(image_path)

# Check if the image was loaded properly
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization to the grayscale image
    equalized_image = cv2.equalizeHist(gray_image)

    # Stack the original and equalized images side by side for comparison
    result = np.hstack((gray_image, equalized_image))

    # Display the original and equalized images
    cv2.imshow("Original vs Equalized", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
