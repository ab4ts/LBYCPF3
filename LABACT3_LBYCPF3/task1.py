import cv2
import numpy as np
import matplotlib.pyplot as plt




image_path = 'grup.jpg'  # Replace with your image path
image = cv2.imread(image_path)


# Check if the image is loaded
if image is None:
   print("Error: Could not load image. Check the file path.")
else:
   # Convert image to RGB
   image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


   # Apply different blurring techniques


  # Averaging blurring
   blur_avg = cv2.blur(image_rgb, (15, 15))


   # Gaussian Blurring
   blur_gaussian = cv2.GaussianBlur(image_rgb, (15, 15), 10)


   # Median Blurring
   blur_median = cv2.medianBlur(image_rgb, 15)


   # Bilateral Filtering
   blur_bilateral = cv2.bilateralFilter(image_rgb, 15, 150, 150)


   # Display the image outputs
   titles = ['Original Image', 'Averaging', 'Gaussian Blurring', 'Median Blurring', 'Bilateral Filtering']
   images = [image_rgb, blur_avg, blur_gaussian, blur_median, blur_bilateral]


   # Create a figure to display the results
   plt.figure(figsize=(15, 10))


   for i in range(5):
       plt.subplot(2, 3, i+1)
       plt.imshow(images[i])
       plt.title(titles[i])
       plt.xticks([]), plt.yticks([])


   plt.show()
