import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables for preferred_wake_method
sleep_quality = ctrl.Antecedent(np.arange(0, 11, 1), 'sleep_quality')
morning_energy = ctrl.Antecedent(np.arange(0, 11, 1), 'morning_energy')

# Define fuzzy output variable for preferred_wake_method
wake_time_adjustment = ctrl.Consequent(np.arange(-30, 31, 1), 'wake_time_adjustment')

# Membership functions for sleep_quality
sleep_quality['very_poor'] = fuzz.trimf(sleep_quality.universe, [0, 0, 3])
sleep_quality['average'] = fuzz.trimf(sleep_quality.universe, [2, 5, 7])
sleep_quality['excellent'] = fuzz.trimf(sleep_quality.universe, [6, 10, 10])

# Membership functions for morning_energy
morning_energy['very_low'] = fuzz.trimf(morning_energy.universe, [0, 0, 3])
morning_energy['moderate'] = fuzz.trimf(morning_energy.universe, [2, 5, 7])
morning_energy['very_high'] = fuzz.trimf(morning_energy.universe, [6, 10, 10])

# Membership functions for wake_time_adjustment (output)
wake_time_adjustment['delay'] = fuzz.trimf(wake_time_adjustment.universe, [-30, -15, 0])
wake_time_adjustment['no_change'] = fuzz.trimf(wake_time_adjustment.universe, [-5, 0, 5])
wake_time_adjustment['advance'] = fuzz.trimf(wake_time_adjustment.universe, [0, 15, 30])

# Define rules for preferred_wake_method
rules = [
    ctrl.Rule(sleep_quality['very_poor'] & morning_energy['very_low'], wake_time_adjustment['delay']),
    ctrl.Rule(sleep_quality['average'] & morning_energy['moderate'], wake_time_adjustment['no_change']),
    ctrl.Rule(sleep_quality['excellent'] & morning_energy['very_high'], wake_time_adjustment['advance']),
    ctrl.Rule(sleep_quality['very_poor'] & morning_energy['very_high'], wake_time_adjustment['no_change']),
    ctrl.Rule(sleep_quality['excellent'] & morning_energy['very_low'], wake_time_adjustment['advance'])
]

# Create control system and simulation for preferred_wake_method
preferred_wake_method_ctrl = ctrl.ControlSystem(rules)
preferred_wake_method_sim = ctrl.ControlSystemSimulation(preferred_wake_method_ctrl)

def process_wake_method(data):
    preferred_wake_method_sim.input['sleep_quality'] = data['sleep_quality']
    preferred_wake_method_sim.input['morning_energy'] = data['morning_energy']

    preferred_wake_method_sim.compute()
    print('Preferred wake method fuzzy')
    print(preferred_wake_method_sim.output['wake_time_adjustment'])
