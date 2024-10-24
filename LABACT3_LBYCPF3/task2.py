import cv2
import numpy as np
import matplotlib.pyplot as plt


# Load the image
image_path = 'grup.jpg'  # Replace with  your image
image = cv2.imread(image_path)


if image is None:
   print("Error: Could not load image. Check the file path.")
else:
   # Convert image to RGB
   image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


   # Kernel sizes example
   kernel_sizes = [15, 25, 35]


   # Function to display a set of images for filtering technique
   def display_filter_results(filter_name, images, kernel_sizes):
       plt.figure(figsize=(15, 5))
       for i, img in enumerate(images):
           plt.subplot(1, 3, i + 1)
           plt.imshow(img)
           plt.title(f'{filter_name} {kernel_sizes[i]}x{kernel_sizes[i]}')
           plt.xticks([]), plt.yticks([])


       plt.tight_layout()
       plt.show()


   # Blurring using Averaging
   avg_blurs = [cv2.blur(image_rgb, (k, k)) for k in kernel_sizes]
   display_filter_results('Averaging', avg_blurs, kernel_sizes)


   # Blurring using Gaussian
   gaussian_blurs = [cv2.GaussianBlur(image_rgb, (k, k), 0) for k in kernel_sizes]
   display_filter_results('Gaussian', gaussian_blurs, kernel_sizes)


   # Blurring using Median
   median_blurs = [cv2.medianBlur(image_rgb, k) for k in kernel_sizes]
   display_filter_results('Median', median_blurs, kernel_sizes)


   # Blurring using Bilateral Filtering (increasing parameters for stronger effect)
   bilateral_blurs = [cv2.bilateralFilter(image_rgb, k*2, 150, 150) for k in kernel_sizes]
   display_filter_results('Bilateral', bilateral_blurs, kernel_sizes)


   # Compare all techniques side by side
   kernel_index = 1 


   # Prepare images for side by side comparison
   comparison_images = [
       avg_blurs[kernel_index],
       gaussian_blurs[kernel_index],
       median_blurs[kernel_index],
       bilateral_blurs[kernel_index]
   ]


comparison_titles = ['Averaging', 'Gaussian', 'Median', 'Bilateral']


   # Display side by side comparison
plt.figure(figsize=(15, 5))
for i, img in enumerate(comparison_images):
       plt.subplot(1, 4, i + 1)
       plt.imshow(img)
       plt.title(f'{comparison_titles[i]} 25x25')
       plt.xticks([]), plt.yticks([])


plt.tight_layout()
plt.show()
