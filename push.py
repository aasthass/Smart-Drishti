import cv2
import RPi.GPIO as GPIO
import time
import os

# GPIO setup for push button
BUTTON_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Function to capture an image
def capture_image(image_path="captured.jpg"):
    cap = cv2.VideoCapture(0)  # Open USB/Pi Camera
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(image_path, frame)  # Save image
        print(f"Image saved: {image_path}")
    cap.release()

# Main loop: Wait for button press
print("Press the button to capture an image...")

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            print("Button Pressed! Capturing Image...")
            capture_image()

            print("Running object detection...")
            #os.system("python detect.py --source captured.jpg --weights yolov5s.pt --save-txt")  # Runs detection
            os.system("python detect.py --weights yolov5s.pt --img 640 --conf 0.4 --source captured.jpg --save-txt --save-conf --project runs/detect --name test")
            
            print("Converting  labels to text...")            
            os.system("python converttts.py")

            print("Speaking detected objects...")
            os.system("python speak.py")  # Runs text-to-speech

            time.sleep(1)  # Debounce delay
except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
