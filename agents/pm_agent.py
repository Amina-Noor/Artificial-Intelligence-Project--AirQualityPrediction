# Make sure you opened Jupyter inside:
# C:\Users\Lenovo\Desktop\Air_Quality_Prediction

from agents.data_utils import preprocess_data
from agents.model_utils import load_pm10_model

# Load trained model
model_pm10, scaler = load_pm10_model()

# Example input (same as your agent)
# CO, NO2, SO2, Temperature, Humidity
new_data = [0.8, 45, 20, 25, 60]

# Preprocess input
X_new = preprocess_data(new_data, scaler)

# Predict PM10
pm10_pred = model_pm10.predict(X_new)[0]

# Output
print("PM10 Prediction:", pm10_pred)

if pm10_pred > 100:
    print("⚠️ PM10 Alert! Unsafe air quality")
else:
    print("✅ PM10 level is safe")