# Import the sys library for capturing program arguments.
# The camera_id can optionally be passed into the program.
import sys

# Import the OpenCV library for image processing.
import cv2

# Import the time library used for creating a timestamp when
# capturing an image from the webcam.
import time

# The numeric device id of the webcam.
# This value can be changed if you have multiple webcams.
camera_id = 0

if len(sys.argv) > 1 and (sys.argv[1].isnumeric()):
    camera_id = int(sys.argv[1])

# Create a new video capture object.
camera = cv2.VideoCapture(camera_id)

# Repeatedly read a frame from the camera and display it.
while True:
    # Read a frame from the camera
    return_value, image = camera.read()

    # It's possible to convert the mat to different formats such as grayscale.
    # eg: image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # See https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html

    # Display the image to the screen
    cv2.imshow('Webcam ' + str(camera_id), image)

    # Capture an image and exit when the 'c' key is pressed.
    # The waitKey function returns a 32 Bit integer value, and input is an 8 
    # bit ASCII, so apply a bitwise 'and' to 0xFF which is the hexadecimal 
    # number FF (which has an integer value of 255 or 
    # 00000000000000000000000011111111) as a binary representation.
    if cv2.waitKey(1) & 0xFF == ord('c'):
        # Generate a timestamp for our file
        timestamp = int(time.time())

        # Write the file to disk using the timestamp
        cv2.imwrite(str(timestamp) + '.jpg', image)
        break

# Release the web cam.
camera.release()

# Close all windows
cv2.destroyAllWindows()
