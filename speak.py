import os

# Read detected objects from YOLOv5 output file
def read_detected_objects(label_file="runs/detect/exp/labels/captured.txt"):
    try:
        with open(label_file, "r") as f:
            objects = [line.split()[0] for line in f.readlines()]  # Read object class names

        if objects:
            detected_str = ", ".join(objects)
            os.system(f'espeak "Detected objects: {detected_str}"')  # Speak detected objects
        else:
            os.system('espeak "No objects detected"')

    except FileNotFoundError:
        os.system('espeak "No detection results found"')

# Run text-to-speech
read_detected_objects()
