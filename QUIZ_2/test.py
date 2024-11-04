import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the grayscale images
image1 = cv2.imread('QUIZ_2/1.jfif', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('QUIZ_2/2.jfif', cv2.IMREAD_GRAYSCALE)

# Check if images are loaded properly
if image1 is None or image2 is None:
    print("Error: One or both images not found or unable to load.")
    exit()

# Function to apply edge detection methods
def apply_edge_detection(image):
    edges = {}

    # Original Image
    edges['Original'] = image

    # Laplacian Edge Detection
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)
    edges['Laplacian'] = laplacian

    # Sobel Edge Detection
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # X direction
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Y direction
    sobel = cv2.magnitude(sobelx, sobely)
    sobel = cv2.convertScaleAbs(sobel)
    edges['Sobel'] = sobel

    # Canny Edge Detection without Gaussian Blur
    canny = cv2.Canny(image, 100, 200)
    edges['Canny'] = canny

    # Canny Edge Detection with Gaussian Blur
    blurred = cv2.GaussianBlur(image, (5, 5), 1.4)
    canny_blur = cv2.Canny(blurred, 100, 200)
    edges['Canny with Gaussian Blur'] = canny_blur

    return edges

# Apply edge detection on both images
edges_image1 = apply_edge_detection(image1)
edges_image2 = apply_edge_detection(image2)

# Function to display images side by side in one window
def display_results_in_one_window(edges_img1, edges_img2):
    titles = ['Original', 'Laplacian', 'Sobel', 'Canny', 'Canny with Gaussian Blur']
    images_img1 = [edges_img1[title] for title in titles]
    images_img2 = [edges_img2[title] for title in titles]

    plt.figure(figsize=(15, 6))

    for i in range(5):
        # Display images from Image 1 in the first row
        plt.subplot(2, 5, i + 1)
        plt.imshow(images_img1[i], cmap='gray')
        plt.title(f"{titles[i]} (Image 1)")
        plt.axis('off')

        # Display images from Image 2 in the second row
        plt.subplot(2, 5, i + 6)
        plt.imshow(images_img2[i], cmap='gray')
        plt.title(f"{titles[i]} (Image 2)")
        plt.axis('off')

    plt.tight_layout()
    plt.show()

# Display the results in one window
display_results_in_one_window(edges_image1, edges_image2)

# Document how each technique performs in identifying the unique shapes associated with a smile
def document_performance(edges, image_number):
    print(f"\nPerformance on Image {image_number}:")

    # Laplacian
    print("\nLaplacian Edge Detection:")
    print("- Highlights regions of rapid intensity change.")
    print("- May produce thicker edges and is sensitive to noise.")

    # Sobel
    print("\nSobel Edge Detection:")
    print("- Calculates gradient in x and y directions.")
    print("- Better at detecting edge orientation.")
    print("- Provides better edge continuity than Laplacian.")

    # Canny
    print("\nCanny Edge Detection:")
    print("- Multi-stage algorithm with noise reduction.")
    print("- Produces thin and precise edges.")
    print("- More effective in capturing subtle features like smile lines.")

    # Canny with Gaussian Blur
    print("\nCanny Edge Detection with Gaussian Blur:")
    print("- Pre-processing with Gaussian blur reduces noise.")
    print("- Enhances edge detection around mouth, cheeks, and eyes.")
    print("- Provides the clearest representation of smile-related features.")

# Document the performance for both images
document_performance(edges_image1, 1)
document_performance(edges_image2, 2)
