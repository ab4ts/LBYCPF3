from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Specify the image path (use the correct path for your image)
image_path = r'Examples\test.jpg'  # Replace with your image path

# Load the image
image = cv2.imread(image_path)

# Check if the image was loaded properly
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    # Compute the 3D color histogram
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Normalize the histogram for plotting
    ratio = 5000 / np.max(hist)

    # Iterate through the 3D histogram and plot points
    for x in range(hist.shape[0]):
        for y in range(hist.shape[1]):
            for z in range(hist.shape[2]):
                if hist[x, y, z] > 0:
                    ax.scatter(x, y, z, s=hist[x, y, z] * ratio, color=(x / 7, y / 7, z / 7))

    ax.set_xlabel('Red Channel')
    ax.set_ylabel('Green Channel')
    ax.set_zlabel('Blue Channel')
    plt.title("3D Histogram (R, G, B Channels)")
    plt.show()
