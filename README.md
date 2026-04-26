# 🌿 PlantGuardNet: AI-Powered Disease Detection

Ek high-performance Computer Vision system jo plant diseases ko real-time mein detect karta hai. Ye project specifically optimize kiya gaya hai Edge Devices (Raspberry Pi) ke liye taake kisaan (farmers) isse field mein asani se use kar saken.

---

## 🚀 Key Features

- **Architecture:** MobileNetV3-Small + **CBAM Attention Module** (Lightweight & Fast)
- **Accuracy:** 94.3% achieved on validation datasets
- **Edge Ready:** Fully compatible with Raspberry Pi using TFLite
- **Robustness:** Trained with advanced data augmentation to handle real-world lighting and backgrounds
- **Mobile Support:** Live camera capture for mobile devices

---

## 📊 Performance

| Metric | Value |
|--------|-------|
| Training Accuracy | 96%+ |
| Validation Accuracy | 94.3% |
| Inference Speed | ~150ms on Raspberry Pi 4 |

---

## 🛠️ Installation

### 1. Repository Clone Karein

```bash
git clone https://github.com/abdullahkhan-cs/PlantGaurdNet.git
cd PlantGaurdNet
```

### 2. Dependencies Install Karein

```bash
pip install -r requirements.txt
```

### 3. App Run Karein

```bash
python app.py
```

### 4. Browser Mein Open Karein

```
http://localhost:5000
```

---

## 🏗️ Project Structure

```
PlantGaurdNet/
├── app.py                  # Flask web application
├── requirements.txt        # Python dependencies
├── labels.txt             # Disease class labels
├── models/
│   └── PlantGuard_Mobile.tflite  # TensorFlow Lite model
├── templates/
│   ├── index.html         # Upload/Camera interface
│   └── result.html        # Results display
├── static/
│   ├── css/style.css     # Styling
│   └── script/js/script.js
└── README.md
```

---

## 🧠 Technical Highlights

Is project mein humne **Transfer Learning** aur **CBAM (Convolutional Block Attention Module)** ka istemal kiya hai. MobileNetV3 ke pre-trained weights ko use karte hue, humne model ko fine-tune kiya hai taake wo internet ki "random" images aur field ki pictures mein farq kar sake.

### 🔍 CBAM (Convolutional Block Attention Module)

CBAM ek lightweight attention mechanism hai jo model ki feature representation capability enhance karta hai:

| Component | Function |
|-----------|----------|
| **Channel Attention** | Important features par focus karta hai |
| **Spatial Attention** | Spatial locations ko smartly process karta hai |
| **Combined Attention** | Dono attention ko sequentially apply karta hai |

### Augmentation Techniques used:

- Random Rotation & Flips
- Color Jittering (Brightness/Contrast adjustment)
- Gaussian Noise for robust feature extraction

---

## 📱 Mobile Features

- **Live Camera:** Open camera button se direct capture
- **Photo Upload:** Gallery se image select karein
- **Low Confidence Warning:** 70% se kam confidence par warning display
- **Responsive Design:** Mobile par fully functional

---

## 🤝 Contributing

Open source community ka swagat hai! Agar aap isse behtar banana chahte hain:

1. Fork karein
2. Naya Feature branch banayein
3. Pull Request bhej dein

---

## 📜 License

Distributed under the MIT License. See LICENSE for more information.

---

## 🙏 Acknowledgments

- University: **QUEST** (optional)
- Mentor: Your mentor name here

---

## 🔗 Links

- **GitHub Repository:** https://github.com/abdullahkhan-cs/PlantGaurdNet
- **Live Demo:** Run locally using `python app.py`

---

*Made with ❤️ for farmers and plant health*