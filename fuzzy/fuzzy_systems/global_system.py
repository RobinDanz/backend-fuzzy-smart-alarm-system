import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

from fuzzy.fuzzy_systems import fatigue_level_fuzz, schedule_importance_fuzz, global_system, sleep_quality_fuzz, weather_fuzz

# Define fuzzy variables (Antecedents)
sleep_quality = ctrl.Antecedent(np.arange(0, 11, 1), 'sleep_quality')
schedule_importance = ctrl.Antecedent(np.arange(0, 11, 1), 'schedule_importance')
physical_well_being = ctrl.Antecedent(np.arange(0, 11, 1), 'physical_well_being')
weather = ctrl.Antecedent(np.arange(0, 11, 1), 'weather')
fatigue_level = ctrl.Antecedent(np.arange(0, 11, 1), 'fatigue_level')

# Define fuzzy output variable (Consequent)
wake_time_adjustment = ctrl.Consequent(np.arange(-60, 60, 15), 'wake_time_adjustment')

# Membership functions for input variables

# Sleep quality
sleep_quality['poor'] = fuzz.trimf(sleep_quality.universe, [0, 0, 5])
sleep_quality['average'] = fuzz.trimf(sleep_quality.universe, [3, 5, 7])
sleep_quality['good'] = fuzz.trimf(sleep_quality.universe, [5, 10, 10])

# Schedule importance
schedule_importance['low'] = fuzz.trimf(schedule_importance.universe, [0, 0, 5])
schedule_importance['medium'] = fuzz.trimf(schedule_importance.universe, [3, 5, 7])
schedule_importance['high'] = fuzz.trimf(schedule_importance.universe, [5, 10, 10])

# Physical well being
physical_well_being['sick'] = fuzz.trimf(physical_well_being.universe, [0, 0, 5])
physical_well_being['neutral'] = fuzz.trimf(physical_well_being.universe, [3, 5, 7])
physical_well_being['healthy'] = fuzz.trimf(physical_well_being.universe, [5, 10, 10])

# Weather
weather['bad'] = fuzz.trimf(weather.universe, [0, 0, 5])
weather['average'] = fuzz.trimf(weather.universe, [3, 5, 7])
weather['good'] = fuzz.trimf(weather.universe, [5, 10, 10])

# Fatigue level
fatigue_level['low'] = fuzz.trimf(fatigue_level.universe, [0, 0, 5])
fatigue_level['average'] = fuzz.trimf(fatigue_level.universe, [3, 5, 7])
fatigue_level['high'] = fuzz.trimf(fatigue_level.universe, [5, 10, 10])

# Membership functions for output variable

# Wake time adjustment
wake_time_adjustment['delay'] = fuzz.trimf(wake_time_adjustment.universe, [-60, -60, 0])
wake_time_adjustment['no_change'] = fuzz.trimf(wake_time_adjustment.universe, [-15, 0, 15])
wake_time_adjustment['advance'] = fuzz.trimf(wake_time_adjustment.universe, [0, 60, 60])

# Define the rules for wake time adjustment based on different inputs

rules = []

# Sleep quality & schedule importance
# rules.append(ctrl.Rule(sleep_quality['poor'] & schedule_importance['high'], wake_time_adjustment['no_change']))
# rules.append(ctrl.Rule(sleep_quality['poor'] & schedule_importance['medium'], wake_time_adjustment['advance']))
# rules.append(ctrl.Rule(sleep_quality['poor'] & schedule_importance['low'], wake_time_adjustment['advance']))

# rules.append(ctrl.Rule(sleep_quality['average'] & schedule_importance['high'], wake_time_adjustment['no_change']))
# rules.append(ctrl.Rule(sleep_quality['average'] & schedule_importance['medium'], wake_time_adjustment['no_change']))
# rules.append(ctrl.Rule(sleep_quality['average'] & schedule_importance['low'], wake_time_adjustment['advance']))

# rules.append(ctrl.Rule(sleep_quality['good'] & schedule_importance['high'], wake_time_adjustment['delay']))
# rules.append(ctrl.Rule(sleep_quality['good'] & schedule_importance['medium'], wake_time_adjustment['no_change']))
# rules.append(ctrl.Rule(sleep_quality['good'] & schedule_importance['low'], wake_time_adjustment['no_change']))

