from PIL import Image
from ultralytics import YOLO
import easyocr
import os


def detect_license_plates(image_path):
    model = YOLO('runs/detect/train2/weights/best.pt')

    input_image = Image.open(image_path)

    plates_folder = 'plates'

    detections = model(input_image)

    license_plate_boxes = detections[0].boxes.data.cpu().numpy()

    reader = easyocr.Reader(['en'])

    for i, box in enumerate(license_plate_boxes):
        x1, y1, x2, y2, conf, cls = box
        license_plate = input_image.crop((x1, y1, x2, y2))

        plate_filename = os.path.join(plates_folder, f'license_plate_{i}.jpg')
        license_plate.save(plate_filename)

        results = reader.readtext(plate_filename)
        plate_number = results[0][1].replace("-", "").replace(":", "").replace(" ", "")
        print(f"License Plate {i+1} Text: {plate_number}")
        
image_path = 'dataset/test/images/Cars39_png.rf.fe511779e2f9eb9d412827d8d91f722b.jpg'


detect_license_plates(image_path)
