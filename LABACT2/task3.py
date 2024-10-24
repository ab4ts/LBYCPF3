import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load an image
image = cv2.imread('LABACT2\photo1.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Create a 3D histogram
hist_size = 32  # Number of bins for each channel
hist = cv2.calcHist([image], [0, 1, 2], None, [hist_size]*3, [0, 256, 0, 256, 0, 256])

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Prepare data for the 3D histogram plot
bin_edges = np.linspace(0, 255, hist_size + 1)
xpos, ypos, zpos = np.meshgrid(bin_edges[:-1], bin_edges[:-1], bin_edges[:-1], indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = zpos.ravel()

# Scale histogram values to better visualize
dx = dy = dz = np.ones_like(zpos)
values = hist.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average', color='b', shade=True)

# Labels and title
ax.set_xlabel('Red Channel')
ax.set_ylabel('Green Channel')
ax.set_zlabel('Blue Channel')
ax.set_title('3D Color Histogram')

plt.show()
