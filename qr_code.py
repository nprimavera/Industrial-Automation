import cv2


# Hyper params
code = 'QR_code/da3115.png'
BLUE = (255, 0, 0)
FONT = cv2.FONT_HERSHEY_TRIPLEX
detector = cv2.QRCodeDetector()



# Function to decode a given qrcode
# and draw a box around the detected code
def decode_qrcode(frame):
    data, matches, _ = detector.detectAndDecode(frame)
    if data:
        cv2.putText(frame, f'data: {data}', (30, 30), FONT, 1, BLUE)
        draw(frame, matches[0], BLUE, thickness=3)
    return data


# Function to draw a box around a code
def draw(frame, points, color, thickness):
    # convert to integer list of points (corners) of the code
    points = [(int(i), int(j)) for (i, j) in points]
    cv2.line(frame, points[0], points[1], color, thickness)
    cv2.line(frame, points[1], points[2], color, thickness)
    cv2.line(frame, points[2], points[3], color, thickness)
    cv2.line(frame, points[3], points[0], color, thickness)



def main():
    frame = cv2.imread(code)
    decoded_data = decode_qrcode(frame)
    print(f"decoded data: {repr(decoded_data)}")
    cv2.imshow('preview', frame)
    cv2.waitKey()



if __name__ == "__main__":
    main()

