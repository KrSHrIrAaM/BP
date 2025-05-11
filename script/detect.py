import cv2
import os
from ultralytics import YOLO
from config import BEST_MODEL


def detect_image(image_path):
    """ Run object detection on an image. """
    model = YOLO(BEST_MODEL)

    # Ensure the image exists before processing
    if not os.path.exists(image_path):
        print(f"❌ Error: Image '{image_path}' not found!")
        return

    results = model.predict(source=image_path, conf=0.25, device=0, show=True,save=True)
    print(results)


def detect_live():
    """ Run live object detection using webcam. """
    model = YOLO(BEST_MODEL)
    cap = cv2.VideoCapture(0)  # Open webcam (0 = default camera)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(source=frame, conf=0.25, device=0, show=True)

        # Display the frame
        cv2.imshow("YOLOv8 Live Detection", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    mode = input("Choose mode: [image/live]: ").strip().lower()

    if mode == "image":
        image_path = input("Enter image path: ").strip()
        detect_image(image_path)
    elif mode == "live":
        detect_live()
    else:
        print("❌ Invalid mode! Choose 'image' or 'live'.")