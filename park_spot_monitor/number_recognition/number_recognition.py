import numpy as np
import imutils
import easyocr
import re
import cv2
import os
from django.conf import settings 
import time
import tempfile

def recognize_plate(image_file):
    """
    Recognizes a plate number from an image file.

    Args:
        image_file: A file object representing the image.

    Returns:
        str: The recognized plate number, or an error message if recognition fails.
    """
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_image:
            temp_image.write(image_file.read())
            temp_file_path = temp_image.name

        image = cv2.imread(temp_file_path)
        if image is None:
            return "Error: can't read an image."
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
        edged = cv2.Canny(bfilter, 30, 200)

        keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(keypoints)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

        location = None
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 10, True)
            if len(approx) == 4:
                location = approx
                break

        mask = np.zeros(gray.shape, np.uint8)
        new_image = cv2.drawContours(mask, [location], 0, 255, -1)
        new_image = cv2.bitwise_and(image, image, mask=mask)

        (x, y) = np.where(mask == 255)
        (x1, y1) = (np.min(x), np.min(y))
        (x2, y2) = (np.max(x), np.max(y))
        cropped_image = gray[x1:x2 + 1, y1:y2 + 1]

        reader = easyocr.Reader(['en'])

        result = reader.readtext(cropped_image)
        if result:
            plate_number = result[0][-2]
            plate_number = re.sub(r"[^a-zA-Z0-9]", "", plate_number)
            os.remove(temp_file_path)
            return plate_number
        else:
            os.remove(temp_file_path)
            return "Error: unable to recognize plate number"
              

    except Exception as e:
        return f"Error {str(e)}"
