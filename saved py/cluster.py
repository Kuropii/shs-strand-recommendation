import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("stemhumss - Copy.csv")

# Rename the column for easier reference
df.rename(columns={'1. Which SHS strand did you take?': 'Strand Taken'}, inplace=True)

# One-Hot Encode "Strand Taken"
strand_encoder = OneHotEncoder(sparse_output=False)
strand_encoded = strand_encoder.fit_transform(df[['Strand Taken']])
strand_encoded_df = pd.DataFrame(strand_encoded, columns=strand_encoder.get_feature_names_out(['Strand Taken']))
df = pd.concat([df, strand_encoded_df], axis=1)

# Select relevant features for clustering
features = ['Mathematics', 'Science', 'English', 'Filipino', 'Social Studies',
            'Business', 'Computer', 'Arts & Design', 'Communication & Public Speaking']

# Encode categorical MBTI feature
label_encoder = LabelEncoder()
df['MBTI GROUP'] = label_encoder.fit_transform(df['MBTI GROUP'])
features.append('MBTI GROUP')

# Normalize input features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

# Applying K-Means Clustering
n_clusters = 3  # Choose the number of clusters you want to create
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Analyzing Cluster Results
print("\n📊 Cluster Assignments:")
print(df[['Strand Taken', 'MBTI GROUP', 'Cluster']].head(20))  # Display the first 10 rows with clusters

# Optional: Visualize Clusters (using first two features for simplicity)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=df['Cluster'], cmap='viridis')
plt.title('K-Means Clustering')
plt.xlabel('Feature 1: Mathematics (scaled)')
plt.ylabel('Feature 2: Science (scaled)')
plt.colorbar(label='Cluster')
plt.show()

# Now you can perform further analysis based on the clusters