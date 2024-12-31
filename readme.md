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
```
## Files 
- main.py: The main Python script that captures video from the webcam and processes frames to detect orange color.
- util.py: Contains the helper function get_limits(), which calculates the lower and upper HSV limits for a given color.

## How it Works
- Capture Video: The cv2.VideoCapture(2) function initializes the webcam feed.
- Convert to HSV: Each frame from the webcam is converted from BGR to HSV colorspace using cv2.cvtColor(). This step helps in better color detection.
- Color Masking: The frame is filtered to detect the orange color using cv2.inRange(), which creates a binary mask of pixels that fall within the HSV range for orange.
- Bounding Box: Using the PIL library, the bounding box of the detected orange region is calculated, and a rectangle is drawn around it.
- Display: The processed frame is displayed in real-time with bounding boxes drawn around detected orange regions.

## Customization
You can modify the target color by changing the orange variable in main.py with the BGR values of any other color you'd like to detect.
- Yellow: [0, 255, 255]
- Blue: [255, 0, 0]
- Green: [0, 255, 0]

Additionally, the ```get_limits()```  function in ```util.py``` can be adjusted for other color ranges if needed.

## Usage
- Run the main.py
```bash
python main.py
```
- The program will access the webcam and begin detecting orange-colored objects in real-time.
- To exit the program, press the q key.

## License
This project is licensed under the MIT License.

