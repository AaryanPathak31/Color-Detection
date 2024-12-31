import numpy as np  # Import NumPy for numerical operations
import cv2  # Import OpenCV for image processing functions

# Function to calculate HSV range for a given BGR color
def get_limits(color):
    # Create a single-pixel image with the specified BGR color
    c = np.uint8([[color]])
    # Convert the BGR color to its HSV equivalent
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    # Extract the hue value from the HSV representation
    hue = hsvC[0][0][0]

    # Handle edge cases for colors near the red hue boundary in HSV space
    if hue >= 165:  # Upper limit for red hue wrap-around
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for red hue wrap-around
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        # For all other colors, define the range as hue ± 10
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit
