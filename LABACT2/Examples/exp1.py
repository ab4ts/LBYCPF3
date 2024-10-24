import numpy as np
import cv2

# Create a blank canvas of size 300x300 with 3 channels for RGB
canvas = np.zeros((300, 300, 3), dtype="uint8")

# Define colors
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)

# Draw a green line from top-left to bottom-right
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw a red line from top-right to bottom-left with thickness 3
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw rectangles
# Green rectangle with no fill
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Red rectangle with a thickness of 5
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Blue filled rectangle
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
