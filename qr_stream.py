import os
import cv2
from qr_code import draw, decode_qrcode
from file_watcher import FileWatcher
decoder = cv2.QRCodeDetector()

# Hyper parameters
# Define full path to the atomically created real-time file:
IMG_PATH = os.environ['XDG_RUNTIME_DIR'] + '/robot_stream.jpg'
ESC_KEY = 27
BLUE = (255, 0, 0)
FONT = cv2.FONT_HERSHEY_TRIPLEX

def main():
    # create a file watcher
    watcher = FileWatcher(IMG_PATH)
    # in a for loop, watch all the atomic files, robot_stream.jpg and decode and report if those files contain a qr code
    while cv2.waitKey(1) not in [ord('q'), ESC_KEY]:
        if watcher.has_changed():
            img = cv2.imread(IMG_PATH)
            data = decode_qrcode(img)
            # NOTE: If the image contains a qr code, 'data' will have it as string, otherwise, it'll be s null string ('')
            cv2.imshow('preview', img)

if __name__ == "__main__":
    main()