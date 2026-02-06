import cv2
import numpy as np
from tensorflow.keras.models import load_model
from collections import deque

# Load face detector
face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

# Load pretrained emotion model (FER-2013)
emotion_model = load_model("emotion_model.h5", compile=False)

# Emotion labels (FER-2013 standard)
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Store last N predictions to smooth output
emotion_queue = deque(maxlen=7)

# Open webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) 

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)  # improves lighting robustness

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(80, 80)
    )

    for (x, y, w, h) in faces:
        roi = gray[y:y+h, x:x+w]
        roi = cv2.resize(roi, (48, 48))
        roi = roi.astype("float") / 255.0
        roi = np.reshape(roi, (1, 48, 48, 1))

        preds = emotion_model.predict(roi, verbose=0)
        emotion_index = np.argmax(preds)
        confidence = np.max(preds)

        emotion_queue.append(emotion_index)

        # Most frequent emotion in recent frames (smoothing)
        final_emotion = max(set(emotion_queue), key=emotion_queue.count)
        label = f"{emotion_labels[final_emotion]} ({confidence*100:.0f}%)"

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            label,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )

    cv2.imshow("AI Real-Time Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
