<div align="center">

# 🧠 AI-Based Real-Time Facial Emotion Recognition System

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)
[![License](https://img.shields.io/badge/License-Academic%20Use-red?style=for-the-badge)](LICENSE)
[![Dataset](https://img.shields.io/badge/Dataset-FER--2013-green?style=for-the-badge)](https://www.kaggle.com/datasets/msambare/fer2013)

<br/>

> A deep learning system that detects and classifies **7 human facial emotions in real time** using a CNN trained on FER-2013 and OpenCV for live webcam inference.

<br/>

| 🎭 Emotions | 📐 Input Size | 🎯 Val. Accuracy | ⚡ Inference |
|:-----------:|:-------------:|:----------------:|:-----------:|
| 7 Classes   | 48 × 48 px    | ~50%             | Real-Time   |

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Demo](#-demo)
- [Emotions Detected](#-emotions-detected)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Technologies Used](#-technologies-used)
- [Dataset](#-dataset)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Model Training](#-model-training)
- [Model Performance](#-model-performance)
- [Prerequisites](#-prerequisites)
- [License](#-license)

---

## 🔍 Overview

Human emotions are a cornerstone of natural communication. This project builds a complete pipeline — from raw webcam frames to live emotion labels — using a **Convolutional Neural Network (CNN)** trained on the **FER-2013** benchmark dataset.

The system:
1. Captures frames from a webcam using **OpenCV**
2. Detects faces using a **Haar Cascade classifier**
3. Preprocesses the face crop (grayscale, resize to 48×48, normalise)
4. Runs it through a trained **CNN model** to predict one of 7 emotions
5. Overlays the predicted label on the live video feed

---

## 🎬 Demo

```
┌─────────────────────────────────────┐
│   📷 Live Webcam Feed               │
│                                     │
│   ┌──────────┐                      │
│   │  😊 HAPPY│  ← Bounding Box      │
│   │  Face    │     + Label          │
│   └──────────┘                      │
│                                     │
│   Press  Q  to quit                 │
└─────────────────────────────────────┘
```

---

## 😃 Emotions Detected

| Emotion   | Label     | Emoji |
|-----------|-----------|:-----:|
| Happy     | `happy`   | 😊    |
| Sad       | `sad`     | 😔    |
| Angry     | `angry`   | 😠    |
| Fear      | `fear`    | 😨    |
| Surprise  | `surprise`| 😮    |
| Disgust   | `disgust` | 🤢    |
| Neutral   | `neutral` | 😐    |

---

## ⭐ Features

- 🎥 **Real-time detection** — frame-by-frame inference from any webcam
- 🧠 **CNN-based model** — automatic hierarchical feature extraction
- 🙂 **7 emotion classes** — covers Ekman's basic emotions + Disgust & Neutral
- ⚡ **Lightweight pipeline** — runs on standard consumer hardware
- 🖥️ **Webcam agnostic** — works with any USB or built-in camera
- 👨‍💻 **Simple interface** — single command to start live detection
- 🔁 **Modular code** — training and inference are fully separated

---

## ⚙️ System Architecture

```
┌─────────────┐
│   Webcam    │  cv2.VideoCapture()
└──────┬──────┘
       │  Raw RGB Frame
       ▼
┌─────────────────────┐
│   Face Detection    │  Haar Cascade Classifier
│   (OpenCV)          │  → Bounding Box (x, y, w, h)
└──────┬──────────────┘
       │  Cropped Face Region
       ▼
┌─────────────────────┐
│  Preprocessing      │  Grayscale → Resize 48×48
│                     │  Normalise ÷ 255 → Reshape (1,48,48,1)
└──────┬──────────────┘
       │  Preprocessed Tensor
       ▼
┌─────────────────────┐
│  CNN Emotion Model  │  Conv2D → MaxPool → Dropout
│  (TensorFlow/Keras) │  → Dense → Softmax(7)
└──────┬──────────────┘
       │  Probability Distribution [7 classes]
       ▼
┌─────────────────────┐
│  Emotion Label      │  argmax → class name
│  Overlay (OpenCV)   │  cv2.putText() on frame
└─────────────────────┘
```

---

## 🧠 Technologies Used

| Technology | Version | Role |
|---|---|---|
| **Python** | 3.8+ | Core language |
| **TensorFlow & Keras** | 2.x | Model building, training & inference |
| **OpenCV** | 4.x | Webcam I/O & face detection |
| **NumPy** | 1.21+ | Image array processing & normalisation |
| **Matplotlib** | 3.x | Training curve visualisation |
| **FER-2013** | — | Labelled facial emotion dataset |

---

## 📂 Dataset

**FER-2013** — sourced from [Kaggle](https://www.kaggle.com/datasets/msambare/fer2013)

| Property | Value |
|---|---|
| Image format | Grayscale JPEG |
| Image size | 48 × 48 pixels |
| Total samples | ~35,887 images |
| Emotion classes | 7 |
| Train split | ~28,709 images |
| Test split | ~3,589 images |

> ⚠️ FER-2013 is known for label noise and inter-class ambiguity, which is why ~50% validation accuracy is a solid baseline for this dataset.

---

## 🗂️ Project Structure

```
emotion-recognition/
│
├── data/
│   └── fer2013/
│       ├── train/
│       │   ├── angry/
│       │   ├── disgust/
│       │   ├── fear/
│       │   ├── happy/
│       │   ├── neutral/
│       │   ├── sad/
│       │   └── surprise/
│       └── test/
│           ├── angry/
│           ├── disgust/
│           ├── fear/
│           ├── happy/
│           ├── neutral/
│           ├── sad/
│           └── surprise/
│
├── models/
│   └── emotion_model.h5        # Saved trained weights
│
├── train_emotion_model.py      # CNN training script
├── detect_emotion.py           # Real-time webcam inference
├── requirements.txt            # Python dependencies
└── README.md
```

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/emotion-recognition.git
cd emotion-recognition
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Activate — Linux/macOS
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the FER-2013 dataset

Place the dataset inside `data/fer2013/` following the structure shown above, or download it directly:

```bash
# Using Kaggle CLI
kaggle datasets download -d msambare/fer2013
unzip fer2013.zip -d data/fer2013/
```

---

## 🚀 Usage

### Run real-time emotion detection

```bash
python detect_emotion.py
```

- The webcam feed will open automatically.
- Detected faces will be highlighted with a bounding box and emotion label.
- Press **`Q`** to quit.

---

## 🏋️ Model Training

### Train from scratch

```bash
python train_emotion_model.py
```

### Training configuration

| Parameter | Value |
|---|---|
| Optimizer | Adam |
| Loss function | Categorical Crossentropy |
| Batch size | 64 |
| Epochs | 50 |
| Input shape | (48, 48, 1) |
| Output classes | 7 (Softmax) |

### CNN Architecture (summary)

```
Input (48×48×1)
    → Conv2D(32, 3×3, ReLU)  → BatchNorm → MaxPool → Dropout(0.25)
    → Conv2D(64, 3×3, ReLU)  → BatchNorm → MaxPool → Dropout(0.25)
    → Conv2D(128, 3×3, ReLU) → BatchNorm → MaxPool → Dropout(0.25)
    → Flatten
    → Dense(256, ReLU) → Dropout(0.5)
    → Dense(7, Softmax)
```

---

## 📊 Model Performance

| Metric | Value |
|---|---|
| Validation Accuracy | ~50% |
| Dataset | FER-2013 |
| State-of-the-art (reference) | ~73% |

> **Why ~50%?**  
> FER-2013 is one of the hardest facial emotion benchmarks due to its small 48×48 resolution, subjective labelling, and high similarity between classes like *Fear* and *Surprise*. A ~50% baseline with a custom CNN is a strong starting point — production systems use deeper architectures (ResNet, VGG) and data augmentation to push higher.

---

## 📋 Prerequisites

- Python 3.8 or higher
- Webcam (USB or built-in)
- Minimum 8 GB RAM
- GPU recommended for training (CPU inference works fine)

Install all Python dependencies:

```bash
pip install tensorflow opencv-python numpy matplotlib
```

Or via `requirements.txt`:

```
tensorflow>=2.8.0
opencv-python>=4.5.0
numpy>=1.21.0
matplotlib>=3.4.0
```

---

## 📜 License

This project is intended for **educational and academic use only**.  
Commercial use, redistribution, or production deployment requires explicit permission from the author.

---

<div align="center">

Made with ❤️ using TensorFlow · OpenCV · FER-2013

</div>
