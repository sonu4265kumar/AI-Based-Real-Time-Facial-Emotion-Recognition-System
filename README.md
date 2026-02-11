

---

```markdown
# 😊 AI-Based Real-Time Facial Emotion Recognition System

A deep learning–based system that detects and recognizes **human facial emotions in real time** using a webcam.  
The project uses **Convolutional Neural Networks (CNN)** trained on the **FER-2013 dataset** and performs live emotion prediction with OpenCV.

---

## 📌 Project Overview

Human emotions play a crucial role in communication.  
This project aims to automatically recognize facial emotions such as **Happy, Sad, Angry, Fear, Surprise, Disgust, and Neutral** from live video using Artificial Intelligence.

The system captures video from a webcam, detects faces, and predicts emotions in real time.

---

## 🎯 Objective

- To detect human faces from live video input  
- To recognize facial emotions using a trained deep learning model  
- To display predicted emotions in real time  

---

## ⭐ Features

- 🎥 Real-time emotion detection using webcam  
- 🧠 CNN-based deep learning model  
- 🙂 Detects 7 different emotions  
- ⚡ Fast and lightweight system  
- 🖥️ Works with a normal webcam  
- 👨‍💻 Easy to use and user-friendly  

---

## 😃 Emotions Detected

- Happy 😊  
- Sad 😔  
- Angry 😠  
- Fear 😨  
- Surprise 😮  
- Disgust 🤢  
- Neutral 😐  

---

## 🧠 Technologies Used

| Technology | Description |
|----------|-------------|
| Python | Main programming language |
| TensorFlow & Keras | Model building and training |
| CNN | Automatic facial feature extraction |
| OpenCV | Face detection and webcam handling |
| NumPy | Image and data processing |
| FER-2013 Dataset | Facial emotion dataset |

---

## 📂 Dataset

**FER-2013 Dataset**
- Grayscale facial images
- Image size: 48 × 48
- Total emotions: 7
- Used for training and validation

Dataset structure:
```

data/fer2013/
├── train/
│   ├── angry/
│   ├── happy/
│   ├── sad/
│   └── ...
└── test/
├── angry/
├── happy/
├── sad/
└── ...

```

---

## ⚙️ System Architecture

```

Webcam
↓
Face Detection (OpenCV)
↓
Image Preprocessing
↓
CNN Emotion Model
↓
Emotion Prediction

````

---

## 🧩 How It Works

1. Webcam captures live video  
2. OpenCV detects the face from each frame  
3. Face image is resized and converted to grayscale  
4. Trained CNN model predicts the emotion  
5. Emotion label is displayed on the screen  

---

## 🏋️ Model Training

- Model trained using **Convolutional Neural Network (CNN)**
- Optimizer: Adam  
- Loss function: Categorical Crossentropy  
- Achieved ~**50% validation accuracy**, which is good for FER-2013 dataset  

Training command:
```bash
python train_emotion_model.py
````

---



## 📜 License

This project is for **educational and academic use only**.

```
