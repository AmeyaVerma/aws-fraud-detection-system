import boto3
import pandas as pd

s3 = boto3.client('s3')

bucket_name = "YOUR_BUCKET_NAME"
input_file = "creditcard.csv"
output_file = "cleaned_fraud_data.csv"

print("Downloading raw dataset...")
s3.download_file(bucket_name, input_file, "raw_data.csv")

df = pd.read_csv("raw_data.csv")

print("Cleaning data...")

df = df.drop_duplicates()
df = df.dropna()

df["risk_flag"] = df["Class"].apply(lambda x: "HIGH" if x == 1 else "LOW")

df.to_csv(output_file, index=False)

print("Uploading cleaned data...")
s3.upload_file(output_file, bucket_name, output_file)

print("ETL pipeline completed successfully.")
