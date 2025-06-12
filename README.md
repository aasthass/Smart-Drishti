# Smart-Drishti
AI Powered Assistive Glasses for the Visually Impaired. 

Workflow:

1. Button Pressed
2. Capture Image
3. Run YOLOv5 Detection
4. Convert YOLO Labels to objects detcted
5. Convert it to a sentence using NLP
6. Audio output through earphones


Features:

- Real-time object detection via YOLOv5
- Converts detected objects into a readable sentence
- Speaks the sentence aloud using `pyttsx3`
- Optional image captioning via Google Gemini
- Triggered via a physical push-button connected to Raspberry Pi

Hardware

- Raspberry Pi 3 or 4
- USB Camera or Raspberry Pi Camera(Global Shutter camera used here)
- Push Button connected to GPIO pin 17
- MicroSD Card (with Raspberry Pi OS installed)

Software

Install dependencies:

```bash
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt

Setup

1. Clone YOLOv5
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
cd ..
2.Connect the Push Button
Connect the button to GPIO 17 and GND on Raspberry Pi.

Run the following command on your Raspberry Pi:
python3 push.py
Then press the physical button to begin:
Image is captured
Objects are detected
Labels are converted to a sentence
Text is spoken aloud


Sample Output: 
Button Pressed! Capturing Image...
Image saved: captured.jpg
Running object detection...
Converted labels saved to: detected_objects.txt
Sentence: There are 2 dogs and 1 person in front of you.
Speaking...
