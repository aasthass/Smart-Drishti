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
