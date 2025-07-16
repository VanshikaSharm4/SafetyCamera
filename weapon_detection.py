# weapon_detection.py (separate helper script)
import cv2
import numpy as np
import os
import glob
from telegram_alerts import send_telegram_alert
import threading

class WeaponDetector:
    def __init__(self):
        # Load class names
        with open("classes.txt", "r") as f:
            self.classes = [line.strip() for line in f.readlines()]

        # Load YOLO model
        self.net = cv2.dnn.readNet("yolov3_training_2000.weights", "yolov3_testing.cfg")
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

        if not os.path.exists("wep_img"):
            os.makedirs("wep_img")

        self.image_counter = self.get_next_image_number()

    def get_next_image_number(self):
        files = glob.glob("wep_img/wep_*.jpg")
        numbers = [int(f.split("_")[-1].split(".")[0]) for f in files if f.split("_")[-1].split(".")[0].isdigit()]
        return max(numbers, default=0) + 1

    def detect_and_save(self, img):
        height, width, _ = img.shape
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), swapRB=True, crop=False)
        self.net.setInput(blob)
        layer_names = self.net.getLayerNames()
        output_layers = [layer_names[i - 1] for i in self.net.getUnconnectedOutLayers()]
        outs = self.net.forward(output_layers)

        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        detected = False

        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(self.classes[class_ids[i]])
                color = (0, 0, 255)  # red
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
                detected = True

        if detected:
            filename = f"wep_img/wep_{self.image_counter}.jpg"
            cv2.imwrite(filename, img)
            
            print(f"[+] Weapon snapshot saved: {filename}")

            try:
                threading.Thread(target=send_telegram_alert, args=("Weapon detected!",), kwargs={"image_path": filename}, daemon=True).start()
            except Exception as e:
                print(f"Telegram alert failed: {e}")

            self.image_counter += 1

        return img


# # --- To be inserted in app.py ---
# # 1. Import at the top:
# # from weapon_detection import WeaponDetector

# # 2. After cap is set up (in main()):
# # weapon_detector = WeaponDetector()

# # 3. Inside the loop, right after ret, image = cap.read():
# # image = weapon_detector.detect_and_save(image)

