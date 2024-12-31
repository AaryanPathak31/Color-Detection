import cv2  # Import OpenCV for computer vision operations
from PIL import Image  # Import PIL for advanced image processing
from util import get_limits  # Import custom function to calculate color limits

# Define the color to detect in BGR format
orange = [0, 165, 255]  # BGR value for orange

# Open the camera for video capture (index 2 corresponds to the third camera)
cap = cv2.VideoCapture(0)

# Infinite loop to process video frames in real time
while True:
    ret, frame = cap.read()  # Read a frame from the video source

    # Check if the frame was successfully captured
    if not ret:
        print("Failed to capture frame. Check the camera index or connection.")
        break

    # Convert the captured frame from BGR to HSV colorspace
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get lower and upper limits for the specified orange color
    lowerLimit, upperLimit = get_limits(color=orange)

    # Create a binary mask where pixels within the color range are white
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # Convert the binary mask to a PIL Image object for bbox calculation
    mask_ = Image.fromarray(mask)

    # Calculate the bounding box for the detected color region
    bbox = mask_.getbbox()

    # If a bounding box is detected, draw a rectangle on the frame
    if bbox is not None:
        x1, y1, x2, y2 = bbox  # Extract bounding box coordinates
        # Draw a green rectangle on the detected region
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # Display the processed frame with bounding box (if any)
    cv2.imshow('frame', frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera resource and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
