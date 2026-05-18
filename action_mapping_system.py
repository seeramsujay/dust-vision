class ActionDispatcher:
    def __init__(self):
        pass

    def dispatch(self, severity_level, context):
        """
        Dispatches mitigation recommendations and contractor alerts
        based on active severity level and location context.
        """
        actions = []
        
        if severity_level == 'unhealthy':
            actions.append({
                'action_type': 'sprinkler',
                'message': f"Activating smart water mist sprinklers at {context.get('location', 'Site')}.",
                'details': {
                    'intensity': 60,
                    'duration': 180
                }
            })
            actions.append({
                'action_type': 'alert',
                'message': f"Warning dispatched to contractor: PM10 predicted to reach {context.get('predicted_pm10', 0.0):.1f} µg/m³."
            })
        elif severity_level == 'hazardous':
            actions.append({
                'action_type': 'sprinkler',
                'message': f"Deploying critical water suppression mist at {context.get('location', 'Site')}.",
                'details': {
                    'intensity': 100,
                    'duration': 300
                }
            })
            actions.append({
                'action_type': 'compliance',
                'message': "CRITICAL RULE BREACH: Contractor notified to halt all earthmoving activities immediately."
            })
            
        return {
            'success': len(actions) > 0,
            'actions_executed': actions
        }
