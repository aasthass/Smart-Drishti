import os
from collections import Counter

# COCO class labels (80 classes)
coco_classes = [
    "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
    "traffic light", "fire hydrant", "stop sign", "parking meter", "bench",
    "bird", "cat", "dog", "horse", "sheep", "cow",
    "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
    "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard",
    "sports ball", "kite", "baseball bat", "baseball glove", "skateboard",
    "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork", "knife",
    "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
    "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant",
    "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote",
    "keyboard", "cell phone", "microwave", "oven", "toaster", "sink",
    "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier",
    "toothbrush"
]

def pluralize(word, count):
    if count == 1:
        return word
    elif word == "person":
        return "people"
    elif word.endswith("y") and not word.endswith(("ay", "ey", "oy")):
        return word[:-1] + "ies"
    elif word.endswith(("s", "x", "sh", "ch")):
        return word + "es"
    else:
        return word + "s"

def convert_labels_to_sentence(label_folder, output_file_path):
    all_labels = []

    # Read label files
    for file_name in os.listdir(label_folder):
        if file_name.endswith(".txt"):
            file_path = os.path.join(label_folder, file_name)
            with open(file_path, "r") as f:
                for line in f:
                    parts = line.strip().split()
                    if parts:
                        class_id = int(parts[0])
                        if class_id < len(coco_classes):
                            class_name = coco_classes[class_id]
                            all_labels.append(class_name)

    # Build sentence
    if not all_labels:
        sentence = "No objects detected in front of you."
    else:
        counts = Counter(all_labels)
        phrases = [f"{count} {pluralize(name, count)}" for name, count in counts.items()]

        if len(phrases) == 1:
            sentence = f"There is {phrases[0]} in front of you."
        else:
            sentence = f"There are {', '.join(phrases[:-1])}, and {phrases[-1]} in front of you."

    # Save to text file
    with open(output_file_path, "w") as f:
        f.write(sentence + "\n")

    print(f"[✓] Saved sentence to: {output_file_path}")
    print(f"[🗣️] {sentence}")


# Example usage
if __name__ == "__main__":
    label_folder = "runs/detect/test/labels"
    output_file = "detected_objects.txt"
    convert_labels_to_sentence(label_folder, output_file)

