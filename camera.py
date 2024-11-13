# Import required libraries
from datetime import datetime
import cv2
import os

# Hyper parameters
ESC_KEY = 27 # ASCII code of escape key
SPACE_BAR = 32 # ASCII code of space bar

# Image properties
WIDTH, HEIGHT, FPS, SAT, CON, BRI = 640, 480, 30, 0, 0, 50  # default value

# Define parameters where the real-time streaming will be saved
IMG_PATH = os.environ['XDG_RUNTIME_DIR'] + '/robot_stream.jpg'
TMP_PATH = os.environ['XDG_RUNTIME_DIR'] + '/robot_stream_tmp.jpg'

# A function to intiliazize camera and return the camera object
def init_camera():
    # Open camera's aperture
    cap = cv2.VideoCapture(0)
    # If not successful, raise error, exit
    assert cap.isOpened(), 'Error opening camera.'
    # customize the camera setting:
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, FPS)
    cap.set(cv2.CAP_PROP_BRIGHTNESS, BRI)
    cap.set(cv2.CAP_PROP_CONTRAST, CON)
    cap.set(cv2.CAP_PROP_SATURATION, SAT)
    return cap

# A function to save real-time frames.
# Notice IMG_PATH and TMP_PATH to understand where the latest frame is being saved.
def save_frames(cap):
    # cap: the initialized camera object
    count = 0
    while (key := cv2.waitKey(1)) not in [ord('q'), ESC_KEY]:
        count += 1
        ret, frame = cap.read()
        assert ret, 'Error reading frame from camera.'
        # flip the frame (our camera is upside down)
        frame = cv2.flip(frame, -1)
        cv2.imwrite(TMP_PATH, frame)
        os.replace(TMP_PATH, IMG_PATH)
        # Show the status of the frames in-place.
        
        # This is optional, you may comment it out:
        print('processing frames:', count, end='\r', flush=True)

# A function to real-time streaming of video and save a frame whenever space bar is pressed
def save_frame(cap):
    while (key := cv2.waitKey(1)) not in [ord('q'), ESC_KEY]:
        # read a frame from camera - ret: the status of reading
        ret, frame = cap.read()
        assert ret, 'Cannot read frame from camera.'
        # flip the frame (our camera is upside down)
        frame = cv2.flip(frame, -1)
        if key == SPACE_BAR:
            # save the image
            # Get the datetime; since file format can't be ':', replace it with dot '.'
            stamp = datetime.now().isoformat().replace(':', '.')
            cv2.imwrite(f'photo_{stamp}.jpg', frame)
        cv2.imshow('preview', frame)

def main():
    # initialize camera
    cap = init_camera()
    # 1) If you want to save a headshot or a frame while streaming camera real-time:
    #save_frame(cap)
    # 2) If you want to record the latest camera's frame:
    save_frames(cap)
    # close campera's apertture
    cap.release()

if __name__ == "__main__":
    main()