<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.28-FF4B4B?style=for-the-badge&logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/Supabase-Database-green?style=for-the-badge&logo=supabase" alt="Supabase">
  <img src="https://img.shields.io/badge/Face_Recognition-AI-orange?style=for-the-badge&logo=opencv" alt="Face Recognition">
  <img src="https://img.shields.io/badge/Voice_Analysis-DL-purple?style=for-the-badge&logo=speakerdeck" alt="Voice Analysis">
  <img src="https://img.shields.io/badge/Streamlit_Cloud-Live-FF4B4B?style=for-the-badge&logo=streamlit" alt="Live">
</div>

<br />

# 🎓 VisiEnroll

### AI-Powered Multi-Modal Attendance System

An intelligent attendance system that eliminates proxy attendance using dual biometric verification — **Face Recognition** and **Voice Analysis**. Teachers can mark attendance for an entire class in seconds by uploading a group photo, or use voice verification for contactless attendance. Built with Streamlit and deployed on Streamlit Cloud for instant access.

<p align="center">
  <a href="https://visienroll.streamlit.app/" target="_blank">
    <strong>🌐 Try it Live → visienroll.streamlit.app</strong>
  </a>
</p>

> ⚠️ **Note:** If the app shows "This app has gone to sleep due to inactivity", simply click **"Yes, get this app back up!"** and wait 1-2 minutes for redeployment.

---

## 🎥 Quick Demo Walkthrough

### 👨‍🏫 Teacher Flow (2 Minutes)

| Step | Action | What Happens |
|:----:|--------|--------------|
| **1** | Open [Live App](https://visienroll.streamlit.app/) → Click **Teacher Portal** | Register & Login with email/password |
| **2** | Go to **Manage Subjects** → Create Subject | Generate QR code & shareable link for students |
| **3** | Click **Take Attendance** → Upload group photo | AI detects & recognizes all enrolled students at once |
| **4** | OR try **Use Voice Attendance** → Record audio | Student says *"My name is X, I am present"* → AI matches voice |

### 👩‍🎓 Student Flow (2 Minutes)

| Step | Action | What Happens |
|:----:|--------|--------------|
| **1** | Click **Student Portal** → Capture photo via webcam | First-time: Register with name, email, and record voice sample |
| **2** | Scan QR code or open shared link | Enroll in teacher's subject instantly |
| **3** | Attendance auto-marked | Teacher triggers face/voice recognition — student just needs to be present |

---

## ✨ Key Features

### 🔐 **Proxy-Proof Attendance**
- **Face Recognition** — Detects & identifies students from individual or group photos
- **Voice Verification** — Confirms identity through unique voice embeddings
- **Dual Modality** — Use either or both methods for maximum reliability

### 📚 **Smart Classroom Management**
- **QR Code Enrollment** — Students join classes by scanning codes (no manual entry)
- **Subject Dashboard** — Real-time view of enrolled students & attendance records
- **Role-Based Portals** — Separate Teacher and Student interfaces

### ⚡ **Built for Speed**
- **Group Photo Processing** — Mark attendance for 30+ students in one click
- **Contactless Option** — Voice attendance requires no physical interaction
- **Instant Deployment** — No installation needed, works entirely in browser

---


| Technology | Role in System |
|------------|----------------|
| **Streamlit** | Full web UI — forms, camera, file uploads, audio recording |
| **Supabase** | Cloud database storing user profiles, face encodings, voice embeddings, attendance logs |
| **face_recognition (dlib)** | Detects faces in uploaded photos, generates 128-dim face encodings |
| **Resemblyzer + Librosa** | Extracts voice embeddings, compares speaker similarity |
| **Segno** | Generates QR codes for class enrollment links |
| **bcrypt** | Secure password hashing for teacher/student accounts |
| **Streamlit Cloud** | Zero-config hosting with automatic HTTPS |

---

## 🔬 How Biometric Verification Works

### 📸 Face Recognition
Upload Photo → dlib detects all faces → Generate 128-dim encoding for each face

### 🎙️ Voice Verification
Record Audio → Librosa preprocesses → Resemblyzer generates voice embedding


---

## 🎯 Highlights of The Project

- ✅ **No Installation Required** — Works entirely in browser via Streamlit Cloud
- ✅ **Real AI in Production** — Face recognition & voice analysis, not mock/demo data
- ✅ **Complete SaaS Flow** — Registration → Enrollment → Biometric Verification → Attendance Logging
- ✅ **Handles Edge Cases** — New student detection, multiple faces in one photo, voice in noisy environments
- ✅ **Database Persistence** — All data stored in Supabase (survives app sleep cycles)

---


---

## 🌐 Live Access

<div align="center">

| | |
|-------------------|------------------------------------------|
| **Live URL** | [visienroll.streamlit.app](https://visienroll.streamlit.app/) |
| **Platform** | Streamlit Cloud |
| **Database** | Supabase (PostgreSQL) |
| **Status** | 🟢 Live & Functional |

### Try it now — no setup required!

</div>

---

## 💡 Tips for Testing the Live App

1. **If app is hibernating**: Click "Yes, get this app back up!" — takes ~90 seconds
2. **Test as Teacher**: Register → Create subject → Share QR → Upload a group photo
3. **Test as Student**: Register with photo + voice → Enroll via QR → Get detected in teacher's photo
4. **For best face recognition**: Use well-lit, front-facing photos with clear faces
5. **For best voice match**: Record in quiet environment, speak clearly for 5+ seconds

---

## 🏆 Key Achievements

- 🔧 Built end-to-end biometric attendance system in Python
- ☁️ Deployed on cloud with persistent database (no local files)
- 🎯 Achieved reliable face matching across different poses and lighting
- 🎤 Implemented speaker verification using neural voice embeddings
- 📱 Created QR-based seamless classroom enrollment flow

---

<div align="center">
  <p>Built with ❤️ to eliminate proxy attendance</p>
  <p>
    <a href="https://visienroll.streamlit.app/"><strong>🔗 Try Live App</strong></a>
  </p>
</div>
