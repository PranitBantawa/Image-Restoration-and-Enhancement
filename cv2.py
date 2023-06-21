import cv2
import numpy as np


# Load the image
img = cv2.imread('C:/Users/prani/Desktop/IRE/IRE_env/image.jpg')
cv2.imshow('Image', img)
cv2.waitKey(0)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform histogram equalization
equalized = cv2.equalizeHist(gray)

# Create a horizontal stack of the original and equalized images
output = np.hstack((gray, equalized))

# Display the output image
cv2.imshow('Output', output)
cv2.waitKey(0)
