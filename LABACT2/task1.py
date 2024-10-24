import cv2
import numpy as np

# Create a blank image (500x500 pixels with 3 channels for RGB)
canvas = np.zeros((500, 500, 3), dtype="uint8")

# Define the center and the radius of the largest circle
center = (250, 250)
radius = 200

# Define colors for the target rings (alternating red and white)
colors = [(255, 0, 0), (255, 255, 255)]  # Red and White

# Draw concentric circles
for i in range(5, 0, -1):  # 5 rings
    color = colors[i % 2]  # Alternate between red and white
    current_radius = radius // 5 * i
    cv2.circle(canvas, center, current_radius, color, thickness=-1)

# Draw the bullseye (innermost circle)
cv2.circle(canvas, center, radius // 5, (0, 0, 0), thickness=-1)  # Black bullseye

# Show the image
cv2.imshow("Canvas with shapes", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
