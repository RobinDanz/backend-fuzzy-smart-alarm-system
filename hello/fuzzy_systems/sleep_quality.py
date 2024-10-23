import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

ambiant_noise = ctrl.Antecedent(np.arange(0, 11, 1), 'ambiant_noise')
bed_quality = ctrl.Antecedent(np.arange(0, 11, 1), 'bed_quality')
stress_level = ctrl.Antecedent(np.arange(0, 11, 1), 'stress_level')

sleep_quality_output = ctrl.Consequent(np.arange(0, 11, 1), 'sleep_quality_output')

ambiant_noise['low'] = fuzz.trimf(ambiant_noise.universe, [0, 0, 5])
ambiant_noise['average'] = fuzz.trimf(ambiant_noise.universe, [3, 5, 7])
ambiant_noise['high'] = fuzz.trimf(ambiant_noise.universe, [5, 10, 10])

bed_quality['poor'] = fuzz.trimf(bed_quality.universe, [0, 0, 5])
bed_quality['average'] = fuzz.trimf(bed_quality.universe, [3, 5, 7])
bed_quality['good'] = fuzz.trimf(bed_quality.universe, [5, 10, 10])

stress_level['low'] = fuzz.trimf(stress_level.universe, [0, 0, 5])
stress_level['average'] = fuzz.trimf(stress_level.universe, [3, 5, 7])
stress_level['high'] = fuzz.trimf(stress_level.universe, [5, 10, 10])

sleep_quality_output['poor'] = fuzz.trimf(sleep_quality_output.universe, [0, 2, 5])
sleep_quality_output['average'] = fuzz.trimf(sleep_quality_output.universe, [3, 5, 8])
sleep_quality_output['good'] = fuzz.trimf(sleep_quality_output.universe, [5, 8, 10])

rules = []

# Ambiant noise & bed_quality
rules.append(ctrl.Rule(ambiant_noise['low'] & bed_quality['poor'], sleep_quality_output['average']))
rules.append(ctrl.Rule(ambiant_noise['low'] & bed_quality['average'], sleep_quality_output['average']))
rules.append(ctrl.Rule(ambiant_noise['low'] & bed_quality['good'], sleep_quality_output['good']))

rules.append(ctrl.Rule(ambiant_noise['average'] & bed_quality['poor'], sleep_quality_output['poor']))
rules.append(ctrl.Rule(ambiant_noise['average'] & bed_quality['average'], sleep_quality_output['average']))
rules.append(ctrl.Rule(ambiant_noise['average'] & bed_quality['good'], sleep_quality_output['good']))

rules.append(ctrl.Rule(ambiant_noise['high'] & bed_quality['poor'], sleep_quality_output['poor']))
rules.append(ctrl.Rule(ambiant_noise['high'] & bed_quality['average'], sleep_quality_output['average']))
rules.append(ctrl.Rule(ambiant_noise['high'] & bed_quality['good'], sleep_quality_output['average']))

# Ambiant noise & stress level
rules.append(ctrl.Rule(ambiant_noise['low'] & stress_level['low'], sleep_quality_output['good']))
rules.append(ctrl.Rule(ambiant_noise['low'] & stress_level['average'], sleep_quality_output['good']))
rules.append(ctrl.Rule(ambiant_noise['low'] & stress_level['high'], sleep_quality_output['average']))

rules.append(ctrl.Rule(ambiant_noise['average'] & stress_level['low'], sleep_quality_output['good']))
rules.append(ctrl.Rule(ambiant_noise['average'] & stress_level['average'], sleep_quality_output['average']))
rules.append(ctrl.Rule(ambiant_noise['average'] & stress_level['high'], sleep_quality_output['average']))

rules.append(ctrl.Rule(ambiant_noise['high'] & stress_level['low'], sleep_quality_output['average']))
rules.append(ctrl.Rule(ambiant_noise['high'] & stress_level['average'], sleep_quality_output['average']))
rules.append(ctrl.Rule(ambiant_noise['high'] & stress_level['high'], sleep_quality_output['poor']))

# Bed Quality and stress level
rules.append(ctrl.Rule(bed_quality['poor'] & stress_level['low'], sleep_quality_output['average']))
rules.append(ctrl.Rule(bed_quality['poor'] & stress_level['average'], sleep_quality_output['average']))
rules.append(ctrl.Rule(bed_quality['poor'] & stress_level['high'], sleep_quality_output['poor']))

rules.append(ctrl.Rule(bed_quality['average'] & stress_level['low'], sleep_quality_output['average']))
rules.append(ctrl.Rule(bed_quality['average'] & stress_level['average'], sleep_quality_output['average']))
rules.append(ctrl.Rule(bed_quality['average'] & stress_level['high'], sleep_quality_output['good']))

rules.append(ctrl.Rule(bed_quality['good'] & stress_level['low'], sleep_quality_output['poor']))
rules.append(ctrl.Rule(bed_quality['good'] & stress_level['average'], sleep_quality_output['average']))
rules.append(ctrl.Rule(bed_quality['good'] & stress_level['high'], sleep_quality_output['average']))

sleep_quality_ctrl = ctrl.ControlSystem(rules=rules)
sleep_quality_sim = ctrl.ControlSystemSimulation(sleep_quality_ctrl)

def process_sleep_quality(data):
    sleep_quality_sim.input['ambiant_noise'] = data['ambiant_noise']
    sleep_quality_sim.input['bed_quality'] = data['bed_quality']
    sleep_quality_sim.input['stress_level'] = data['stress_level']

    sleep_quality_sim.compute()

    print(sleep_quality_sim.output['sleep_quality_output'])