import cv2
import pyautogui
import numpy as np

# specify resolution
resolution = (1920,1080)

# specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# specify name of output file
filename = "Recording.mp4"

# specify frame rate
fps = 60.0

# creating VideoWriter object
out = cv2.VideoWriter(filename,codec,fps,resolution)

# create an empty window
cv2.namedWindow("Live",cv2.WINDOW_NORMAL)

# resized the window
cv2.resizeWindow("Live",480,270)

while True:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # convert screenshot to numpy array
    frame = np.array(img)

    # RGB
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    # writing to output file
    out.write(frame)

    # display the recording screen
    cv2.imshow('Live',frame)

    # stop recording
    if cv2.waitKey(1) == ord('q'):
        break
# Release the Video writer
out.release()

# destroy all windows
cv2.destroyAllWindows()
