class PredictionAgent:
    def __init__(self, model_path, scaler_path=None):
        import joblib
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path) if scaler_path else None

        # Define which features should be scaled
        self.scaled_features_indices = [0,1,2,3,4]  # CO, NO2, SO2, PM2_5_lag1, NO2_lag1

    def predict_pm25(self, features):
        import numpy as np
        features = np.array(features).reshape(1, -1)

        # Only scale first 5 features
        if self.scaler:
            features_scaled_part = self.scaler.transform(features[:, self.scaled_features_indices])
            features[:, self.scaled_features_indices] = features_scaled_part

        prediction = self.model.predict(features)[0]
        return float(prediction)
