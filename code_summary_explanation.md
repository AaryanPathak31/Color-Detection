## File 1: ```main.py```
This is the main script that runs your color detection. Let's look at it part by part.

# 1. Import Libraries:
``` bash
import cv2
from PIL import Image
from util import get_limits
```
- cv2: This is the OpenCV library, which is used for computer vision tasks like capturing video, processing images, and detecting colors.
- PIL.Image: PIL (Python Imaging Library) is used to work with images. We use it to process the mask later and get the bounding box (the rectangle around the color).
- get_limits: This is a custom function we will use from util.py to calculate the color limits for the color we want to detect (in this case, orange).
# 2. Set Target Color:
``` bash
yellow = [0, 255, 255]  # yellow in BGR colorspace 
```
We define the color we want to detect. This color is set to yellow in BGR format (Blue, Green, Red). OpenCV uses BGR instead of RGB for color representation.
# 3. Capture Video:
``` bash
cap = cv2.VideoCapture(2)
```
cv2.VideoCapture(2): This opens the webcam for capturing live video. The 2 here refers to the default camera on your computer. If you have multiple cameras, you can change this number.
# 4. Start Video Capture Loop:
``` bash
while True:
    ret, frame = cap.read()
```
This line starts a loop to continuously capture frames (images) from the webcam.
cap.read(): This reads one frame from the webcam. The ret variable tells us if the frame was successfully captured, and frame contains the actual image data.
# 5. Convert Frame to HSV:
``` bash
hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```
- cv2.cvtColor(frame, cv2.COLOR_BGR2HSV): This converts the captured frame from BGR (used by OpenCV) to HSV (Hue, Saturation, Value). HSV makes it easier to detect specific colors because Hue corresponds to colors like red, green, blue, etc., and is more intuitive for color filtering.
# 6. Get Color Limits:
```
lowerLimit, upperLimit = get_limits(color=yellow)
```
- This calls the get_limits function from util.py to calculate the lower and upper bounds for the yellow color. It returns these limits, which will be used to create a mask (a filter) for detecting yellow.
# 7. Create Mask:
```
mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
```
cv2.inRange(hsvImage, lowerLimit, upperLimit): This creates a binary mask (black and white image) where:
White pixels represent areas that match the yellow color range.
Black pixels represent areas that do not match the yellow color.
# 8. Convert Mask to PIL Image:
``` 
mask_ = Image.fromarray(mask)
```
We convert the mask (created in the previous step) from a NumPy array to a PIL Image so we can process it further.
# 9. Find Bounding Box:

bbox = mask_.getbbox()
getbbox(): This function finds the bounding box (coordinates of the rectangle) around the white areas of the mask. It returns the top-left (x1, y1) and bottom-right (x2, y2) corners of the rectangle.
# 10. Draw Rectangle (Bounding Box):
```
if bbox is not None:
    x1, y1, x2, y2 = bbox
    frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
```
If the bounding box is found (i.e., the mask has detected yellow), a green rectangle is drawn around the detected area using cv2.rectangle().
(0, 255, 0) is the color green in BGR format, and 5 is the thickness of the rectangle.
# 11. Display the Frame:
``` bash
cv2.imshow('frame', frame)
```
This shows the current frame with the bounding box (if any) in a window.
# 12. Exit on 'q' Key:
```
if cv2.waitKey(1) & 0xFF == ord('q'):
    break
```
cv2.waitKey(1): This waits for 1 millisecond for a key press.
If the user presses the 'q' key, the loop breaks and stops the program.
# 13. Release Resources:
``` bash
cap.release()
cv2.destroyAllWindows()
```
cap.release(): This releases the webcam resource when we are done.
cv2.destroyAllWindows(): Closes any OpenCV windows that were opened during the program.
## File 2: util.py
This file contains the function get_limits() that calculates the lower and upper HSV limits for the target color.

# 1. Import Libraries:
``` bash
import numpy as np
import cv2
```
numpy: Used for numerical operations (like working with arrays).
cv2: OpenCV, used to handle image and video processing.
# 2. Define get_limits Function:
```
def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
```
- np.uint8([[color]]): We create a NumPy array with the input color in BGR format (like [0, 255, 255] for yellow). The array shape [[color]] is used to represent a single pixel in the image.
- cv2.cvtColor(c, cv2.COLOR_BGR2HSV): This converts the color from BGR to HSV. Now we have the Hue value of the target color.
# 3. Extract Hue Value:
``` bash
hue = hsvC[0][0][0]  # Get the hue value
```
The Hue value is extracted from the HSV image. This value represents the color itself (like red, blue, or yellow).
# 4. Handle Red Hue Wrap-around:
```
if hue >= 165:  # Upper limit for divided red hue
    lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
    upperLimit = np.array([180, 255, 255], dtype=np.uint8)
```
This block handles the special case for red, which wraps around the Hue spectrum (i.e., 0 and 180 are next to each other). If the Hue value is close to 180 (which represents red), we set a range from hue-10 to 180.
# 5. Handle Other Colors:
```
elif hue <= 15:  # Lower limit for divided red hue
    lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
    upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
```
- If the Hue is closer to 0 (the lower part of red), we adjust the range accordingly.
``` bash
else:
    lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
    upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
```
For other colors (not red), we simply create a range around the Hue value (hue ± 10) to capture variations of that color.
# 6. Return Limits:
```
return lowerLimit, upperLimit
```
Finally, the function returns the calculated lower and upper HSV limits, which will be used in main.py to create the color mask.
# Summary:
- main.py captures video from the webcam, processes each frame to detect the orange color, draws a bounding box around it, and displays it.
- util.py helps by providing the get_limits() function, which calculates the range of HSV values to detect a given color (like orange) accurately.
