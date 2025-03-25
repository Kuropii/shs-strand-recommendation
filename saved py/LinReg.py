import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv("cleaned_dataset.csv")

# Rename the column for easier reference
df.rename(columns={'1. Which SHS strand did you take?': 'Strand Taken'}, inplace=True)

# One-Hot Encode "Strand Taken"
strand_encoder = OneHotEncoder(sparse_output=False)
strand_encoded = strand_encoder.fit_transform(df[['Strand Taken']])
strand_encoded_df = pd.DataFrame(strand_encoded, columns=strand_encoder.get_feature_names_out(['Strand Taken']))
df = pd.concat([df, strand_encoded_df], axis=1)

# Select relevant features
features = ['Mathematics', 'Science', 'English', 'Filipino', 'Social Studies',
            'Business', 'Computer', 'Arts & Design', 'Communication & Public Speaking']

# Encode categorical MBTI feature
label_encoder = LabelEncoder()
df['MBTI GROUP'] = label_encoder.fit_transform(df['MBTI GROUP'])
features.append('MBTI GROUP')

# Normalize input features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

# Prepare result storage
predicted_scores = {}
mse_scores = {}
r2_scores = {}

# Train models for each strand
for strand in strand_encoded_df.columns:
    y = df[strand]
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # Store MSE and R² scores
    mse_scores[strand] = mean_squared_error(y_test, y_pred)
    r2_scores[strand] = r2_score(y_test, y_pred)

    # Predict for a new student
    new_student_data = {
        'Mathematics': 3, 'Science': 3, 'English': 3, 'Filipino': 3, 'Social Studies': 3,
        'Business': 3, 'Computer': 3, 'Arts & Design': 3, 'Communication & Public Speaking': 3,
        'MBTI GROUP': label_encoder.transform(['Diplomat'])[0]
    }
    new_student_df = pd.DataFrame([new_student_data])
    new_student_scaled = scaler.transform(new_student_df)
    predicted_scores[strand] = model.predict(new_student_scaled)[0]

# Normalize predicted scores to a percentage scale
total_score = sum(predicted_scores.values())
normalized_scores = {strand: (score / total_score) * 100 for strand, score in predicted_scores.items()}

# Print evaluation results
print("\n📌 Training MSE for each strand:")
for strand, mse in mse_scores.items():
    print(f"{strand}: {mse:.4f}")

print("\n📊 R² Scores for each strand:")
for strand, r2 in r2_scores.items():
    print(f"{strand}: {r2:.4f}")
 
print("\n📊 Predicted Compatibility Scores (Normalized %):")
for strand, score in sorted(normalized_scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{strand}: {score:.2f}%")
