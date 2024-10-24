import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables for schedule_importance
meeting_time = ctrl.Antecedent(np.arange(0, 11, 1), 'meeting_time')
urgent_tasks = ctrl.Antecedent(np.arange(0, 11, 1), 'urgent_tasks')

# Define fuzzy output variable for schedule_importance
wake_time_adjustment = ctrl.Consequent(np.arange(-30, 31, 1), 'wake_time_adjustment')

# Membership functions for meeting_time
meeting_time['none'] = fuzz.trimf(meeting_time.universe, [0, 0, 3])
meeting_time['moderate'] = fuzz.trimf(meeting_time.universe, [2, 5, 7])
meeting_time['very_busy'] = fuzz.trimf(meeting_time.universe, [6, 10, 10])

# Membership functions for urgent_tasks
urgent_tasks['empty'] = fuzz.trimf(urgent_tasks.universe, [0, 0, 3])
urgent_tasks['active'] = fuzz.trimf(urgent_tasks.universe, [2, 5, 7])
urgent_tasks['urgent'] = fuzz.trimf(urgent_tasks.universe, [6, 10, 10])

# Membership functions for wake_time_adjustment (output)
wake_time_adjustment['delay'] = fuzz.trimf(wake_time_adjustment.universe, [-30, -15, 0])
wake_time_adjustment['no_change'] = fuzz.trimf(wake_time_adjustment.universe, [-5, 0, 5])
wake_time_adjustment['advance'] = fuzz.trimf(wake_time_adjustment.universe, [0, 15, 30])

# Define rules for schedule_importance
rules_schedule_importance = [
    ctrl.Rule(meeting_time['none'] & urgent_tasks['empty'], wake_time_adjustment['delay']),
    ctrl.Rule(meeting_time['moderate'] & urgent_tasks['active'], wake_time_adjustment['no_change']),
    ctrl.Rule(meeting_time['very_busy'] & urgent_tasks['urgent'], wake_time_adjustment['advance']),
    ctrl.Rule(meeting_time['none'] & urgent_tasks['urgent'], wake_time_adjustment['no_change']),
    ctrl.Rule(meeting_time['very_busy'] & urgent_tasks['empty'], wake_time_adjustment['advance'])
]

# Create control system and simulation for schedule_importance
wake_ctrl_schedule = ctrl.ControlSystem(rules_schedule_importance)
wake_sim_schedule = ctrl.ControlSystemSimulation(wake_ctrl_schedule)
