# Printer Predictive Maintenance

## Overview
Predict printer failures using XGBoost and deploy via FastAPI.

## Features
- MLflow experiment tracking
- FastAPI real-time inference
- Docker deployment

## Run Training
python src/pipelines/training_pipeline.py

## Run API
uvicorn src.serving.app:app --reload
