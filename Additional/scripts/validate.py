import os
from ultralytics import YOLO
from config import BEST_MODEL

def validate_model():
    """ Evaluate YOLOv8 model on the validation dataset. """
    try:
        # Ensure the trained model exists
        if not os.path.exists(BEST_MODEL):
            raise FileNotFoundError(f"❌ Error: Trained model '{BEST_MODEL}' not found!")

        # Load the trained YOLOv8 model
        model = YOLO(BEST_MODEL)

        # Run evaluation on the validation dataset
        metrics = model.val(
            split="val",  # 🔹 Uses the validation dataset
            batch=8,      # Adjust batch size based on GPU memory
            device=0,     # Use GPU if available
            verbose=True  # Show detailed evaluation logs
        )

        print("🚀 Evaluation completed successfully!")
        print("📊 Results:")
        print(metrics)

    except FileNotFoundError as fnf_error:
        print(f"❌ Validation issue: {fnf_error}")
    except Exception as e:
        print(f"❌ Validation failed: {e}")

if __name__ == "__main__":
    validate_model()