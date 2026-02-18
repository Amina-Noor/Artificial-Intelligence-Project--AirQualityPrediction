
import numpy as np

class DataPreprocessingAgent:
    def __init__(self):
        pass

    def clean_input(self, data_dict):
        cleaned = {}
        for key, val in data_dict.items():
            if val is None or val < 0:
                cleaned[key] = 0
            else:
                cleaned[key] = val
        return cleaned

if __name__ == "__main__":
    agent = DataPreprocessingAgent()
    sample_data = {'temperature': 25, 'humidity': -5, 'no2': None}
    cleaned = agent.clean_input(sample_data)
    print("Cleaned data:", cleaned)
