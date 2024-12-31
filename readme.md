# Orange Color Detection with OpenCV

This project detects and highlights orange-colored objects in real-time using the webcam. It uses OpenCV for computer vision tasks and PIL for image processing. The project converts the input video feed to HSV colorspace and applies a color filter to detect regions containing the specified color (orange).

## Features
- Real-time orange color detection using webcam feed.
- Displays bounding boxes around detected orange-colored objects.
- Adjustable color detection range via HSV (Hue, Saturation, Value) color space.
- Uses OpenCV for video capture and processing.
- Utilizes PIL for extracting bounding boxes from the color mask.

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.x
- OpenCV (cv2 package)
- PIL (Pillow) for image processing
- NumPy for handling numerical operations

You can install the required packages using pip:

```bash
pip install opencv-python pillow numpy
