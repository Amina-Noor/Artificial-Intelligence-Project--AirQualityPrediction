# agents/data_utils.py
import numpy as np

EXPECTED_FEATURES = 13  # model was trained with this

def preprocess_data(new_data, scaler=None):
    X = np.array(new_data, dtype=float)

    # Pad with zeros if fewer features
    if X.size < EXPECTED_FEATURES:
        X = np.pad(X, (0, EXPECTED_FEATURES - X.size))

    # Trim if extra (safety)
    X = X[:EXPECTED_FEATURES]

    X = X.reshape(1, -1)

    if scaler is not None:
        return scaler.transform(X)

    return X
