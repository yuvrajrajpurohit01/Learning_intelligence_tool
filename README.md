# 🎓 AI-Powered Learning Intelligence Tool

## 🔍 Project Overview

This project is an **AI-powered Learning Intelligence Tool** developed as part of a **Data Science & Machine Learning Internship Assessment**.

The tool analyzes learner behavior and performance data to generate **intelligent predictions and actionable insights** for mentors and administrators. It is implemented as a **fully executable AI system**, not a notebook or experimental script, and follows a **production-style architecture**.

All components of the system have been implemented, manually tested, and verified to be working correctly.  
Screenshots of execution and deployment (CLI and Streamlit) are attached for verification.

---

## 🎯 Objectives

The tool is designed to:

- Predict whether a student will complete a course  
- Detect students at risk of dropping out early  
- Identify difficult chapters based on learner behavior  
- Generate human-readable insights for informed decision-making  

---

## 🧠 AI Capabilities Implemented

### 1️⃣ Course Completion Prediction
- Implemented as a **binary classification problem**
- Uses a trained **Logistic Regression** model
- Predicts whether a student is likely to complete the course

### 2️⃣ Early Risk Detection
- Identifies students likely to drop out early
- Combines:
  - ML prediction results
  - Engagement behavior (time spent)
  - Performance metrics (assessment scores)

### 3️⃣ Chapter Difficulty Detection
- Detects difficult chapters using:
  - Dropout rate
  - Average time spent
  - Assessment scores
- Produces a ranked difficulty score per chapter

### 4️⃣ Insight Generation
- Outputs **human-readable insights**, including:
  - High-risk students list
  - Key factors affecting course completion
  - Chapters needing improvement

---

## 🏗️ System Architecture

The tool follows a modular AI system design:

1. **Data Ingestion Module**  
   - Loads and validates input CSV data

2. **Feature Engineering Module**  
   - Aggregates learner-level features from raw data

3. **Model Inference Module**  
   - Loads the trained ML model
   - Performs course completion prediction

4. **Analytics Module**  
   - Early risk detection
   - Chapter difficulty computation

5. **Insight Generation Module**  
   - Produces mentor/admin-friendly insights

6. **Interface Layer**
   - Command Line Interface (CLI) – mandatory
   - Streamlit Web Dashboard – optional

---

## 📁 Project Structure
- models/                      Saved ML models
- ├── completion_model.pkl     Trained course completion model

- app.py                       Streamlit web dashboard (optional UI)
- main.py                       CLI-based executable AI tool
- data_loader.py               Input data ingestion & validation
- feature_engineering.py        Feature creation logic
- inference.py                  Model loading & prediction
- chapter_difficulty.py         Chapter difficulty analysis
- insights.py                  Human-readable insight generation

- train_model.py               Offline model training script
- sample_input.csv              Sample input dataset
- requirements.txt             Project dependencies
- README.md                    Project documentation


Each component in this structure is functional and verified.

---

## 🛠️ Technology Stack

- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn  
- **Data Processing:** Pandas  
- **Model Persistence:** Joblib  
- **Interface:**  
  - Command Line Interface (CLI)  
  - Streamlit Web Dashboard (optional)

---

## 📥 Input Format

The tool accepts a **CSV file** with the following columns:

| Column Name | Description |
|-----------|-------------|
| student_id | Unique student identifier |
| course_id | Course identifier |
| chapter_order | Chapter sequence |
| time_spent | Time spent on chapter |
| score | Assessment score |
| completion_status | Chapter completion (0/1) |

A sample input file is provided as `sample_input.csv`.

---

## 📤 Output Format

The tool generates a **JSON report** containing:

- Course completion predictions per student  
- Early risk flags  
- Chapter difficulty analysis  
- Human-readable summary insights  

Example output file: report.json


---

## ▶️ How to Run the Project (CLI Execution)

### Step 1: Open a New Terminal
Navigate to the project root directory.

### Step 2: Install Dependencies
pip install -r requirements.txt
### Step 3: Run the AI Tool
python main.py --input sample_input.csv --output report.json

--- 

### 🌐 Optional Web Deployment (Streamlit)
An optional Streamlit-based web dashboard is provided for interactive usage.

Run Streamlit App
streamlit run app.py

---

### 🤖 Machine Learning Model Details

Model Used: Logistic Regression

Problem Type: Binary Classification

Features Used:

Average time spent

Average assessment score

Number of chapters completed

Training: Performed offline using train_model.py

Inference: Model loaded from completion_model.pkl

---

### 🤝 AI Usage Disclosure
#### AI tools (including ChatGPT) were used for:

- Architectural guidance

- Code structuring suggestions

- Documentation refinement

All machine learning logic, feature engineering, scoring mechanisms, and final implementation were independently written, verified, and executed by the author.






