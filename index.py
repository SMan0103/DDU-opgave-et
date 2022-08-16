import numpy as np
import cv2 as cv

#define camera
camera = cv.VideoCapture(0)


#define the window name
window_name = "Live Video"

#define the window size
cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

# Make a window to display the video from the camera
cv.namedWindow("Video", cv.WINDOW_AUTOSIZE)

while True:
    # Read the next frame from the camera
    ret, frame = camera.read()

    # Display the frame in the window
    cv.imshow("Video", frame)

    # Check if the user wants to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


# Release the camera and close any open windows
camera.release()
cv.destroyAllWindows()


