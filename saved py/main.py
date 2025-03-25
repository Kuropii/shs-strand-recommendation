import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
df = pd.read_csv("survey_data.csv")

# Function to determine MBTI type
def get_mbti(row):
    energy = "E" if row["Energy"] <= 3 else "I"
    processing = "N" if row["Processing"] <= 3 else "S"
    decision = "T" if row["Decision"] <= 3 else "F"
    lifestyle = "J" if row["Lifestyle"] <= 3 else "P"
    return energy + processing + decision + lifestyle

df["MBTI_Type"] = df.apply(get_mbti, axis=1)

# Define MBTI category mappings
mbti_categories = {
    "Analyst": ["INTJ", "INTP", "ENTJ", "ENTP"],
    "Diplomat": ["INFJ", "INFP", "ENFJ", "ENFP"],
    "Sentinel": ["ISTJ", "ISFJ", "ESTJ", "ESFJ"],
    "Explorer": ["ISTP", "ISFP", "ESTP", "ESFP"]
}

def get_category(mbti_type):
    for category, types in mbti_categories.items():
        if mbti_type in types:
            return category
    return "Unknown"

df["MBTI_Category"] = df["MBTI_Type"].apply(get_category)

# Encode categorical values
category_encoder = LabelEncoder()
strand_encoder = LabelEncoder()

df["MBTI_Category_Num"] = category_encoder.fit_transform(df["MBTI_Category"])
df["SHS_Strand_Num"] = strand_encoder.fit_transform(df["1. Which SHS strand did you take?"])

# Filter dataset to include only ABM and STEM students
df_filtered = df[df["1. Which SHS strand did you take?"].isin(["ABM", "STEM"])].copy()

# Trim spaces from column names
df_filtered = df_filtered.rename(columns=lambda x: x.strip())

# Select features: MBTI category + confidence levels in subjects
subject_features = ["Mathematics", "Science", "English", "Filipino",
                    "Social Studies", "Business", "Computer", "Arts & Design",
                    "Communication & Public Speaking"]

X = df_filtered[["MBTI_Category_Num"] + subject_features]
y = df_filtered["SHS_Strand_Num"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Decision Tree model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2%}")

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt="d", xticklabels=["ABM", "STEM"], yticklabels=["ABM", "STEM"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix for ABM & STEM")
plt.show()

# Decision Tree visualization
plt.figure(figsize=(12, 6))
plot_tree(model, feature_names=X.columns, class_names=["ABM", "STEM"], filled=True, fontsize=6)
plt.title("Decision Tree for ABM & STEM")
plt.show()

# Classification report
print("Classification Report:\n", classification_report(y_test, y_pred, target_names=["ABM", "STEM"]))