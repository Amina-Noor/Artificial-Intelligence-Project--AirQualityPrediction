# agents/model_utils.py

import os
import joblib

def load_pm2_5_model():
    model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'final_pm2_5_model.pkl')
    model_path = os.path.abspath(model_path)  # makes absolute path
    model = joblib.load(model_path)
    return model, None  # replace None with scaler if you have it
