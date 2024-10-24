import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# Function to draw shapes on a blank canvas
def draw_shapes():
    canvas = np.zeros((400, 400, 3), dtype="uint8")  # Create a blank canvas (400x400)
    
    # Draw a green line from the top-left to the bottom-right corner
    cv2.line(canvas, (0, 0), (400, 400), (0, 255, 0), thickness=5)

    # Draw a red rectangle with a thickness of 3 pixels
    cv2.rectangle(canvas, (50, 50), (150, 150), (0, 0, 255), thickness=3)

    # Draw a filled blue circle with radius 50 pixels
    cv2.circle(canvas, (200, 200), 50, (255, 0, 0), thickness=-1)

    # Show the canvas
    cv2.imshow("Canvas with Shapes", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function to compute and display grayscale histogram
def grayscale_histogram(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()

# Function to compute and display color histograms (R, G, B)
def color_histograms(image):
    chans = cv2.split(image)  # Split the image into R, G, B channels
    colors = ("b", "g", "r")
    
    plt.figure()
    plt.title("Color Histograms")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        plt.plot(hist, color=color)
    plt.xlim([0, 256])
    plt.show()

# Function to compute and display 2D histogram (Red vs Green)
def two_d_histogram(image):
    chans = cv2.split(image)
    hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])

    plt.imshow(hist, interpolation="nearest")
    plt.title("2D Histogram (Green vs Red)")
    plt.colorbar()
    plt.show()

# Function to compute and display 3D histogram (R, G, B channels)
def three_d_histogram(image):
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in range(hist.shape[0]):
        for j in range(hist.shape[1]):
            for k in range(hist.shape[2]):
                if hist[i, j, k] > 0:
                    ax.scatter(i, j, k, s=hist[i, j, k], color=(i / 8, j / 8, k / 8))
    
    ax.set_xlabel('Red Channel')
    ax.set_ylabel('Green Channel')
    ax.set_zlabel('Blue Channel')
    plt.title("3D Histogram (R, G, B Channels)")
    plt.show()

# Function to apply and display histogram equalization
def histogram_equalization(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    eq_image = cv2.equalizeHist(gray_image)

    result = np.hstack((gray_image, eq_image))  # Side-by-side comparison

    cv2.imshow("Original vs Equalized", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function to run the workflow
def main():
    # Predefined image path
    image_path = r"photo1.png"  # Replace with actual image path

    # Check if file exists
    if not os.path.exists(image_path):
        print(f"Error: File not found at {image_path}")
        return

    # Load the image
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Unable to load the image. Please check the file format.")
        return

  
    draw_shapes()
    
    grayscale_histogram(image)
    color_histograms(image)
    two_d_histogram(image)    
    three_d_histogram(image)
    histogram_equalization(image)

if __name__ == "__main__":
    main()
