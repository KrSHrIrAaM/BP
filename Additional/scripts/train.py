import os
import torch
from ultralytics import YOLO
from config import DATA_YAML, PRETRAINED_MODEL

def verify_dataset():
    """ Ensure dataset files exist before training. """
    if not os.path.exists(DATA_YAML):
        raise FileNotFoundError(f"❌ Error: Dataset YAML file '{DATA_YAML}' not found!")

    train_images = os.path.join(os.path.dirname(DATA_YAML), "images/train2017")
    if not os.path.exists(train_images):
        raise FileNotFoundError(f"❌ Error: Training images directory '{train_images}' not found!")

    print("✅ Dataset verified successfully.")

def train_model():
    """ Train YOLOv8 model with optimized settings. """
    try:
        # Verify dataset before training
        verify_dataset()

        # Load YOLOv8 model
        model = YOLO(PRETRAINED_MODEL)

        # Train the model with best model saving enabled
        model.train(
            data=DATA_YAML,
            epochs=20,
            imgsz=640,
            batch=8,
            device=0 if torch.cuda.is_available() else 'cpu',  # Uses GPU if available
            workers=4,
            name="train_run",
            save=True,
            save_period=1,  # 🔹 Ensures best model is saved periodically
            project="runs/detect",
            exist_ok=True
        )

        print("🚀 YOLOv8 training completed successfully!")

    except FileNotFoundError as fnf_error:
        print(f"❌ Dataset issue: {fnf_error}")
    except Exception as e:
        print(f"❌ Training failed: {e}")

if __name__ == "__main__":
    train_model()