<<<<<<< HEAD
# 🌍 Air Quality Prediction System (PM2.5)

An AI-based agentic system designed to predict **PM2.5 air pollution levels** using environmental and temporal features.  
The system integrates machine learning with an interactive Jupyter Notebook UI to provide predictions, AQI classification, and health recommendations.

---

## 📌 Project Overview

Air pollution poses serious health risks, particularly fine particulate matter (PM2.5), which can penetrate deep into the respiratory system.  
This project predicts PM2.5 concentrations using a trained **Ridge Regression model** and interprets results through an **agent-based architecture**.

The system is implemented entirely in **Python** and executed within **Jupyter Notebook** using **ipywidgets** for user interaction.

---

## 🧠 System Architecture (Agent-Based)

The project follows a modular **Agentic AI design**:

### 1️⃣ Data Preprocessing Agent
- Cleans and validates raw user inputs
- Handles missing values and formatting
- Ensures inputs are suitable for the prediction model

### 2️⃣ Prediction Agent
- Loads the trained PM2.5 machine learning model
- Ensures feature consistency between training and inference
- Generates PM2.5 predictions

### 3️⃣ Decision Agent
- Classifies predicted PM2.5 into AQI categories
- Generates health-based recommendations
- Acts as an interpretation layer for end users

---

## 📊 Dataset Description

The dataset contains air quality measurements and temporal features:

**Key Features Used:**
- CO
- NO₂
- SO₂
- PM2.5 (target variable)
- Lag features (previous PM2.5 and NO₂)
- Temporal features (year, month, day, day of week)

---

## ⚙️ Machine Learning Model

- **Algorithm:** Ridge Regression
- **Target Variable:** PM2.5
- **Feature Engineering:**
  - Lag features to capture temporal dependency
  - Temporal features for seasonal trends
- **Evaluation Metrics:**
  - MAE (Mean Absolute Error)
  - RMSE (Root Mean Squared Error)
  - R² Score

---

## 🖥️ User Interface

- Built using **ipywidgets**
- Runs entirely inside Jupyter Notebook
- Clean, professional dashboard layout
- Allows users to input:
  - Temperature
  - Humidity
  - NO₂ concentration
- Displays:
  - PM2.5 prediction
  - AQI status
  - Health recommendations

---

## 📁 Project Structure

Air_Quality_Prediction/
│
├── notebooks/
│ ├── agents/
│ │ ├── data_preprocessing_agent.py
│ │ ├── prediction_agent.py
│ │ └── decision_agent.py
│ │
│ ├── final_pm2_5_model.pkl
│ └── main_ui.ipynb
│
├── predictions.csv
├── README.md
└── requirements.txt


---

## 🚀 How to Run the Project

1. Clone or download the repository
2. Create and activate a Python environment
3. Install dependencies:
   pip install -r requirements.txt

Open Jupyter Notebook:

        jupyter notebook
        
Run main_ui.ipynb and interact with the dashboard

📦 Requirements

Python 3.9+
pandas
numpy
scikit-learn
ipywidgets
matplotlib 

🎯 Key Highlights

✔ Agent-based modular architecture
✔ Time-series aware feature engineering
✔ Interactive Jupyter UI
✔ Clean and reproducible pipeline
✔ Suitable for academic submission and demonstrations

🔮 Future Improvements

Add real-time data integration

Improve lag feature handling using stored history

Experiment with advanced models (Random Forest, XGBoost)

Deploy as a web application

👤 Author
            Amina Noor
    Air Quality Prediction System – AI Project
=======
# Artificial Intelligence Project – Air Quality Prediction

## Description
This project uses **Artificial Intelligence / Machine Learning** to predict air quality based on environmental data.  
It estimates the **Air Quality Index (AQI)** using parameters such as:

- Temperature  
- Humidity  
- Carbon Monoxide (CO)  
- Nitrogen Dioxide (NO2)  
- Particulate Matter (PM2.5 / PM10)  

The goal is to **provide insights and early warnings** about air pollution to help reduce health risks.

---

## Features
- Predicts AQI using AI/ML algorithms  
- Visualizes air quality trends with graphs  
- Easy-to-use Python scripts and Jupyter Notebook  
- Can be extended for real-time monitoring  

---

## Technologies Used
- **Programming Language:** Python  
- **Libraries:**  
  - `pandas` – Data processing  
  - `numpy` – Numerical operations  
  - `scikit-learn` – Machine learning models  
  - `matplotlib` / `seaborn` – Data visualization  
- **IDE / Tools:** Jupyter Notebook, VS Code, Anaconda  

---

## Installation
1. Clone the repository:
2. Navigate to the project folder:
cd Artificial-Intelligence-Project--AirQualityPrediction
3. Install required Python libraries:
pip install -r requirements.txt
```bash
git clone https://github.com/YourUsername/Artificial-Intelligence-Project--AirQualityPrediction.git
>>>>>>> c8d0f4d597aaa84022abdc41ac7c2806c724da15
