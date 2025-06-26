# customer-satisfaction-app
# ✈️ Airline Customer Satisfaction Predictor

This is a Flask web application that predicts customer satisfaction based on airline experience data. It uses a machine learning model trained on a dataset with features like age, flight distance, baggage handling, inflight entertainment, etc.

## 🚀 Live Demo
🔗 [Click Here to Open App](https://customer-satisfaction-app.onrender.com)

---

## 🧠 Features

- Built with Python + Flask
- Machine Learning model trained using scikit-learn
- Hosted on Render (Free Tier)
- Interactive form UI using Bootstrap
- Predicts whether a customer is **Satisfied** or **Not Satisfied**

- ![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey)
![Render](https://img.shields.io/badge/Deployed%20on-Render-brightgreen)

## 📸 Screenshots

### 📝 Input Form
![Input Form](screenshots/form.png)

### ✅ Prediction Result
![Prediction](screenshots/result.png)

## 🛠️ Tech Stack

- Python 3.10
- Flask
- NumPy
- scikit-learn
- HTML5 + CSS + Bootstrap
- Render (Deployment)


---

## 📁 Folder Structure
Customer_Satisfaction/
│
├── app.py # Flask backend
├── model.pkl # Trained ML model
├── columns.pkl # Column order for prediction
├── requirements.txt # All required Python packages
├── render.yaml # Render deployment config
├── templates/
│ └── index.html # HTML frontend
└── cust_satisfaction.csv # Dataset (optional)
