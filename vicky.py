# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12QnWtAXAjbFrXwK_6nLDdvlJhq64lhj1
"""

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

def remove_background(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale image
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edges
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask with white background
    mask = np.ones_like(image) * 255

    # Draw contours on the mask
    cv2.drawContours(mask, contours, -1, (0, 0, 0), thickness=cv2.FILLED)

    # Invert the mask
    mask = cv2.bitwise_not(mask)

    # Remove the background using bitwise_and
    result = cv2.bitwise_and(image, mask)

    return result, gray

# Example usage
image_path = 'E:\background\kingfisher-2046453_640.jpg'
result, gray_image = remove_background(image_path)

# Display the original, grayscale, and result images
original_image = cv2.imread(image_path)
cv2_imshow(original_image)
cv2_imshow(gray_image)
cv2_imshow(result)