# # physical_well_being and schedule importance
# rules.append(ctrl.Rule(physical_well_being['sick'] & schedule_importance['high'], wake_time_adjustment['no_change']))
# rules.append(ctrl.Rule(physical_well_being['sick'] & schedule_importance['medium'], wake_time_adjustment['advance']))
# rules.append(ctrl.Rule(physical_well_being['healthy'] & sleep_quality['good'], wake_time_adjustment['delay']))
# rules.append(ctrl.Rule(physical_well_being['healthy'] & sleep_quality['poor'], wake_time_adjustment['advance']))
# rules.append(ctrl.Rule(physical_well_being['neutral'] & sleep_quality['average'], wake_time_adjustment['no_change']))

# # Weather and physical_well_being/sleep quality
# rules.append(ctrl.Rule(weather['bad'] & schedule_importance['high'], wake_time_adjustment['no_change']))
# rules.append(ctrl.Rule(weather['good'] & physical_well_being['healthy'], wake_time_adjustment['delay']))
# rules.append(ctrl.Rule(weather['average'] & physical_well_being['sick'], wake_time_adjustment['advance']))
# rules.append(ctrl.Rule(weather['good'] & sleep_quality['good'], wake_time_adjustment['delay']))

# # Fallback or catch-all rules
# rules.append(ctrl.Rule(sleep_quality['poor'] | physical_well_being['neutral'], wake_time_adjustment['advance']))
# rules.append(ctrl.Rule(schedule_importance['low'] & physical_well_being['healthy'], wake_time_adjustment['advance']))

# # Optional default rule
# rules.append(ctrl.Rule(sleep_quality['poor'] | schedule_importance['low'] | physical_well_being['healthy'], wake_time_adjustment['no_change']))

# # Add fatigue level rules
# rules.append(ctrl.Rule(fatigue_level['low'] & schedule_importance['low'], wake_time_adjustment['no_change']))
# rules.append(ctrl.Rule(fatigue_level['low'] & schedule_importance['medium'], wake_time_adjustment['no_change']))
# rules.append(ctrl.Rule(fatigue_level['low'] & schedule_importance['high'], wake_time_adjustment['delay']))

# rules.append(ctrl.Rule(fatigue_level['average'] & schedule_importance['low'], wake_time_adjustment['advance']))
# rules.append(ctrl.Rule(fatigue_level['average'] & schedule_importance['medium'], wake_time_adjustment['no_change']))
# rules.append(ctrl.Rule(fatigue_level['average'] & schedule_importance['high'], wake_time_adjustment['no_change']))

# rules.append(ctrl.Rule(fatigue_level['high'] & schedule_importance['low'], wake_time_adjustment['advance']))
# rules.append(ctrl.Rule(fatigue_level['high'] & schedule_importance['medium'], wake_time_adjustment['advance']))
# rules.append(ctrl.Rule(fatigue_level['high'] & schedule_importance['high'], wake_time_adjustment['no_change']))

# rules.append(ctrl.Rule(fatigue_level['low'] & sleep_quality['poor'], wake_time_adjustment['no_change']))
# rules.append(ctrl.Rule(fatigue_level['low'] & sleep_quality['average'], wake_time_adjustment['no_change']))
# rules.append(ctrl.Rule(fatigue_level['low'] & sleep_quality['good'], wake_time_adjustment['delay']))

# rules.append(ctrl.Rule(fatigue_level['average'] & sleep_quality['poor'], wake_time_adjustment['advance']))
# rules.append(ctrl.Rule(fatigue_level['average'] & sleep_quality['average'], wake_time_adjustment['no_change']))
# rules.append(ctrl.Rule(fatigue_level['average'] & sleep_quality['good'], wake_time_adjustment['no_change']))

# rules.append(ctrl.Rule(fatigue_level['high'] & sleep_quality['poor'], wake_time_adjustment['advance']))
# rules.append(ctrl.Rule(fatigue_level['high'] & sleep_quality['average'], wake_time_adjustment['advance']))
# rules.append(ctrl.Rule(fatigue_level['high'] & sleep_quality['good'], wake_time_adjustment['advance']))

