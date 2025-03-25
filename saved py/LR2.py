import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("csv_dataset.csv")

# Convert MBTI factors to MBTI Type
def get_mbti_type(row):
    energy = "E" if row["Energy"] <= 3 else "I"
    processing = "N" if row["Processing"] <= 3 else "S"
    decision = "T" if row["Decision"] <= 3 else "F"
    lifestyle = "J" if row["Lifestyle"] <= 3 else "P"
    return energy + processing + decision + lifestyle

df["MBTI Type"] = df.apply(get_mbti_type, axis=1)

# Assign MBTI group categories
mbti_groups = {
    "INTJ": "Analyst", "INTP": "Analyst", "ENTJ": "Analyst", "ENTP": "Analyst",
    "INFJ": "Diplomat", "INFP": "Diplomat", "ENFJ": "Diplomat", "ENFP": "Diplomat",
    "ISTJ": "Sentinel", "ISFJ": "Sentinel", "ESTJ": "Sentinel", "ESFJ": "Sentinel",
    "ISTP": "Explorer", "ISFP": "Explorer", "ESTP": "Explorer", "ESFP": "Explorer"
}
df["MBTI Group"] = df["MBTI Type"].map(mbti_groups)

# Define weight multipliers for subjects' confidence levels
subject_weights = {
    "Mathematics": {"STEM": 1.2, "ABM": 1.0, "HUMSS": 0.8},
    "Science": {"STEM": 1.3, "ABM": 0.9, "HUMSS": 0.7},
    "English": {"STEM": 1.0, "ABM": 1.1, "HUMSS": 1.2},
    "Filipino": {"STEM": 0.9, "ABM": 1.0, "HUMSS": 1.1},
    "Social Studies": {"STEM": 0.8, "ABM": 1.1, "HUMSS": 1.3},
    "Business": {"STEM": 0.7, "ABM": 1.4, "HUMSS": 1.0},
    "Computer": {"STEM": 1.3, "ABM": 0.8, "HUMSS": 0.7},
    "Arts & Design": {"STEM": 0.8, "ABM": 0.9, "HUMSS": 1.2},
    "Communication & Public Speaking": {"STEM": 0.9, "ABM": 1.2, "HUMSS": 1.3}
}

# Apply weighted scoring
def calculate_compatibility(row, strand):
    score = 0
    for subject, weights in subject_weights.items():
        score += row[subject] * weights[strand]
    return score

df["STEM Score"] = df.apply(lambda row: calculate_compatibility(row, "STEM"), axis=1)
df["ABM Score"] = df.apply(lambda row: calculate_compatibility(row, "ABM"), axis=1)
df["HUMSS Score"] = df.apply(lambda row: calculate_compatibility(row, "HUMSS"), axis=1)

# Normalize scores for better comparability
scaler = StandardScaler()
df[["STEM Score", "ABM Score", "HUMSS Score"]] = scaler.fit_transform(df[["STEM Score", "ABM Score", "HUMSS Score"]])

# Select relevant features for training
features = ["Mathematics", "Science", "English", "Filipino", "Social Studies",
            "Business", "Computer", "Arts & Design", "Communication & Public Speaking"]

X = df[features]
y = df[["STEM Score", "ABM Score", "HUMSS Score"]]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Decision Tree Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict strand compatibility scores
df["Predicted STEM"] = model.predict(X)[:, 0]
df["Predicted ABM"] = model.predict(X)[:, 1]
df["Predicted HUMSS"] = model.predict(X)[:, 2]

# Display results
df[["Predicted STEM", "Predicted ABM", "Predicted HUMSS"]].head()
