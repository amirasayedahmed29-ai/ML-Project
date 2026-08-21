from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

app = FastAPI(title="House Price Prediction API")

try:
    model = joblib.load('house_price_model.pkl')
except Exception as e:
    model = None

class HouseFeatures(BaseModel):
    area_sqft: float
    bhk: int
    bathroom_clean: int
    floor_clean: int
    furnishing_code: int
    is_top_location: int

@app.get("/")
def home():
    return {"message": "House Price Prediction API is Running!"}

@app.post("/predict")
def predict_price(features: HouseFeatures):
    if model is None:
        raise HTTPException(status_code=500, detail="Model file not found or failed to load.")
    
    input_data = pd.DataFrame([features.dict()])
    
    log_prediction = model.predict(input_data)[0]
    predicted_price = float(np.expm1(log_prediction))
    
    return {
        "predicted_price": round(predicted_price, 2)
    }