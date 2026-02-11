import boto3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# -------------------------------
# STEP 1: Connect to AWS S3
# -------------------------------
s3 = boto3.client('s3')

bucket_name = "barclays-ml-project-ameya"
file_name = "cleaned_fraud_data.csv"

print("Downloading cleaned dataset from S3...")
s3.download_file(bucket_name, file_name, "cleaned_data.csv")
print("Download complete.")

# -------------------------------
# STEP 2: Load dataset
# -------------------------------
df = pd.read_csv("cleaned_data.csv")
print("Dataset loaded:", df.shape)

# -------------------------------
# STEP 3: Prepare data
# -------------------------------
X = df.drop(["Class", "risk_flag"], axis=1)
y = df["Class"]

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training data ready.")

# -------------------------------
# STEP 4: Train model
# -------------------------------
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)

print("Model trained.")

# -------------------------------
# STEP 5: Accuracy check
# -------------------------------
accuracy = model.score(X_test, y_test)
print("Model accuracy:", accuracy)

# -------------------------------
# STEP 6: Save model
# -------------------------------
with open("fraud_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as fraud_model.pkl")

# -------------------------------
# STEP 7: Upload model to S3
# -------------------------------
print("Uploading model to S3...")
s3.upload_file("fraud_model.pkl", bucket_name, "fraud_model.pkl")

print("Model uploaded to AWS successfully.")
