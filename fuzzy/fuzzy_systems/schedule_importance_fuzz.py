import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables for schedule_importance
meeting_time = ctrl.Antecedent(np.arange(0, 480, 1), 'meeting_time')
urgent_tasks = ctrl.Antecedent(np.arange(0, 11, 1), 'urgent_tasks')

# Define fuzzy output variable for schedule_importance
schedule_importance_output = ctrl.Consequent(np.arange(0, 11, 1), 'wake_time_adjustment')

# Membership functions for meeting_time
meeting_time['none'] = fuzz.trapmf(meeting_time.universe, [0, 0, 30, 60])
meeting_time['moderate'] = fuzz.trimf(meeting_time.universe, [55, 120, 185])
meeting_time['busy'] = fuzz.trapmf(meeting_time.universe, [180, 300, 480, 480])

# Membership functions for urgent_tasks
urgent_tasks['low'] = fuzz.trimf(urgent_tasks.universe, [0, 0, 3])
urgent_tasks['some'] = fuzz.trimf(urgent_tasks.universe, [2, 4, 6])
urgent_tasks['a_lot'] = fuzz.trapmf(urgent_tasks.universe, [5, 8, 10, 10])

# Membership functions for wake_time_adjustment (output)
schedule_importance_output['low'] = fuzz.trimf(schedule_importance_output.universe, [0, 0, 2])
schedule_importance_output['average'] = fuzz.trimf(schedule_importance_output.universe, [3, 5, 8])
schedule_importance_output['high'] = fuzz.trimf(schedule_importance_output.universe, [7, 10, 10])

# Define rules for schedule_importance
rules = [
    ctrl.Rule(meeting_time['none'] & urgent_tasks['low'], schedule_importance_output['low']),
    ctrl.Rule(meeting_time['none'] & urgent_tasks['some'], schedule_importance_output['low']),
    ctrl.Rule(meeting_time['none'] & urgent_tasks['a_lot'], schedule_importance_output['average']),

    ctrl.Rule(meeting_time['moderate'] & urgent_tasks['low'], schedule_importance_output['average']),
    ctrl.Rule(meeting_time['moderate'] & urgent_tasks['some'], schedule_importance_output['average']),
    ctrl.Rule(meeting_time['moderate'] & urgent_tasks['a_lot'], schedule_importance_output['high']),


    ctrl.Rule(meeting_time['busy'] & urgent_tasks['low'], schedule_importance_output['average']),
    ctrl.Rule(meeting_time['busy'] & urgent_tasks['some'], schedule_importance_output['high']),
    ctrl.Rule(meeting_time['busy'] & urgent_tasks['a_lot'], schedule_importance_output['high']),
]

# Create control system and simulation for schedule_importance
schedule_importance_ctrl = ctrl.ControlSystem(rules=rules)
schedule_importance_sim = ctrl.ControlSystemSimulation(schedule_importance_ctrl)

def process_schedule_importance(data):
    schedule_importance_sim.input['meeting_time'] = data['meeting_time']
    schedule_importance_sim.input['urgent_tasks'] = data['urgent_tasks']

    schedule_importance_sim.compute()
    return schedule_importance_sim.output['wake_time_adjustment']


    
