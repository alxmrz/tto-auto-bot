import cv2
import mss
import numpy as np


def find_template(template_img, source_image=None):
    with mss.MSS() as sct:
        if source_image is None:
            screenshot = sct.grab(sct.monitors[1])
            source_image = np.array(screenshot)

        gray = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(gray, template_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.8:
            grid_x, grid_y = max_loc
            return grid_x, grid_y
        else:
            return None


def capture_region(x, y, width, height):
    with mss.MSS() as sct:
        zone = {
            "left": int(x),
            "top": int(y),
            "width": int(width),
            "height": int(height)
        }
        screenshot = sct.grab(zone)
        return np.array(screenshot)
