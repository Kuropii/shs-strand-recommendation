import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv("cleaned_dataset.csv")

# Selecting features (academic performance, skills, MBTI, etc.)
features = [
    "Mathematics", "Science", "English", "Filipino", "Social Studies", "Business", "Computer",
    "Arts & Design", "Communication & Public Speaking", "Opportunity Satisfaction",
    "MBTI TYPE", "MBTI GROUP"
]

target = "1. Which SHS strand did you take?"

# Encode categorical features
le = LabelEncoder()
df["MBTI TYPE"] = le.fit_transform(df["MBTI TYPE"])
df["MBTI GROUP"] = le.fit_transform(df["MBTI GROUP"])
df[target] = le.fit_transform(df[target])

# Save mapping for decoding strand names later
strand_mapping = dict(zip(le.classes_, range(len(le.classes_))))
reverse_strand_mapping = {v: k for k, v in strand_mapping.items()}

# Normalize numerical features
scaler = StandardScaler()
df[features] = scaler.fit_transform(df[features])

# Split dataset into training and testing sets
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train k-NN Classifier with k=3
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Get probability predictions for compatibility scoring
y_prob = knn.predict_proba(X_test)

# Convert probabilities into a readable format
probability_df = pd.DataFrame(y_prob, columns=[reverse_strand_mapping[i] for i in range(len(reverse_strand_mapping))])

# Add actual strands for reference
probability_df["Actual Strand"] = [reverse_strand_mapping[label] for label in y_test]

# Convert probabilities to percentage format (individual rating, not summing to 100%)
probability_df.iloc[:, :-1] = probability_df.iloc[:, :-1] * 100  # Scale to 0-100%

# Show top recommendations per student
print("\nStrand Recommendation Compatibility Scores (Individual Ratings):\n")
for i in range(10):  # Show top 10 results
    student_scores = probability_df.iloc[i].drop(["Actual Strand"]).sort_values(ascending=False)
    print(f"Student {i+1} (Actual: {probability_df['Actual Strand'].iloc[i]}):")
    print(student_scores.to_string())  # Show all strands with their percentage
    print("-" * 40)

# Evaluate the model
accuracy = accuracy_score(y_test, knn.predict(X_test))
print(f"\nModel Accuracy: {accuracy:.2f}")
