# SafetyCamera

 **Selected for the Grand Finale of SAP HackFest held at PSG Institute of Technology and Applied Research, Coimbatore**   

SafetyCamera is a real-time AI-powered surveillance system that combines **YOLO-based weapon detection**, **gesture recognition**, and **instant alerts** to improve community safety. It is designed to help **police authorities** and **volunteers** by providing real-time monitoring and automated SOS alerts.

---

## Features

- **YOLOv8 Weapon Detection** – Detects knives, guns, and other dangerous weapons in real-time.  
- **Gesture Recognition (MediaPipe)** – Identifies distress signals (e.g., SOS hand gestures).  
- **Face Detection (OpenCV)** – Tracks human presence for context-aware alerts.  
- **Instant Alerts (Telegram API)** – Sends emergency messages with snapshots.  
- **Multi-Interface Support** –  
  - **Police Dashboard** (`web.py`) for law enforcement monitoring,  
  - **Volunteer Dashboard** (`web2.py`) for community support,  
  - **Main Application** (`app.py`) for running YOLO detection + alerts.  
- **Hackathon-Ready Deployment** – Recognized and selected for **SAP HackFest Grand Finale**.  

---

## Technology Stack

| Component        | Description                          |
|------------------|--------------------------------------|
| Python           | Core programming language            |
| OpenCV           | Face detection + image processing    |
| MediaPipe        | Gesture recognition                  |
| **YOLOv8**       | Real-time weapon detection           |
| Telegram API     | Emergency alert system               |
| Streamlit        | Police & Volunteer dashboards        |

---

## Setup & Run

Follow these steps to run the project:

1. **Clone the repository**  
2. **Create and activate a virtual environment**  
3. **Install dependencies using** `pip install -r requirements.txt`  
4. **Configure Telegram Bot Token and Chat ID** in `telegram_alerts.py`  
5. **Run the dashboards and app in separate terminals:**  
   - `streamlit run web.py` → Police Dashboard  
   - `streamlit run web2.py` → Volunteer Dashboard  
   - `python app.py` → Main Detection & Alert Engine (YOLO + MediaPipe)  
