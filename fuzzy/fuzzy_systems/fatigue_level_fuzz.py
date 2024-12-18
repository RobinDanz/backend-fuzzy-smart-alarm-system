import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

last_night_sleep = ctrl.Antecedent(np.arange(0, 17, 1), 'last_night_sleep')
last_night_sleep_below_twelve = ctrl.Antecedent(np.arange(0, 19, 1), 'last_night_sleep_below_twelve')
sleep_debt = ctrl.Antecedent(np.arange(0, 31, 1), 'sleep_debt')

fatigue_level_output = ctrl.Consequent(np.arange(0, 11, 1), 'fatigue_level_output')

last_night_sleep['little'] = fuzz.trapmf(last_night_sleep.universe, [0, 0, 1, 4])
last_night_sleep['average'] = fuzz.trimf(last_night_sleep.universe, [3, 7, 9])
last_night_sleep['high'] = fuzz.trapmf(last_night_sleep.universe, [8, 12, 16, 16])

last_night_sleep_below_twelve['little'] = fuzz.trapmf(last_night_sleep_below_twelve.universe, [0, 0, 3, 6])
last_night_sleep_below_twelve['average'] = fuzz.trimf(last_night_sleep_below_twelve.universe, [5, 10, 12])
last_night_sleep_below_twelve['high'] = fuzz.trapmf(last_night_sleep_below_twelve.universe, [11, 15, 18, 18])

sleep_debt['low'] = fuzz.trapmf(sleep_debt.universe, [0, 0, 3, 7])
sleep_debt['average'] = fuzz.trimf(sleep_debt.universe, [3, 5, 7])
sleep_debt['high'] = fuzz.trapmf(sleep_debt.universe, [3, 15, 30, 30])

fatigue_level_output['low'] = fuzz.trimf(fatigue_level_output.universe, [0, 1, 3])
fatigue_level_output['average'] = fuzz.trimf(fatigue_level_output.universe, [2, 5, 8])
fatigue_level_output['high'] = fuzz.trimf(fatigue_level_output.universe, [5, 10, 10])

rules = []

rules.append(ctrl.Rule(last_night_sleep['little'] & sleep_debt['low'], fatigue_level_output['average']))
rules.append(ctrl.Rule(last_night_sleep['little'] & sleep_debt['average'], fatigue_level_output['average']))
rules.append(ctrl.Rule(last_night_sleep['little'] & sleep_debt['high'], fatigue_level_output['high']))

rules.append(ctrl.Rule(last_night_sleep['average'] & sleep_debt['low'], fatigue_level_output['low']))
rules.append(ctrl.Rule(last_night_sleep['average'] & sleep_debt['average'], fatigue_level_output['average']))
rules.append(ctrl.Rule(last_night_sleep['average'] & sleep_debt['high'], fatigue_level_output['high']))

rules.append(ctrl.Rule(last_night_sleep['high'] & sleep_debt['low'], fatigue_level_output['low']))
rules.append(ctrl.Rule(last_night_sleep['high'] & sleep_debt['average'], fatigue_level_output['low']))
rules.append(ctrl.Rule(last_night_sleep['high'] & sleep_debt['high'], fatigue_level_output['average']))

rules_below_twelve = []
rules_below_twelve.append(ctrl.Rule(last_night_sleep_below_twelve['little'] & sleep_debt['low'], fatigue_level_output['average']))
rules_below_twelve.append(ctrl.Rule(last_night_sleep_below_twelve['little'] & sleep_debt['average'], fatigue_level_output['average']))
rules_below_twelve.append(ctrl.Rule(last_night_sleep_below_twelve['little'] & sleep_debt['high'], fatigue_level_output['high']))

rules_below_twelve.append(ctrl.Rule(last_night_sleep_below_twelve['average'] & sleep_debt['low'], fatigue_level_output['low']))
rules_below_twelve.append(ctrl.Rule(last_night_sleep_below_twelve['average'] & sleep_debt['average'], fatigue_level_output['average']))
rules_below_twelve.append(ctrl.Rule(last_night_sleep_below_twelve['average'] & sleep_debt['high'], fatigue_level_output['high']))

rules_below_twelve.append(ctrl.Rule(last_night_sleep_below_twelve['high'] & sleep_debt['low'], fatigue_level_output['low']))
rules_below_twelve.append(ctrl.Rule(last_night_sleep_below_twelve['high'] & sleep_debt['average'], fatigue_level_output['low']))
rules_below_twelve.append(ctrl.Rule(last_night_sleep_below_twelve['high'] & sleep_debt['high'], fatigue_level_output['average']))

fatigue_level_ctrl = ctrl.ControlSystem(rules=rules)
fatigue_level_sim = ctrl.ControlSystemSimulation(fatigue_level_ctrl)

fatigue_level_below_twelve_ctrl = ctrl.ControlSystem(rules=rules_below_twelve)
fatigue_level_below_twelve_sim = ctrl.ControlSystemSimulation(fatigue_level_below_twelve_ctrl)



def process_fatigue_level(data, age):

    if age <= 12:
        fatigue_level_below_twelve_sim.input['last_night_sleep_below_twelve'] = data['last_night_sleep']
        fatigue_level_below_twelve_sim.input['sleep_debt'] = data['sleep_debt']
        fatigue_level_below_twelve_sim.compute()
        return fatigue_level_below_twelve_sim.output['fatigue_level_output']
    else:
        fatigue_level_sim.input['last_night_sleep'] = data['last_night_sleep']
        fatigue_level_sim.input['sleep_debt'] = data['sleep_debt']
        fatigue_level_sim.compute()
        return fatigue_level_sim.output['fatigue_level_output']
