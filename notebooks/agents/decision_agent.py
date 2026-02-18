class DecisionAgent:
    def classify_aqi(self, pm2_5):
        if pm2_5 <= 12:
            return "Good"
        elif pm2_5 <= 35.4:
            return "Moderate"
        elif pm2_5 <= 55.4:
            return "Unhealthy for Sensitive Groups"
        elif pm2_5 <= 150.4:
            return "Unhealthy"
        else:
            return "Very Unhealthy"

    def get_recommendation(self, aqi_status):
        recommendations = {
            "Good": "Air quality is satisfactory. Enjoy outdoor activities 🌿",
            "Moderate": "Air quality is acceptable. Sensitive individuals should take care 🙂",
            "Unhealthy for Sensitive Groups": "Sensitive groups should limit prolonged outdoor exertion 😷",
            "Unhealthy": "Avoid outdoor activities and wear a mask if necessary 🚫",
            "Very Unhealthy": "Health alert! Stay indoors and use air purifiers 🚨"
        }
        return recommendations.get(aqi_status, "No recommendation available.")
