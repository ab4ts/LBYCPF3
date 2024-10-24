from matplotlib import pyplot as plt
import cv2

# Correct image path
image_path = r'Examples\test.jpg'  # Use raw string (r"") to avoid escape sequence issues

# Load the image
image = cv2.imread(image_path)

# Check if the image was loaded properly
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Show the original grayscale image
    cv2.imshow("Original", gray_image)

    # Compute the grayscale histogram
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    # Plot the grayscale histogram
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()

    # Wait for a keypress and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
