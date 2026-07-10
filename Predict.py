import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load("models/stroke_model.pkl")
scaler = joblib.load("models/scaler.pkl")

print("Enter the following patient details:")

age = float(input("Age: "))
hypertension = int(input("Hypertension (0=No, 1=Yes): "))
heart_disease = int(input("Heart Disease (0=No, 1=Yes): "))
avg_glucose_level = float(input("Average Glucose Level: "))
bmi = float(input("BMI: "))

gender = input("Gender (Male/Female): ").strip().lower()
ever_married = input("Ever Married? (Yes/No): ").strip().lower()
work_type = input("Work Type (Private, Self-employed, Govt_job, children, Never_worked): ").strip()
residence = input("Residence Type (Urban/Rural): ").strip().lower()
smoking = input("Smoking Status (never smoked, formerly smoked, smokes, Unknown): ").strip()

# One-hot encoding
features = {
    "gender_Female": 1 if gender == "female" else 0,
    "gender_Male": 1 if gender == "male" else 0,

    "ever_married_No": 1 if ever_married == "no" else 0,
    "ever_married_Yes": 1 if ever_married == "yes" else 0,

    "work_type_Govt_job": 1 if work_type == "Govt_job" else 0,
    "work_type_Never_worked": 1 if work_type == "Never_worked" else 0,
    "work_type_Private": 1 if work_type == "Private" else 0,
    "work_type_Self-employed": 1 if work_type == "Self-employed" else 0,
    "work_type_children": 1 if work_type == "children" else 0,

    "Residence_type_Rural": 1 if residence == "rural" else 0,
    "Residence_type_Urban": 1 if residence == "urban" else 0,

    "smoking_status_Unknown": 1 if smoking == "Unknown" else 0,
    "smoking_status_formerly smoked": 1 if smoking == "formerly smoked" else 0,
    "smoking_status_never smoked": 1 if smoking == "never smoked" else 0,
    "smoking_status_smokes": 1 if smoking == "smokes" else 0,
}

sample = np.array([[
    age,
    hypertension,
    heart_disease,
    avg_glucose_level,
    bmi,

    features["gender_Female"],
    features["gender_Male"],
    features["ever_married_No"],
    features["ever_married_Yes"],
    features["work_type_Govt_job"],
    features["work_type_Never_worked"],
    features["work_type_Private"],
    features["work_type_Self-employed"],
    features["work_type_children"],
    features["Residence_type_Rural"],
    features["Residence_type_Urban"],
    features["smoking_status_Unknown"],
    features["smoking_status_formerly smoked"],
    features["smoking_status_never smoked"],
    features["smoking_status_smokes"]
]])

sample = scaler.transform(sample)

prediction = model.predict(sample)[0]
probability = model.predict_proba(sample)[0][1]

print("\nPrediction")
print("-" * 30)

if prediction == 1:
    print("⚠️ High Risk of Stroke")
else:
    print("✅ Low Risk of Stroke")

print(f"Probability of Stroke: {probability:.2%}")