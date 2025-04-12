# 👚 Virtual Dressing Room – Try Before You Thrift 👕

Step into the future of fashion with our **Virtual Dressing Room** – a real-time try-on experience. 
Overlay outfits on yourself live using your webcam and pose detection.

---

## 💡 About the Project

The **Virtual Dressing Room** is an Python project that uses **OpenCV** and **MediaPipe** to detect body landmarks and overlay clothing images onto a user’s shoulder area. 
It's an interactive, fun way to visualize outfits before buying them – perfect for thrift or online clothing platforms.

---

## 🔧 Tech Stack

### 🧠 Core Technologies
- **Python**
- **OpenCV** – Real-time computer vision
- **MediaPipe** – Pose estimation & landmark detection
- **cvzone** – Simplifies OpenCV+MediaPipe integration
- **NumPy** – Image manipulation and positioning

### 📦 Extras
- **Flask** *(optional)* – For web interface integration
- **Pillow** – Image loading and processing

---

## ✨ Features

- 📸 **Live Webcam Overlay** – Try on clothes in real time
- 💃 **Pose Detection** – Detect shoulder landmarks using MediaPipe
- 👕 **Dynamic Outfit Switching** – Use gestures (e.g. index finger up) to switch outfits
- 🗂️ **Wardrobe Folder Support** – Load all images from a `static/wardrobe/` directory
- ⚙️ **Modular Codebase** – Separate files for webcam logic and main app (`camera.py`, `app.py`)

---

## 🧵 How It Works

1. Detect body pose using **MediaPipe Pose**.
2. Track shoulder coordinates.
3. Overlay shirt images at correct position with optional hand gesture switching.
4. Display live webcam feed with outfit preview.

---

## 👩‍💻 Collaborators

| Role | Name | GitHub |
|------|------|--------|
| 🧠 Developer | **Keerthana** | [@HelloKeerthana](https://github.com/HelloKeerthana) |
| 💡 Developer | **Prakarshi, Naishi & Polina** | [@PrakarshiNaishiPolina](https://github.com/PrakarshiNaishiPolina) |
| 🎨 Developer | **Dikshya Pokhrel** | [@DikshyPokhrel](https://github.com/DikshyPokhrel) |
| ⚙️ Developer | **Sree Deepti** | [@ksdsree26](https://github.com/ksdsree26) |

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/HelloKeerthana/Virtual-dressing-room.git
Install dependencies:

pip install -r requirements.txt
Run the script:


python camera.py
📂 Project Structure

virtual-dressing-room/
│
├── camera.py         
├── app.py             
├── static/
│   └── wardrobe/     
├── templates/        
├── requirements.txt 

Coming soon!
Live demo images and videos will be added here.

🌟 Support
If you liked our project, drop a ⭐, share it, or remix it. Fashion meets code, and it looks good on you! 💁‍♀️💻✨

“Try it. Fit it. Love it – before it hits your cart.”
