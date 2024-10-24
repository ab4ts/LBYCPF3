import cv2
import matplotlib.pyplot as plt

# Load the image and convert it to grayscale
image = cv2.imread('LABACT2\photo1.png')  # Replace with your image path
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Function to plot histogram with different number of bins
def plot_histogram(image, bins):
    plt.hist(image.ravel(), bins=bins, range=[0, 256])
    plt.title(f"Histogram with {bins} bins")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.show()

# Plot histograms for different numbers of bins
for bins in [16, 32, 64, 128, 256]:
    plot_histogram(gray_image, bins)
