# Student Domain Recommender System 🎓

A Streamlit-based machine learning application designed to recommend the most suitable job domain for students based on academic and behavioral inputs.
## 🚩 Problem Statement

Many students struggle to identify the most aligned job role or domain due to lack of tailored guidance. This system aims to bridge that gap using historical academic and aptitude data to provide intelligent, data-driven career recommendations.

## 🔍 Project Objective

To develop a web-based recommendation system that takes multiple academic, logical, and behavioral inputs from students and suggests the best-suited job role or domain.

## 🧠 Machine Learning Approach

- Preprocessed the dataset containing 35+ student-related features using **Pandas** and **NumPy**.
- Performed **Exploratory Data Analysis (EDA)** to understand feature relevance.
- Selected meaningful features (e.g., subject-wise marks, communication skills, coding skill ratings, book interests, etc.) to build the model.
- Trained a **Decision Tree Classifier** to predict one of 8 job domains using Scikit-learn.
- Used **cross-validation** (`crossvalidation.ipynb`) to fine-tune model performance and prevent overfitting.
- Serialized the model using **Pickle** and integrated it with a Streamlit UI (`app.py`).

## 🧾 Features & Functionality

- Input form captures:
  - Technical subject marks (OS, CN, Algorithms, SE, etc.)
  - Communication and public speaking ratings
  - Book preference (used as a behavioral indicator)
  - Learning and working style (e.g., self-learning, working hours, team work, etc.)
- Mapped categorical responses to numerical values for model training.
- Provided 8 predicted job roles such as:
  - Data Science & Analytics
  - CRM & Technical Support
  - UI/UX & Design
  - Software Development & Engineering
  - Software Testing & QA
  - Network & Security
  - Management & Business
  - Database & Data Management

## 📊 Dataset Overview

The dataset includes diverse academic and personal attributes from student records such as:

- 📚 Academic Scores: OS, CN, Algorithms, Programming, SE, etc.
- 🧠 Cognitive Ratings: Logical quotient, communication, coding, memory, etc.
- 🧾 Behavioral Preferences: Book types, work style, management vs. technical interest
- 🎯 Target: `Suggested Job Role` (multi-class label)

You can view or download the dataset from [this link](https://drive.google.com/file/d/1MmoIka-RuexdLcTSpC3b6Fx-d2j2o9vk/view?usp=drive_link)

## 🌐 Hosted Application

Access the live project here: **[Student Domain Recommender - Web App](https://student-domain-recommender.streamlit.app/)**

## 📁 Project Files

| File                      | Description |
|---------------------------|-------------|
| `main.ipynb`              | Full data analysis, preprocessing, feature engineering, model training |
| `crossvalidation.ipynb`   | Performed K-fold CV to evaluate model robustness |
| `app.py`                  | Streamlit app UI with customized form and output handling |
| `model1.pkl`              | Trained Decision Tree model |
| `img2.png`                | Custom blurred background for the app |
| `studentplacementdata.csv` | Dataset with student attributes and job labels |

## 👨‍💻 Contributor
**Sanchit Singh**  
