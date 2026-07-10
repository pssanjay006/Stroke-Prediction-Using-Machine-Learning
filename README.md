# 🧠 Stroke Prediction Using Machine Learning

A machine learning project that predicts whether a patient is at risk of stroke based on demographic, lifestyle, and medical information. This project applies data preprocessing, exploratory data analysis (EDA), feature engineering, class imbalance handling, and Logistic Regression for binary classification.

---

## 📌 Project Overview

Stroke is one of the leading causes of death and long-term disability worldwide. Early prediction of stroke risk can help healthcare professionals take preventive measures.

This project develops a binary classification model that predicts stroke occurrence using patient health records.

---

## 🎯 Objectives

- Perform data cleaning and preprocessing.
- Analyze the dataset using Exploratory Data Analysis (EDA).
- Handle missing values and categorical variables.
- Address class imbalance.
- Train a Logistic Regression model.
- Evaluate the model using multiple performance metrics.
- Save the trained model for future predictions.

---

## 📂 Dataset

Dataset: **Healthcare Stroke Dataset**

The dataset contains patient information such as:

- Gender
- Age
- Hypertension
- Heart Disease
- Ever Married
- Work Type
- Residence Type
- Average Glucose Level
- BMI
- Smoking Status
- Stroke (Target Variable)

**Target Variable**

- 0 → No Stroke
- 1 → Stroke

---

## 🛠 Technologies Used

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn
- Joblib

---

## 📊 Project Workflow

1. Data Loading
2. Data Cleaning
3. Missing Value Handling
4. Exploratory Data Analysis (EDA)
5. Feature Engineering
6. Encoding Categorical Features
7. Feature Scaling
8. Handling Class Imbalance
9. Model Training
10. Model Evaluation
11. Model Saving

---

## 📈 Exploratory Data Analysis

The project includes visualizations such as:

- Class Distribution
- Correlation Heatmap
- Age Distribution
- BMI Distribution
- Average Glucose Level Distribution
- Stroke Distribution
- Feature Relationships

---

## 🤖 Machine Learning Model

Algorithm Used:

- Logistic Regression

The model was trained after preprocessing and feature scaling.

---

## 📏 Evaluation Metrics

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC-AUC Score

---

## 📁 Project Structure

```
Stroke-Prediction-Using-Machine-Learning
│
├── data/
│   └── stroke.csv
│
├── notebooks/
│   └── final_stroke_prediction.ipynb
│
├── models/
│   ├── stroke_model.pkl
│   └── scaler.pkl
│
├── images/
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   ├── class_distribution.png
│   └── correlation_heatmap.png
│
├── requirements.txt
├── predict.py
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/pssanjay006/Stroke-Prediction-Using-Machine-Learning.git
```

Move into the project folder

```bash
cd Stroke-Prediction-Using-Machine-Learning
```

Install the required libraries

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Open Jupyter Notebook

```bash
jupyter notebook
```

Open

```
final_stroke_prediction.ipynb
```

Run all cells sequentially.

---

## 🔮 Making Predictions

After training, save the model:

```python
import joblib

joblib.dump(model, "stroke_model.pkl")
joblib.dump(scaler, "scaler.pkl")
```

Load the model for prediction:

```python
model = joblib.load("models/stroke_model.pkl")
scaler = joblib.load("models/scaler.pkl")
```

---

## 📊 Results

The project demonstrates a complete machine learning workflow for healthcare prediction, including:

- Data preprocessing
- Feature engineering
- Handling imbalanced data
- Logistic Regression model training
- Performance evaluation

---

## 💡 Future Improvements

- Compare multiple machine learning algorithms.
- Hyperparameter tuning using GridSearchCV.
- Deploy the model using Streamlit or Flask.
- Add explainability using SHAP or LIME.
- Build a web interface for predictions.

---

## 👨‍💻 Author

**Sanjay P S**

B.Tech Artificial Intelligence & Data Science

GitHub: https://github.com/pssanjay006

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