# ======================================

rules.append(ctrl.Rule(sleep_quality['poor'] & schedule_importance['low'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(sleep_quality['poor'] & schedule_importance['medium'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(sleep_quality['poor'] & schedule_importance['high'], wake_time_adjustment['no_change']))

rules.append(ctrl.Rule(sleep_quality['average'] & schedule_importance['low'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(sleep_quality['average'] & schedule_importance['medium'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(sleep_quality['average'] & schedule_importance['high'], wake_time_adjustment['delay']))

rules.append(ctrl.Rule(sleep_quality['good'] & schedule_importance['low'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(sleep_quality['good'] & schedule_importance['medium'], wake_time_adjustment['delay']))
rules.append(ctrl.Rule(sleep_quality['good'] & schedule_importance['high'], wake_time_adjustment['delay']))

rules.append(ctrl.Rule(sleep_quality['poor'] & physical_well_being['sick'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(sleep_quality['poor'] & physical_well_being['neutral'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(sleep_quality['poor'] & physical_well_being['healthy'], wake_time_adjustment['no_change']))

rules.append(ctrl.Rule(sleep_quality['average'] & physical_well_being['sick'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(sleep_quality['average'] & physical_well_being['neutral'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(sleep_quality['average'] & physical_well_being['healthy'], wake_time_adjustment['delay']))

rules.append(ctrl.Rule(sleep_quality['good'] & physical_well_being['sick'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(sleep_quality['good'] & physical_well_being['neutral'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(sleep_quality['good'] & physical_well_being['healthy'], wake_time_adjustment['no_change']))

rules.append(ctrl.Rule(sleep_quality['poor'] & weather['bad'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(sleep_quality['poor'] & weather['average'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(sleep_quality['poor'] & weather['good'], wake_time_adjustment['advance']))

rules.append(ctrl.Rule(sleep_quality['average'] & weather['bad'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(sleep_quality['average'] & weather['average'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(sleep_quality['average'] & weather['good'], wake_time_adjustment['no_change']))

rules.append(ctrl.Rule(sleep_quality['good'] & weather['bad'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(sleep_quality['good'] & weather['average'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(sleep_quality['good'] & weather['good'], wake_time_adjustment['delay']))

rules.append(ctrl.Rule(schedule_importance['low'] & physical_well_being['sick'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(schedule_importance['low'] & physical_well_being['neutral'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(schedule_importance['low'] & physical_well_being['healthy'], wake_time_adjustment['no_change']))

rules.append(ctrl.Rule(schedule_importance['medium'] & physical_well_being['sick'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(schedule_importance['medium'] & physical_well_being['neutral'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(schedule_importance['medium'] & physical_well_being['healthy'], wake_time_adjustment['no_change']))

rules.append(ctrl.Rule(schedule_importance['high'] & physical_well_being['sick'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(schedule_importance['high'] & physical_well_being['neutral'], wake_time_adjustment['delay']))
rules.append(ctrl.Rule(schedule_importance['high'] & physical_well_being['healthy'], wake_time_adjustment['delay']))

rules.append(ctrl.Rule(schedule_importance['low'] & weather['bad'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(schedule_importance['low'] & weather['average'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(schedule_importance['low'] & weather['good'], wake_time_adjustment['no_change']))

rules.append(ctrl.Rule(schedule_importance['medium'] & weather['bad'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(schedule_importance['medium'] & weather['average'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(schedule_importance['medium'] & weather['good'], wake_time_adjustment['delay']))

rules.append(ctrl.Rule(schedule_importance['high'] & weather['bad'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(schedule_importance['high'] & weather['average'], wake_time_adjustment['delay']))
rules.append(ctrl.Rule(schedule_importance['high'] & weather['good'], wake_time_adjustment['delay']))

rules.append(ctrl.Rule(physical_well_being['sick'] & weather['bad'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(physical_well_being['sick'] & weather['average'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(physical_well_being['sick'] & weather['good'], wake_time_adjustment['no_change']))

rules.append(ctrl.Rule(physical_well_being['neutral'] & weather['bad'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(physical_well_being['neutral'] & weather['average'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(physical_well_being['neutral'] & weather['good'], wake_time_adjustment['delay']))

rules.append(ctrl.Rule(physical_well_being['healthy'] & weather['bad'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(physical_well_being['healthy'] & weather['average'], wake_time_adjustment['delay']))
rules.append(ctrl.Rule(physical_well_being['healthy'] & weather['good'], wake_time_adjustment['delay']))

rules.append(ctrl.Rule(fatigue_level['low'] & sleep_quality['poor'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(fatigue_level['low'] & sleep_quality['average'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(fatigue_level['low'] & sleep_quality['good'], wake_time_adjustment['delay']))

rules.append(ctrl.Rule(fatigue_level['average'] & sleep_quality['poor'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(fatigue_level['average'] & sleep_quality['average'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(fatigue_level['average'] & sleep_quality['good'], wake_time_adjustment['delay']))

rules.append(ctrl.Rule(fatigue_level['high'] & sleep_quality['poor'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(fatigue_level['high'] & sleep_quality['average'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(fatigue_level['high'] & sleep_quality['good'], wake_time_adjustment['no_change']))

rules.append(ctrl.Rule(fatigue_level['low'] & schedule_importance['low'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(fatigue_level['low'] & schedule_importance['medium'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(fatigue_level['low'] & schedule_importance['high'], wake_time_adjustment['delay']))

rules.append(ctrl.Rule(fatigue_level['average'] & schedule_importance['low'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(fatigue_level['average'] & schedule_importance['medium'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(fatigue_level['average'] & schedule_importance['high'], wake_time_adjustment['delay']))

rules.append(ctrl.Rule(fatigue_level['high'] & schedule_importance['low'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(fatigue_level['high'] & schedule_importance['medium'], wake_time_adjustment['delay']))
rules.append(ctrl.Rule(fatigue_level['high'] & schedule_importance['high'], wake_time_adjustment['delay']))

rules.append(ctrl.Rule(fatigue_level['low'] & physical_well_being['sick'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(fatigue_level['low'] & physical_well_being['neutral'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(fatigue_level['low'] & physical_well_being['healthy'], wake_time_adjustment['advance']))

rules.append(ctrl.Rule(fatigue_level['average'] & physical_well_being['sick'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(fatigue_level['average'] & physical_well_being['neutral'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(fatigue_level['average'] & physical_well_being['healthy'], wake_time_adjustment['no_change']))

rules.append(ctrl.Rule(fatigue_level['high'] & physical_well_being['sick'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(fatigue_level['high'] & physical_well_being['neutral'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(fatigue_level['high'] & physical_well_being['healthy'], wake_time_adjustment['no_change']))

rules.append(ctrl.Rule(fatigue_level['low'] & weather['bad'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(fatigue_level['low'] & weather['average'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(fatigue_level['low'] & weather['good'], wake_time_adjustment['no_change']))

rules.append(ctrl.Rule(fatigue_level['average'] & weather['bad'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(fatigue_level['average'] & weather['average'], wake_time_adjustment['no_change']))
rules.append(ctrl.Rule(fatigue_level['average'] & weather['good'], wake_time_adjustment['delay']))

rules.append(ctrl.Rule(fatigue_level['high'] & weather['bad'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(fatigue_level['high'] & weather['average'], wake_time_adjustment['advance']))
rules.append(ctrl.Rule(fatigue_level['high'] & weather['good'], wake_time_adjustment['no_change']))



# Create a control system and simulation
alarm_ctrl = ctrl.ControlSystem(rules=rules)
alarm_sim = ctrl.ControlSystemSimulation(alarm_ctrl)

def set_alarm_settings(data):
    alarm_sim.input['sleep_quality'] = data['sleep_quality']
    alarm_sim.input['schedule_importance'] = data['schedule_importance']
    alarm_sim.input['physical_well_being'] = data['physical_well_being'] 
    alarm_sim.input['weather'] = data['weather'] 
    alarm_sim.input['fatigue_level'] = data['fatigue_level']
    
    alarm_sim.compute()
    ret  = alarm_sim.output['wake_time_adjustment']
    return ret