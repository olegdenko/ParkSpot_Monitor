import numpy as np
import imutils
import easyocr
import re
import cv2


def recognize_plate(image):
    try:

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
        new_image = cv2.drawContours(mask, [location], 0,255, -1)
        new_image = cv2.bitwise_and(image, image, mask=mask)

        (x,y) = np.where(mask==255)
        (x1, y1) = (np.min(x), np.min(y))
        (x2, y2) = (np.max(x), np.max(y))
        cropped_image = gray[x1:x2+1, y1:y2+1]

        reader = easyocr.Reader(['en'])
        result = reader.readtext(cropped_image)
        plate_number = result[0][-2]
        plate_number = re.sub(r"[^a-zA-Z0-9]","",plate_number)

        return plate_number
    
    except Exception as e:
        return f"Error {str(e)}"
    
# image = cv2.imread("Cars14.png")
# plate_number = recognize_plate(image)

# if plate_number:
#     print(f"Recognized plate number: {plate_number}")
# else:
#     print("License plate recognition failed")