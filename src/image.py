import cv2
import mss
import numpy as np


class Image:
    def __init__(self, sct: mss.MSS):
        self.sct = sct

    def find_template(self, template_img, source_image=None):
        if source_image is None:
            screenshot = self.sct.grab(self.sct.monitors[1])
            source_image = np.array(screenshot)

        gray = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(gray, template_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.8:
            return max_loc

        return None

    def capture_region(self, x, y, width, height):
        zone = {
            "left": int(x),
            "top": int(y),
            "width": int(width),
            "height": int(height),
        }
        screenshot = self.sct.grab(zone)
        return np.array(screenshot)
