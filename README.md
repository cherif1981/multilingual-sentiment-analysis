# Multilingual Sentiment Analysis (Arabic + English)

This project performs sentiment analysis on Arabic and English text using:
- TF-IDF + Logistic Regression
- Multilingual BERT & AraBERT

## Features
- Language detection
- Arabic normalization
- REST API for inference

## Run API
uvicorn src.inference.api:app --reload
