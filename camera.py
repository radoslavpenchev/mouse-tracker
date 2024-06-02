import cv2
from datetime import datetime

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def capture_image(self):
        ret, frame = self.cap.read()
        if ret:
            filename = f"static/images/{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            cv2.imwrite(filename, frame)
            return filename
        return None
