from pathlib import Path

import torch
from yolov5 import Detector, Model, utils
# Define dataset paths and classes
train_path = Path("train")
val_path = Path("val")
classes = ["fish", "Jelly", "shark", "tuna"]

# Load the pre-trained YOLOv5 model
model = Detector(weights="yolov5s.pt")

# Define function to read annotations
def read_annotations(txt_path):
    with open(txt_path, "r") as f:
        annotations = []
        for line in f:
            xmin, ymin, xmax, ymax, class_id = line.strip().split(" ")
            annotations.append(
                {
                    "xmin": int(xmin),
                    "ymin": int(ymin),
                    "xmax": int(xmax),
                    "ymax": int(ymax),
                    "class_id": int(class_id),
                }
            )
    return annotations

# Define training function
def train():
    # Create datasets
    train_dataset = utils.datasets.LoadImagesAndLabels(
        train_path, classes, image_size=640, augment=True
    )
    val_dataset = utils.datasets.LoadImagesAndLabels(
        val_path, classes, image_size=640
    )

    # Create training pipeline
    model.model.train()
    optimizer = torch.optim.Adam(model.model.parameters(), lr=0.001)

    for epoch in range(100):
        for images, labels in train_dataset:
            # Forward pass
            preds = model(images)

            # Calculate loss
            loss = model.compute_loss(preds, labels)

            # Backpropagation
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        # Evaluate on the validation set
        val_results = utils.validate(model, val_dataset, classes=classes)
        print(f"Epoch: {epoch}, Validation mAP: {val_results['map']}")
