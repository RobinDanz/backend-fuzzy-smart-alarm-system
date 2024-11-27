import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the fuzzy variables
wind_speed = ctrl.Antecedent(np.arange(0, 76, 1), 'wind_speed')  # in km/h
temperature = ctrl.Antecedent(np.arange(-15, 41, 1), 'temperature')  # in °C
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')  # in %

weather = ctrl.Consequent(np.arange(0, 101, 1), 'weather')  # Sleep quality scale (0-100)

# Define membership functions for Wind Speed
wind_speed['calm'] = fuzz.trimf(wind_speed.universe, [0, 0, 20])
wind_speed['breezy'] = fuzz.trimf(wind_speed.universe, [17, 30, 46])
wind_speed['windy'] = fuzz.trapmf(wind_speed.universe, [44, 60, 75, 75])

# Define membership functions for Temperature
temperature['cold'] = fuzz.trapmf(temperature.universe, [-15, -15, 0, 7])
temperature['moderate'] = fuzz.trimf(temperature.universe, [5, 20, 30])
temperature['warm'] = fuzz.trimf(temperature.universe, [25, 40, 40])

# Define membership functions for Humidity
humidity['dry'] = fuzz.trimf(humidity.universe, [0, 0, 31])
humidity['normal'] = fuzz.trimf(humidity.universe, [29, 40, 51])
humidity['humid'] = fuzz.trimf(humidity.universe, [49, 100, 100])

# Define membership functions for Weather
weather['bad'] = fuzz.trimf(weather.universe, [0, 0, 40])
weather['average'] = fuzz.trimf(weather.universe, [30, 50, 70])
weather['good'] = fuzz.trimf(weather.universe, [60, 100, 100])

# Define fuzzy rules
rules = [
    ctrl.Rule(wind_speed['calm'] & temperature['cold'] & humidity['dry'], weather['average']),
    ctrl.Rule(wind_speed['calm'] & temperature['cold'] & humidity['normal'], weather['good']),
    ctrl.Rule(wind_speed['calm'] & temperature['cold'] & humidity['humid'], weather['average']),
    ctrl.Rule(wind_speed['calm'] & temperature['moderate'] & humidity['dry'], weather['good']),
    ctrl.Rule(wind_speed['calm'] & temperature['moderate'] & humidity['normal'], weather['good']),
    ctrl.Rule(wind_speed['calm'] & temperature['moderate'] & humidity['humid'], weather['average']),
    ctrl.Rule(wind_speed['calm'] & temperature['warm'] & humidity['dry'], weather['good']),
    ctrl.Rule(wind_speed['calm'] & temperature['warm'] & humidity['normal'], weather['average']),
    ctrl.Rule(wind_speed['calm'] & temperature['warm'] & humidity['humid'], weather['bad']),
    ctrl.Rule(wind_speed['breezy'] & temperature['cold'] & humidity['dry'], weather['average']),
    ctrl.Rule(wind_speed['breezy'] & temperature['cold'] & humidity['normal'], weather['average']),
    ctrl.Rule(wind_speed['breezy'] & temperature['cold'] & humidity['humid'], weather['bad']),
    ctrl.Rule(wind_speed['breezy'] & temperature['moderate'] & humidity['dry'], weather['good']),
    ctrl.Rule(wind_speed['breezy'] & temperature['moderate'] & humidity['normal'], weather['good']),
    ctrl.Rule(wind_speed['breezy'] & temperature['moderate'] & humidity['humid'], weather['average']),
    ctrl.Rule(wind_speed['breezy'] & temperature['warm'] & humidity['dry'], weather['average']),
    ctrl.Rule(wind_speed['breezy'] & temperature['warm'] & humidity['normal'], weather['average']),
    ctrl.Rule(wind_speed['breezy'] & temperature['warm'] & humidity['humid'], weather['bad']),
    ctrl.Rule(wind_speed['windy'] & temperature['cold'] & humidity['dry'], weather['bad']),
    ctrl.Rule(wind_speed['windy'] & temperature['cold'] & humidity['normal'], weather['bad']),
    ctrl.Rule(wind_speed['windy'] & temperature['cold'] & humidity['humid'], weather['bad']),
    ctrl.Rule(wind_speed['windy'] & temperature['moderate'] & humidity['dry'], weather['average']),
    ctrl.Rule(wind_speed['windy'] & temperature['moderate'] & humidity['normal'], weather['average']),
    ctrl.Rule(wind_speed['windy'] & temperature['moderate'] & humidity['humid'], weather['bad']),
    ctrl.Rule(wind_speed['windy'] & temperature['warm'] & humidity['dry'], weather['bad']),
    ctrl.Rule(wind_speed['windy'] & temperature['warm'] & humidity['normal'], weather['bad']),
    ctrl.Rule(wind_speed['windy'] & temperature['warm'] & humidity['humid'], weather['bad']),
]

# Create control system
weather_ctrl = ctrl.ControlSystem(rules)
weather_sim = ctrl.ControlSystemSimulation(weather_ctrl)



# # Output result
# if 'weather' in weather_sim.output:
#     print(f"Weather Evaluation for Sleep: {weather_sim.output['weather']:.2f}")
# else:
#     print("Error: Weather output not computed.")


def process_weather(data):
    weather_sim.input['wind_speed'] = data['wind_speed']
    weather_sim.input['temperature'] = data['temperature']
    weather_sim.input['humidity'] = data['humidity']

    weather_sim.compute()

    return weather_sim.output['weather']
