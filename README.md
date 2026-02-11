# Cloud-Native Financial Fraud Detection System (AWS + ML)

## Overview
This project demonstrates an end-to-end cloud-based fraud detection system built using AWS and Machine Learning.

The system simulates how financial institutions deploy risk detection pipelines in production.

## Features
- Transaction data stored in AWS S3
- ETL pipeline for data cleaning and preprocessing
- Machine learning fraud detection model
- Model stored in AWS S3
- Deployed on AWS EC2
- FastAPI endpoint for real-time fraud prediction

## Architecture
User Request → FastAPI (EC2) → ML Model → Prediction  
Data Pipeline: Raw Data → S3 → ETL → Clean Data → Model Training → Deployment

## Tech Stack
- Python
- AWS S3
- AWS EC2
- FastAPI
- Scikit-learn
- Pandas

