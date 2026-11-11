import pytest
from aq_severity_engine import SeverityRuleEngine
from action_mapping_system import ActionDispatcher

def test_severity_rule_engine():
    engine = SeverityRuleEngine()
    
    good = engine.classify(30, 15, 5, 50)
    assert good['level'] == 'good'
    assert good['color'] == 'Green'

    mod = engine.classify(100, 45, 5, 50)
    assert mod['level'] == 'moderate'
    assert mod['color'] == 'Yellow'

    unhealthy = engine.classify(200, 90, 5, 50)
    assert unhealthy['level'] == 'unhealthy'
    assert unhealthy['color'] == 'Red'

    hazardous = engine.classify(300, 150, 5, 50)
    assert hazardous['level'] == 'hazardous'
    assert hazardous['color'] == 'Crimson'

def test_action_dispatcher():
    dispatcher = ActionDispatcher()
    
    ctx = {'location': 'Zone A', 'predicted_pm10': 210.5}
    res = dispatcher.dispatch('unhealthy', ctx)
    assert res['success'] is True
    assert len(res['actions_executed']) == 2
    assert res['actions_executed'][0]['action_type'] == 'sprinkler'
    assert res['actions_executed'][1]['action_type'] == 'alert'

    res_haz = dispatcher.dispatch('hazardous', ctx)
    assert res_haz['success'] is True
    assert len(res_haz['actions_executed']) == 2
    assert res_haz['actions_executed'][0]['action_type'] == 'sprinkler'
