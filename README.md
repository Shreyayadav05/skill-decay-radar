# 🧠 Skill Decay Radar  
Detecting Human Reasoning Degradation Due to AI Dependence

---

## 📌 Overview
Skill Decay Radar is a human-centric web application that studies how continuous reliance on AI assistance affects independent human reasoning.  
The system compares restricted (no AI) and assisted (AI-enabled) problem-solving modes and quantifies potential cognitive skill decay using behavioral telemetry.

This project is designed for:
- College Major / Capstone Project
- Research Prototype
- Resume & Interview Demonstration

---

## 🎯 Problem Statement
AI tools improve short-term task performance, but their long-term impact on human reasoning skills is unclear.  
Most AI systems focus on output quality and speed while ignoring whether humans lose independent problem-solving ability over time.

This project aims to:
- Establish a baseline of unaided reasoning
- Compare it with AI-assisted reasoning
- Detect and quantify skill decay due to AI dependence

---

## ✨ Key Features
- Restricted vs Assisted reasoning modes
- Real-time reasoning tasks
- Time-based cognitive telemetry
- Accuracy and AI-dependence tracking
- User profile with submission history
- Interactive dashboard with graphs
- Skill Decay Score (single numerical metric)
- Clean UI/UX with navigation and back buttons
- Deployable web application

---

## 🏗️ Technology Stack
Frontend:
- HTML
- CSS
- Chart.js

Backend:
- Python (Flask)
- SQLite
- Flask Sessions

AI Integration (Optional):
- Google Gemini API

---

## 🧠 Skill Decay Measurement

### Metrics Collected
- Time taken to answer
- Correct / incorrect response
- AI usage (assisted vs restricted)
- User justification

### Skill Decay Score (SDS)
A single quantitative metric to summarize degradation:

SDS = (Post-Assisted Restricted Time − Baseline Time)  
      + (Baseline Accuracy − Post Accuracy) × 10

Higher SDS indicates higher potential skill decay.

---

## 🚀 Live Deployment
Live Application URL (Render):
https://skill-decay-radar.onrender.com

(Replace with your actual deployed link if different)

---

## ⚙️ Installation & Local Setup

1. Clone the repository:
git clone https://github.com/your-username/skill-decay-radar.git  
cd skill-decay-radar  

2. Create virtual environment:
python -m venv venv  
venv\Scripts\activate  

3. Install dependencies:
pip install -r requirements.txt  

4. Initialize database:
python init_db.py  

5. Run application:
python app.py  

Open in browser:
http://127.0.0.1:5000

---

## 📊 Application Pages
- Home: Solve reasoning tasks (restricted / assisted)
- Profile: View personal submission history
- Dashboard: Visualize thinking-time trends

---

## 🔐 Environment Variables (Optional AI)
If using Gemini AI, set:
GEMINI_API_KEY=your_api_key_here

---

## 🎓 Academic Significance
- Demonstrates Human–AI Interaction (HCI)
- Highlights ethical impact of AI dependence
- Uses data-driven cognitive analysis
- Strong relevance to AI, ML, and Data Science domains

---

## 🧠 Viva / Interview Talking Points
- Difference between performance and competence
- Importance of baseline (restricted mode)
- Ethical implications of AI over-reliance
- Interpretation of Skill Decay Score
- Limitations and future scope

---

## 🚧 Limitations
- Small-scale experimentation
- Early-stage trend analysis
- AI output variability

---

## 🔮 Future Enhancements
- Adaptive AI assistance
- Larger user studies
- Multiple reasoning domains
- Predictive skill decay modeling

---

## 🏆 Resume Line
Designed and deployed a human-centric AI system to detect and quantify reasoning skill decay caused by AI dependence using cognitive telemetry and a novel Skill Decay Score.

---

## 📜 License
This project is developed for educational and research purposes only.
