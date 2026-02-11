import boto3
import pandas as pd

# -------------------------------
# STEP 1: Connect to AWS S3
# -------------------------------
s3 = boto3.client('s3')

bucket_name = "barclays-ml-project-ameya"  
input_file = "creditcard.csv"
output_file = "cleaned_fraud_data.csv"

# -------------------------------
# STEP 2: Download raw dataset
# -------------------------------
print("Downloading raw dataset from S3...")

s3.download_file(bucket_name, input_file, "raw_data.csv")

print("Download complete.")

# -------------------------------
# STEP 3: Read dataset
# -------------------------------
df = pd.read_csv("raw_data.csv")

print("Dataset loaded.")
print("Original shape:", df.shape)

# -------------------------------
# STEP 4: Basic cleaning
# -------------------------------

# remove duplicate rows
df = df.drop_duplicates()

# remove null values if any
df = df.dropna()

# create risk column (example logic)
df["risk_flag"] = df["Class"].apply(lambda x: "HIGH" if x == 1 else "LOW")

print("Data cleaned.")
print("New shape:", df.shape)

# -------------------------------
# STEP 5: Save cleaned file
# -------------------------------
df.to_csv(output_file, index=False)

print("Cleaned file saved locally.")

# -------------------------------
# STEP 6: Upload cleaned file back to S3
# -------------------------------
print("Uploading cleaned file to S3...")

s3.upload_file(output_file, bucket_name, output_file)

print("Upload successful.")
print("ETL pipeline completed successfully.")
