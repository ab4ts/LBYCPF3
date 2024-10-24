import cv2
import numpy as np
import mahotas
import matplotlib.pyplot as plt

# List of image paths
image_paths = ['object.jpg', 'letterhead.png', 'noisy.png']

# Function to display images side by side
def show_images(titles, images, cmap='gray'):
    n = len(images)
    plt.figure(figsize=(20, 8))
    for i in range(n):
        plt.subplot(1, n, i + 1)
        plt.imshow(images[i], cmap=cmap)
        plt.title(titles[i])
        plt.axis('off')
    plt.show()

for img_path in image_paths:
    # Load the image in grayscale
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    original = image.copy()

    # Check if image is loaded
    if image is None:
        print(f"Error: Could not load image {img_path}")
        continue

    # Apply Simple Thresholding with a manual threshold
    _, simple_thresh = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

    # Apply Adaptive Mean Thresholding
    adaptive_mean_thresh = cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    # Apply Adaptive Gaussian Thresholding
    adaptive_gauss_thresh = cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Apply Otsu's Thresholding
    # Preprocess with Gaussian blur for better results
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    _, otsu_thresh = cv2.threshold(
        blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Apply Riddler-Calvard Thresholding using mahotas
    T_riddler_calvard = mahotas.thresholding.rc(image)
    riddler_thresh = image.copy()
    riddler_thresh[riddler_thresh > T_riddler_calvard] = 255
    riddler_thresh[riddler_thresh <= T_riddler_calvard] = 0
    riddler_thresh = riddler_thresh.astype(np.uint8)

    # Display the results
    titles = ['Original', 'Simple Threshold', 'Adaptive Mean',
              'Adaptive Gaussian', "Otsu's Method", 'Riddler-Calvard']
    images = [original, simple_thresh, adaptive_mean_thresh,
              adaptive_gauss_thresh, otsu_thresh, riddler_thresh]

    show_images(titles, images)
