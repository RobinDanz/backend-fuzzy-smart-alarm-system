import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables for preferred_wake_method
sleep_quality = ctrl.Antecedent(np.arange(0, 11, 1), 'sleep_quality')
mood = ctrl.Antecedent(np.arange(0, 11, 1), 'mood')
weather = ctrl.Antecedent(np.arange(0, 11, 1), 'weather')
preferred_wake_method = ctrl.Antecedent(np.arange(0, 11, 1), 'preferred_wake_method')

# Define fuzzy output variable for preferred_wake_method
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

preferred_wake_method['gentle'] = fuzz.trimf(preferred_wake_method.universe, [0, 0, 5])
preferred_wake_method['moderate'] = fuzz.trimf(preferred_wake_method.universe, [3, 5, 7])
preferred_wake_method['dynamic'] = fuzz.trimf(preferred_wake_method.universe, [5, 10, 10])

# Membership functions for output variable
wake_time_adjustment['delay'] = fuzz.trimf(wake_time_adjustment.universe, [-30, -15, 0])
wake_time_adjustment['no_change'] = fuzz.trimf(wake_time_adjustment.universe, [-5, 0, 5])
wake_time_adjustment['advance'] = fuzz.trimf(wake_time_adjustment.universe, [0, 15, 30])

# Define rules for preferred_wake_method (5 rules)
rules_preferred_wake_method = [
    ctrl.Rule(preferred_wake_method['gentle'] & sleep_quality['good'], wake_time_adjustment['advance']),
    ctrl.Rule(preferred_wake_method['gentle'] & sleep_quality['poor'], wake_time_adjustment['no_change']),
    ctrl.Rule(preferred_wake_method['moderate'] & mood['neutral'], wake_time_adjustment['no_change']),
    ctrl.Rule(preferred_wake_method['dynamic'] & weather['good'], wake_time_adjustment['advance']),
    ctrl.Rule(preferred_wake_method['dynamic'] & mood['stressed'], wake_time_adjustment['delay'])
]

# Create control system and simulation for preferred_wake_method
wake_ctrl_preferred_wake = ctrl.ControlSystem(rules_preferred_wake_method)
wake_sim_preferred_wake = ctrl.ControlSystemSimulation(wake_ctrl_preferred_wake)
