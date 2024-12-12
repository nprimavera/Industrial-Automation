import time
import os
import cv2
from qr_code import decode_qrcode
from controller09_ex import Robot
from adafruit_crickit import crickit
from file_watcher import FileWatcher


# Initialize Decoder
decoder = cv2.QRCodeDetector()

# Initialize the Robot instance
robot = Robot()

# Set LED brightness
crickit.onboard_pixel.brightness = 0.01

# Define LED colors
RGB = dict(red=0xFF0000, green=0x00FF00, blue=0x0000FF)

# Define full path to the atomically created real-time file:
IMG_PATH = os.environ['XDG_RUNTIME_DIR'] + '/robot_stream.jpg'
ESC_KEY = 27
BLUE = (255, 0, 0)
FONT = cv2.FONT_HERSHEY_TRIPLEX

def blink_led(duration=3, color='blue'):
    """
    Blink the Crickit onboard LED for a specified duration and color.

    Args:
        duration (int): Duration in seconds for the blinking.
        color (str): Color of the LED ('red', 'green', 'blue').
    """
    try:
        for _ in range(duration * 2):  # Blink twice per second
            crickit.onboard_pixel.fill(RGB[color])  # Turn on the LED
            time.sleep(0.5)
            crickit.onboard_pixel.fill(0)  # Turn off the LED
            time.sleep(0.5)
    except KeyError:
        print(f"Invalid color '{color}' specified. Valid colors: {list(RGB.keys())}")

def detect_qr_and_act(timeout=100):
    """
    Detect QR codes while the robot moves forward at a minimum speed.
    Stop upon QR code detection or timeout.

    Args:
        cap: Initialized camera object.
        timeout (int): Maximum time in seconds to run detection.
    """
    start_time = time.time()  # Record the start time
    watcher = FileWatcher(IMG_PATH) # create a file watcher
    try:
        counter = 0
        while cv2.waitKey(1) not in [ord('q'), ESC_KEY]:
            # Check for timeout
            elapsed_time = time.time() - start_time
            if elapsed_time >= timeout:
                print(f"Timeout of {timeout} seconds reached. Stopping.")
                break
            # time.sleep(3)
            if watcher.has_changed():
                img = cv2.imread(IMG_PATH)
                data = decode_qrcode(img)
            if data:
                print(f"QR Code Detected: {data}")
                if data == "da3115":  # Replace with your target QR code
                    print("Target QR Code detected!")
                    
                    # Stop the robot
                    robot.move(0, 0, 0)  # Stop motors
                    
                    # Blink the LED
                    blink_led(duration=3, color='blue')
                    
                    # Pause for 3 seconds
                    time.sleep(3)

                    # Calculate time to move backward
                    travel_time = counter * 0.5
                    print(f"Travel time to QR code: {travel_time:.2f} seconds")

                    # Move backward for the same duration
                    robot.move(-0.37, -0.36, elapsed_time)  # Move backward at half throttle
                    break
            # Log progress
            print(f"Elapsed time: {int(elapsed_time)}s. No QR code detected yet.")

            # Robot keeps moving at minimal speed
            #robot.move(0.37, 0.35, 0.5)  # Continue moving forward at low speed in small steps
            counter += 1

    except KeyboardInterrupt:
        print("\nDetection loop interrupted by user.")
    except Exception as e:
        print(f"Error during QR detection and action: {e}")
    finally:
        print("Stopping QR detection loop.")
        robot.move(0, 0, 0)  # Ensure motors stop

def main():
    """
    Main function to initialize components and start the detection process.
    """
    try:
        # Start QR detection
        detect_qr_and_act(timeout = 60)
    except KeyboardInterrupt:
        print("\nMain function interrupted by user.")
    except Exception as e:
        print(f"Error in main function: {e}")

if __name__ == "__main__":
    main()
