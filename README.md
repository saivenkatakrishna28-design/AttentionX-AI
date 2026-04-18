# 🚀 AttentionX AI

<p align="center">
<b>Automated Content Repurposing Engine</b><br>
Built for the <b>UnsaidTalks AttentionX AI Hackathon</b>
</p>

<p align="center">
Turn long-form videos into viral short-form clips using Artificial Intelligence.
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

**One long video becomes a week’s worth of content.**

---

# 🎯 Problem Statement

Today’s creators produce valuable content in:

* 🎓 Lectures
* 🎙 Podcasts
* 🧑‍🏫 Mentorship Sessions
* 💼 Workshops
* 🎥 Interviews
* 📚 Educational Talks

However, modern audiences prefer short-form content.

Important moments remain buried inside long videos.

AttentionX AI solves this by automatically extracting the best moments and converting them into engaging short clips.

---

# ✨ Full Features

## 🎯 Emotional Peak Detection

AI analyzes transcript, keywords, and audio intensity to detect:

* motivational moments
* viral reactions
* energetic moments
* insightful advice
* engaging highlights

---

## 🎬 Smart Vertical Crop (9:16)

Automatically converts landscape videos into mobile-first short format.

Perfect for:

* Instagram Reels
* TikTok
* YouTube Shorts

---

## 📝 Dynamic Captions

Creates automatic subtitles with timing.

Benefits:

* better watch retention
* silent viewing support
* accessibility
* modern reel style appearance

---

## 🔥 Hook Title Generator

Creates engaging titles such as:

* You Need To Hear This
* Best Advice in 30 Seconds
* Hidden Truth About Success
* This Changed My Life

---

## 📤 Multi Clip Export

One long video can generate:

* 3 shorts
* 5 shorts
* 10 shorts

depending on detected highlights.

---

## ⚡ Fast Workflow

Hours of manual editing become minutes.

---

# 🛠 Tech Stack

| Layer              | Technology |
| ------------------ | ---------- |
| Frontend           | Streamlit  |
| Backend            | Python     |
| Speech Recognition | Whisper    |
| Video Editing      | MoviePy    |
| Audio Analysis     | Librosa    |
| Computer Vision    | OpenCV     |
| Data Handling      | Pandas     |

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
```

---

# 📁 Project Structure

```text id="k0v8rx"
AttentionX-AI/
│── app.py
│── README.md
│── requirements.txt
│── .env.example
│── demo-script.txt
│── submission-text.txt
│── project-description.txt
│── assets/
│── engine/
│   ├── config.py
│   ├── pipeline.py
│   ├── captions.py
│   ├── scorer.py
│   ├── cropper.py
│   └── utils.py
```

---

# 🚀 Run Locally

```bash id="g4w0du"
pip install -r requirements.txt
streamlit run app.py
```

---

# 📌 Important Note

For the strongest demo, use a video where:

* one speaker is clearly visible
* audio is clean
* there are energetic or insightful moments
* duration is between 3 to 20 minutes
* face remains visible often
* speech is clear

This makes the project look significantly stronger during judging.

---

# 📂 Submission Checklist

✅ Public GitHub Repository
✅ Full Source Code
✅ README Present
✅ Demo Video Link
✅ Working Prototype
✅ Clean Folder Structure

---

# 👨‍💻 Team

**Blue Stars**
Parul Institute of Engineering and Technology

---

# 🏆 Why This Project Stands Out

## Impact

Saves creators hours of editing time.

## Innovation

Combines multiple AI systems into one workflow.

## Technical Execution

Well-structured deployable prototype.

## User Experience

Simple upload and generate experience.

## Market Potential

Can scale into a creator SaaS startup.

---

# 🔮 Future Scope

* Multi-language subtitles
* AI thumbnails
* Voice cloning
* Direct social media publishing
* Analytics dashboard
* Collaboration workspace
* Subscription model

---

# 🙌 Final Note

## One Long Video → Endless Content Opportunities

Built with creativity, speed, and AI innovation.

---

# ❤️ Thank You
