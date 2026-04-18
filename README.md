# 🚀 AttentionX AI

<p align="center">
<b>Automated Content Repurposing Engine</b><br>
Built for the <b>UnsaidTalks AttentionX AI Hackathon</b>
</p>

<p align="center">
Turn long-form videos into viral short-form clips using Artificial Intelligence.
</p>

<p align="center">
👨‍💻 <b>Developed by Nune Sai Venkata Krishna</b>
</p>

---

## 🎥 Demo Video

https://drive.google.com/file/d/1zuMKkaFUm9ODZ3JA9Xpz3JhWB7xjHDSO/view?usp=sharing

---

## 🌐 Live Demo

Hosted prototype available via GitHub Codespaces preview.

---

# 🌟 Full Project Overview

AttentionX AI is a smart AI-powered platform that helps creators, mentors, educators, podcasters, and businesses convert long-form videos into multiple engaging short-form clips automatically.

Instead of manually editing one-hour videos, the platform detects valuable moments, generates captions, converts videos to vertical format, and exports ready-to-post content for Instagram Reels, TikTok, and YouTube Shorts.

## One Long Video → A Week’s Worth of Content

---

# 🎯 Problem Statement

Today’s creators produce valuable long-form content such as:

- 🎓 Lectures  
- 🎙 Podcasts  
- 🧑‍🏫 Mentorship Sessions  
- 💼 Workshops  
- 🎥 Interviews  
- 📚 Educational Talks  

However, modern audiences prefer short-form content.

As a result, the best moments stay hidden inside long videos.

AttentionX AI solves this by automatically finding the best moments and converting them into ready-to-post short clips.

---

# ✨ Core Features

## 🎯 Emotional Peak Detection

AI detects:

- motivational moments  
- viral reactions  
- energetic moments  
- high-retention scenes  
- valuable insights  

---

## 🎬 Smart Vertical Crop (9:16)

Automatically converts wide videos into mobile-first vertical reels.

Platforms supported:

- Instagram Reels  
- TikTok  
- YouTube Shorts  

---

## 📝 Dynamic Captions

Creates stylish captions with timing.

Benefits:

- higher retention  
- silent viewing support  
- accessibility  
- premium short-video feel  

---

## 🔥 Hook Title Generator

Examples:

- You Need To Hear This  
- Best Advice in 30 Seconds  
- Hidden Truth About Success  
- This Changed My Life  

---

## 📤 Multi-Clip Export

Generate multiple shorts from one long video.

Examples:

- 3 clips  
- 5 clips  
- 10 clips  

---

## ⚡ Fast Workflow

Hours of editing reduced to minutes.

---

# 🛠 Tech Stack

| Layer | Technology |
|------|------------|
| Frontend | Streamlit |
| Backend | Python |
| Speech Recognition | Whisper |
| Video Processing | MoviePy |
| Audio Analysis | Librosa |
| Computer Vision | OpenCV |
| Data Handling | Pandas |

---

# 🧠 Architecture

```mermaid
flowchart LR
A[Upload Long Video] --> B[Extract Audio]
B --> C[Whisper Transcription]
B --> D[Audio Energy Analysis]
C --> E[Transcript Segment Scoring]
D --> E
E --> F[Rank Emotional Peaks]
F --> G[Create Short Clips]
G --> H[Smart Crop to 9:16]
H --> I[Generate Captions + Hooks]
I --> J[Download Ready Shorts]
