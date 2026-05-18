class SeverityRuleEngine:
    def classify(self, pm10, pm25, wind_speed, humidity):
        """
        Classifies current/predicted air quality and environmental risk.
        Proactive trigger boundaries based on PM10 levels.
        """
        if pm10 < 50:
            level = "good"
            display_name = "Good"
            color = "Green"
        elif pm10 < 150:
            level = "moderate"
            display_name = "Moderate"
            color = "Yellow"
        elif pm10 < 250:
            level = "unhealthy"
            display_name = "Unhealthy"
            color = "Red"
        else:
            level = "hazardous"
            display_name = "Hazardous"
            color = "Crimson"
            
        return {
            'level': level,
            'display_name': display_name,
            'color': color
        }
