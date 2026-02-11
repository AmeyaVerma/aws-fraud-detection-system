from fastapi import FastAPI
import boto3
import pickle
import pandas as pd

app = FastAPI()

s3 = boto3.client('s3')
bucket_name = "YOUR_BUCKET_NAME"

print("Downloading model from S3...")
s3.download_file(bucket_name, "fraud_model.pkl", "fraud_model.pkl")

with open("fraud_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "Fraud Detection API running"}

@app.get("/predict")
def predict():
    sample = pd.DataFrame([[0]*30])
    prediction = model.predict(sample)
    return {"fraud_prediction": int(prediction[0])}
