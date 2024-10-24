from matplotlib import pyplot as plt
import cv2

# Correct image path (use raw string to avoid backslash issues)
image_path = r'Examples\test.jpg'  # Replace with the correct path

# Load the image
image = cv2.imread(image_path)

# Check if the image was loaded properly
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    # Show the original image
    cv2.imshow("Original", image)

    # Split the image into Blue, Green, and Red channels
    chans = cv2.split(image)
    colors = ("b", "g", "r")

    # Plot the color histograms
    plt.figure()
    plt.title("Color Histograms")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    # Plot histogram for each channel
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        plt.plot(hist, color=color)
    plt.xlim([0, 256])
    plt.show()

    # Wait for a keypress and close the image window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
