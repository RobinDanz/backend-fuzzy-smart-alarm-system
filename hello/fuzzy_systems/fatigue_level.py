import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

last_night_sleep = ctrl.Antecedent(np.arange(0, 11, 0.5), 'last_night_sleep')
sleep_dept = ctrl.Antecedent(np.arange(0, 11, 1), 'sleep_dept')

fatigue_level_output = ctrl.Consequent(np.arange(0, 11, 1), 'fatigue_level_output')

last_night_sleep['low'] = fuzz.trimf(last_night_sleep.universe, [0, 0, 4])
last_night_sleep['average'] = fuzz.trimf(last_night_sleep.universe, [4, 5.5, 8])
last_night_sleep['high'] = fuzz.trimf(last_night_sleep.universe, [8, 10, 10])

sleep_dept['low'] = fuzz.trimf(sleep_dept.universe, [0, 0, 5])
sleep_dept['average'] = fuzz.trimf(sleep_dept.universe, [3, 5, 7])
sleep_dept['high'] = fuzz.trimf(sleep_dept.universe, [5, 10, 10])

fatigue_level_output['low'] = fuzz.trimf(fatigue_level_output.universe, [0, 1, 3])
fatigue_level_output['average'] = fuzz.trimf(fatigue_level_output.universe, [3, 5, 8])
fatigue_level_output['high'] = fuzz.trimf(fatigue_level_output.universe, [5, 8.5, 10])

rules = []

rules.append(ctrl.Rule(last_night_sleep['low'] & sleep_dept['low'], fatigue_level_output['average']))
rules.append(ctrl.Rule(last_night_sleep['low'] & sleep_dept['average'], fatigue_level_output['average']))
rules.append(ctrl.Rule(last_night_sleep['low'] & sleep_dept['high'], fatigue_level_output['high']))

rules.append(ctrl.Rule(last_night_sleep['average'] & sleep_dept['low'], fatigue_level_output['low']))
rules.append(ctrl.Rule(last_night_sleep['average'] & sleep_dept['average'], fatigue_level_output['average']))
rules.append(ctrl.Rule(last_night_sleep['average'] & sleep_dept['high'], fatigue_level_output['high']))

rules.append(ctrl.Rule(last_night_sleep['high'] & sleep_dept['low'], fatigue_level_output['low']))
rules.append(ctrl.Rule(last_night_sleep['high'] & sleep_dept['average'], fatigue_level_output['low']))
rules.append(ctrl.Rule(last_night_sleep['high'] & sleep_dept['high'], fatigue_level_output['average']))

fatigue_level_ctrl = ctrl.ControlSystem(rules=rules)
fatigue_level_sim = ctrl.ControlSystemSimulation(fatigue_level_ctrl)

def process_fatigue_level(data):
    print(data)
    fatigue_level_sim.input['last_night_sleep'] = data['last_night_sleep']
    fatigue_level_sim.input['sleep_dept'] = data['sleep_dept']

    fatigue_level_sim.compute()

    print(fatigue_level_sim)
    print(fatigue_level_sim.output['fatigue_level_output'])
