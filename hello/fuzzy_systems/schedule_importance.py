import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables for schedule_importance
sleep_quality = ctrl.Antecedent(np.arange(0, 11, 1), 'sleep_quality')
mood = ctrl.Antecedent(np.arange(0, 11, 1), 'mood')
weather = ctrl.Antecedent(np.arange(0, 11, 1), 'weather')
schedule_importance = ctrl.Antecedent(np.arange(0, 11, 1), 'schedule_importance')

# Define fuzzy output variable for schedule_importance
wake_time_adjustment = ctrl.Consequent(np.arange(-30, 31, 1), 'wake_time_adjustment')

# Membership functions for input variables
sleep_quality['poor'] = fuzz.trimf(sleep_quality.universe, [0, 0, 5])
sleep_quality['average'] = fuzz.trimf(sleep_quality.universe, [3, 5, 7])
sleep_quality['good'] = fuzz.trimf(sleep_quality.universe, [5, 10, 10])

mood['stressed'] = fuzz.trimf(mood.universe, [0, 0, 5])
mood['neutral'] = fuzz.trimf(mood.universe, [3, 5, 7])
mood['relaxed'] = fuzz.trimf(mood.universe, [5, 10, 10])

weather['bad'] = fuzz.trimf(weather.universe, [0, 0, 5])
weather['average'] = fuzz.trimf(weather.universe, [3, 5, 7])
weather['good'] = fuzz.trimf(weather.universe, [5, 10, 10])

schedule_importance['low'] = fuzz.trimf(schedule_importance.universe, [0, 0, 5])
schedule_importance['medium'] = fuzz.trimf(schedule_importance.universe, [3, 5, 7])
schedule_importance['high'] = fuzz.trimf(schedule_importance.universe, [5, 10, 10])

# Membership functions for output variable
wake_time_adjustment['delay'] = fuzz.trimf(wake_time_adjustment.universe, [-30, -15, 0])
wake_time_adjustment['no_change'] = fuzz.trimf(wake_time_adjustment.universe, [-5, 0, 5])
wake_time_adjustment['advance'] = fuzz.trimf(wake_time_adjustment.universe, [0, 15, 30])

# Define rules for schedule_importance (5 rules)
rules_schedule_importance = [
    ctrl.Rule(schedule_importance['low'] & sleep_quality['poor'], wake_time_adjustment['delay']),
    ctrl.Rule(schedule_importance['low'] & mood['neutral'], wake_time_adjustment['no_change']),
    ctrl.Rule(schedule_importance['medium'] & weather['average'], wake_time_adjustment['no_change']),
    ctrl.Rule(schedule_importance['high'] & sleep_quality['good'], wake_time_adjustment['advance']),
    ctrl.Rule(schedule_importance['high'] & mood['relaxed'], wake_time_adjustment['advance'])
]

# Create control system and simulation for schedule_importance
wake_ctrl_schedule = ctrl.ControlSystem(rules_schedule_importance)
wake_sim_schedule = ctrl.ControlSystemSimulation(wake_ctrl_schedule)
