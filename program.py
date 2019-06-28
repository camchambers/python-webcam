# Import the OpenCV library for image processing which requires the 
# opencv-python library be installed
import cv2

# Import the time library used for creating a timestamp when saving the file
import time

# Create a new video capture object
camera = cv2.VideoCapture(0)

# Repeatedly read a frame from the camera and dipslay it
while True:

    # Read a frame from the camera
    return_value,image = camera.read()

    # It's possible to convert the mat to different formats here if we want to 
    # (ie. grayscale)
    # image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # Display the image to the screen
    # The imshow takes the following arguments: (window name, flags)
    cv2.imshow('image',image)

    # Wait for the 'c' key to be pressed
    # The waitKey function returns a 32 Bit integer value, and input is an 8 
    # bit ASCII, so apply a bitwise 'and' to 0xFF which is the hexadecimal 
    # number FF (which has an integer value of 255 or 
    # 00000000000000000000000011111111) as a binary representation
    if cv2.waitKey(1)& 0xFF == ord('c'):
        
        # Generate a timestamp for our file
        timestamp = int(time.time())

        # Write the file to disk using the timestamp
        cv2.imwrite(str(timestamp) + '.jpg',image)

        # Break out of the main loop
        break

# Free up the camera 
camera.release()

# Close all windows
cv2.destroyAllWindows()