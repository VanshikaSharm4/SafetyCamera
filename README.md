# SafetyCame : AI-Powered Real-Time Public Safety & Threat Detection

> **From passive surveillance to intelligent intervention.**

### Selected for the Grand Finale of SAP HackFest

**Hosted at PSG Institute of Technology and Applied Research, Coimbatore**

SafetyCamera is an **AI-powered real-time surveillance and emergency response system** designed to transform conventional CCTV infrastructure into an intelligent safety network.

Instead of simply recording incidents after they happen, SafetyCamera continuously analyzes live camera feeds to identify **potential threats, dangerous weapons, human presence, and distress gestures** — and can immediately trigger automated emergency alerts.

The system combines **YOLOv8 computer vision, MediaPipe gesture recognition, OpenCV-based face detection, Streamlit dashboards, and Telegram-based emergency notifications** into a unified safety platform.

---

## Why SafetyCamera?

Traditional CCTV systems are fundamentally **reactive**.

They record hours of footage, but a human operator still has to monitor multiple screens, recognize a threat, determine whether it is serious, and initiate an appropriate response.

SafetyCamera introduces an **AI-assisted proactive layer** that continuously observes, analyzes, and responds to events in real time.

```text
LIVE CAMERA FEED
       │
       ▼
┌─────────────────────┐
│   AI VISION ENGINE  │
└─────────────────────┘
       │
       ├── Weapon Detection
       │
       ├── SOS Gesture Recognition
       │
       ├── Face / Human Detection
       │
       └── Context Analysis
       │
       ▼
┌─────────────────────┐
│   THREAT IDENTIFIED │
└─────────────────────┘
       │
       ▼
┌─────────────────────┐
│ AUTOMATED RESPONSE  │
└─────────────────────┘
       │
       ├── Police Dashboard
       ├── Volunteer Dashboard
       └── Telegram SOS Alert
```

The objective is to move surveillance from **simply documenting an incident to actively identifying potential threats as they unfold**.

> **Detect earlier. Alert faster. Respond smarter.**

---

## Project Showcase

<p align="center">
  <img src="img1" width="32%" alt="SafetyCamera AI Detection">
  <img src="img2" width="32%" alt="SafetyCamera Police Dashboard">
  <img src="img3" width="32%" alt="SafetyCamera Emergency Alert">
</p>

---



SafetyCamera was **selected for the Grand Finale of SAP HackFest**, hosted at **PSG Institute of Technology and Applied Research, Coimbatore**.

The project was developed around the challenge of applying modern AI and computer vision techniques to **real-world public safety and emergency response scenarios**.

Rather than treating computer vision as an isolated model, SafetyCamera combines multiple AI capabilities with monitoring interfaces and automated communication to create a **complete end-to-end safety workflow**.

The project demonstrates how AI can transform conventional surveillance infrastructure into an **intelligent early-warning and incident-response system**.

---

## Core AI Capabilities

### 1. YOLOv8 Weapon Detection

SafetyCamera integrates **YOLOv8** into the real-time surveillance pipeline to detect potentially dangerous objects directly from live camera frames.

The detection engine is designed to identify configured threat classes and highlight detected objects using bounding boxes and confidence information.

This allows monitoring personnel to immediately understand **what the system detected, where it was detected, and when the event occurred**.

---

### 2. SOS Gesture Recognition

Not every emergency can be communicated verbally.

SafetyCamera therefore incorporates **MediaPipe hand tracking and landmark analysis** to identify predefined distress gestures.

A recognized gesture can initiate the emergency-response pipeline:

```text
Hand Detected
      ↓
Landmark Extraction
      ↓
Gesture Classification
      ↓
SOS Recognized
      ↓
Emergency Trigger
      ↓
Alert + Snapshot
```

This creates an additional communication channel for individuals who may be unable to speak, make a phone call, or physically reach an emergency mechanism.

---

### 3. Face & Human Presence Detection

Using **OpenCV-based computer vision**, SafetyCamera can identify human presence within the monitored environment and provide additional contextual information around detected events.

Instead of treating every detection as an isolated object, the system can use surrounding human presence to provide a more meaningful interpretation of the monitored scene.

---

### 4. Automated Telegram Alerts

Speed is critical during emergency situations.

SafetyCamera integrates the **Telegram Bot API** to automatically deliver notifications when configured threat conditions occur.

An alert can include:

* Emergency notification
* Captured camera snapshot
* Detection context
* Detected threat
* Incident timestamp
* Configured monitoring information

This creates a direct communication channel between the AI detection engine and authorized responders, reducing dependence on continuous manual monitoring.

---

## Multi-Interface Monitoring System

SafetyCamera is not limited to a single monitoring screen.

The system provides dedicated interfaces designed around different stakeholders, creating a layered response architecture that connects **AI detection, human monitoring, and automated communication**.

### Police Dashboard

The police interface provides a centralized environment for authorized personnel to monitor AI-generated detections and respond to potential incidents.

### Volunteer Dashboard

The volunteer interface provides an additional monitoring layer for community safety volunteers, allowing them to receive relevant safety information and support incident response.

### Main Detection Engine

The main application runs the core computer vision pipeline independently from the dashboards, allowing the AI engine and visualization layers to remain modular and extensible.

---

## Technology Stack

### Artificial Intelligence & Computer Vision

* **YOLOv8** — Real-time object detection
* **MediaPipe** — Hand landmark and gesture recognition
* **OpenCV** — Image processing and human/face detection

### Application Development

* **Python** — Core application and AI pipeline
* **Streamlit** — Interactive monitoring dashboards
* **Jupyter Notebook** — Model experimentation and development

### Communication

* **Telegram Bot API** — Automated emergency notifications

### Frontend

* HTML
* CSS
* JavaScript
* Streamlit

---

## The Impact

SafetyCamera goes beyond building a standalone computer-vision model.

It combines **real-time perception, threat detection, gesture recognition, contextual analysis, monitoring dashboards, and automated emergency communication** into a single system.

The complete workflow can be summarized as:

> **Computer Vision → Threat Detection → Context → Automated Alert → Human Response**

The result is an AI-assisted surveillance architecture designed to shift security operations from **passive observation toward proactive threat awareness**.

Instead of relying entirely on someone noticing an incident after it occurs, SafetyCamera aims to continuously analyze the environment and bring potentially critical events to the attention of authorized responders in real time.

That combination of **AI, automation, computer vision, and human-in-the-loop response** is what makes SafetyCamera more than a surveillance application — it is a foundation for an intelligent public-safety platform.
