# 🍽️ Food Waste Prediction System

A Machine Learning-based web application that predicts the amount of food waste generated in a college hostel or mess. The system helps optimize food preparation, reduce unnecessary waste, and support sustainable food management.

## 🌐 Live Demo

https://food-waste-prediction-7rqd.onrender.com

---

## 📌 Project Overview

The Food Waste Prediction System uses Machine Learning to estimate the quantity of food likely to be wasted based on factors such as day, meal, menu, number of students present, weather, special events, examinations, and food prepared.

---

## ✨ Features

- Predicts food waste in kilograms
- User-friendly web interface
- Trained using a custom dataset
- Real-time prediction
- Responsive design
- Deployed on Render

---

## 📊 Dataset

This project was trained using a **custom dataset** collected and prepared specifically for this application.

**Dataset Size:** 63 Records

### Features

- Day
- Meal
- Menu
- Students Present
- Weather
- Special Event
- Exam
- Food Prepared (kg)

### Target

- Food Wasted (kg)

---

## 🤖 Machine Learning Model

**Algorithm:** Random Forest Regressor

### Model Performance

- **R² Score:** **0.65**
- **Mean Absolute Error (MAE):** **1.23 kg**

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Git
- GitHub
- Render
- Gunicorn

---

## 📂 Project Structure

```
Food Waste Prediction/
│
├── dataset/
├── model/
├── templates/
├── app.py
├── train_model.py
├── predict.py
├── requirements.txt
├── Procfile
└── README.md
```

---

## 🚀 Installation

```bash
git clone <repository-url>
cd Food-Waste-Prediction
pip install -r requirements.txt
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 📚 Acknowledgements

- The Machine Learning concepts used in this project were learned through an introductory Machine Learning workshop.
- The dataset was independently collected and prepared specifically for this project.
- The Machine Learning model, data preprocessing, Flask backend, deployment configuration (including **Procfile**), and overall application logic were implemented independently.
- HTML and Flask deployment concepts were learned during the development of this project.
- AI assistance was used only for the frontend (HTML/CSS) design and UI enhancement.

---

## 👨‍💻 Developed By

**Dhanvanth U** - AIML II YEAR

---

## 📄 License

This project is intended for educational and learning purposes.
