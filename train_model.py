import boto3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

s3 = boto3.client('s3')

bucket_name = "YOUR_BUCKET_NAME"
file_name = "cleaned_fraud_data.csv"

print("Downloading cleaned dataset...")
s3.download_file(bucket_name, file_name, "cleaned_data.csv")

df = pd.read_csv("cleaned_data.csv")

X = df.drop(["Class", "risk_flag"], axis=1)
y = df["Class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=50)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("Model accuracy:", accuracy)

with open("fraud_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Uploading model to S3...")
s3.upload_file("fraud_model.pkl", bucket_name, "fraud_model.pkl")

print("Model uploaded successfully.")
