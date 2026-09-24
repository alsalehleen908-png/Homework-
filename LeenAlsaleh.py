# =================================================================or similar
# FTL SYRIA - PYTHON INDIVIDUAL PRACTICAL ASSIGNMENT
# Submission Deadline: Friday, 25 September 2026
# =================================================================

# -----------------------------------------------------------------
# Exercise 1 - Python Data Structures and Loops
# -----------------------------------------------------------------

# 1. Create climate information for at least 5 cities using a list of dictionaries
# 2. Include one city with a missing temperature value (None)
cities_climate = [
    {"city": "Damascus", "temperature": 38.0, "humidity": 30, "rainfall": 2.0},
    {"city": "Aleppo", "temperature": 41.5, "humidity": 20, "rainfall": 0.0},
    {"city": "Latakia", "temperature": 29.0, "humidity": 65, "rainfall": 10.0},
    {"city": "Homs", "temperature": None, "humidity": 35, "rainfall": 0.0},  # missing temp
    {"city": "Sweida", "temperature": 31.0, "humidity": 40, "rainfall": 14.0},
]

valid_temperatures = []
classifications_count = {
    "Extreme Heat": 0,
    "High Heat": 0,
    "Moderate Heat": 0,
    "Normal": 0,
}

print("=== Exercise 1: City Information & Classifications ===")
for c in cities_climate:
    # 3. Use continue to skip the city with missing temperature data
    if c["temperature"] is None:
        continue
    
    temp = c["temperature"]
    valid_temperatures.append(temp)
    
    # 1. Loop through all valid cities and display their information
    print(f"City: {c['city']} | Temp: {temp}°C | Humidity: {c['humidity']}% | Rainfall: {c['rainfall']} mm")
    
    # 4. Classify temperatures
    if temp >= 40.0:
        cat = "Extreme Heat"
    elif temp >= 35.0:
        cat = "High Heat"
    elif temp >= 30.0:
        cat = "Moderate Heat"
    else:
        cat = "Normal"
    
    classifications_count[cat] += 1

# 5. Calculate statistics
num_valid = len(valid_temperatures)
avg_temp = round(sum(valid_temperatures) / num_valid, 2) if num_valid > 0 else 0
max_temp = max(valid_temperatures) if num_valid > 0 else 0
min_temp = min(valid_temperatures) if num_valid > 0 else 0

# 6. Store the final classification results in a dictionary
exercise1_results = {
    "valid_observations": num_valid,
    "average_temperature": avg_temp,
    "highest_temperature": max_temp,
    "lowest_temperature": min_temp,
    "classifications_breakdown": classifications_count
}

print("\nExercise 1 Summary Results:")
print(exercise1_results)
print("-" * 50)


# -----------------------------------------------------------------
# Exercise 2 - Functions and Climate Risk
# -----------------------------------------------------------------

def calculate_risk(temperature, rainfall):
    """Returns risk level based on temperature and rainfall rules."""
    if temperature >= 40.0:
        return "EXTREME"
    elif temperature >= 35.0 or rainfall < 5.0:
        return "HIGH"
    elif temperature >= 30.0 or rainfall < 15.0:
        return "MODERATE"
    else:
        return "LOW"

def get_temp_stats(valid_temps):
    """Returns a tuple containing: (average, minimum, maximum)."""
    if not valid_temps:
        return (0.0, 0.0, 0.0)
    avg = sum(valid_temps) / len(valid_temps)
    return (round(avg, 2), min(valid_temps), max(valid_temps))

print("=== Exercise 2: Risk Assessment & Sorting ===")

# Enrich valid cities with risk
valid_cities = [c for c in cities_climate if c["temperature"] is not None]
for c in valid_cities:
    c["risk"] = calculate_risk(c["temperature"], c["rainfall"])

# 2. Display the city, temperature and calculated risk
print("All Valid Cities Risk:")
for c in valid_cities:
    print(f"City: {c['city']}, Temp: {c['temperature']}°C, Risk: {c['risk']}")

# 3. Tuple stats function test
valid_temps_list = [c["temperature"] for c in valid_cities]
stats_tuple = get_temp_stats(valid_temps_list)
print(f"\nStats Tuple (Avg, Min, Max): {stats_tuple}")# 4. Display only cities classified as HIGH or EXTREME
print("\nCities classified as HIGH or EXTREME:")
high_extreme_cities = [c for c in valid_cities if c["risk"] in ["HIGH", "EXTREME"]]
for c in high_extreme_cities:
    print(f"- {c['city']} ({c['risk']}, {c['temperature']}°C)")

# 5. Sort the cities from the highest to the lowest temperature using sorted() and lambda
sorted_cities = sorted(valid_cities, key=lambda x: x["temperature"], reverse=True)
print("\nSorted Cities (Highest to Lowest Temp):")
for c in sorted_cities:
    print(f"{c['city']}: {c['temperature']}°C")

print("-" * 50)


# -----------------------------------------------------------------
# Exercise 3 - OOP Climate Monitoring System
# -----------------------------------------------------------------

class ClimateStation:
    def init(self, city, temperature, humidity, rainfall):
        self.city = city
        self.temperature = temperature
        self.humidity = humidity
        self.rainfall = rainfall

    def display_summary(self):
        print(f"[Station] {self.city} | Temp: {self.temperature}°C | Humidity: {self.humidity}% | Rainfall: {self.rainfall} mm")

    def calculate_risk(self):
        if self.temperature is None:
            return "UNKNOWN"
        if self.temperature >= 40.0:
            return "EXTREME"
        elif self.temperature >= 35.0 or self.rainfall < 5.0:
            return "HIGH"
        elif self.temperature >= 30.0 or self.rainfall < 15.0:
            return "MODERATE"
        else:
            return "LOW"

    def update_temperature(self, new_temperature):
        self.temperature = new_temperature


class SmartClimateStation(ClimateStation):
    def init(self, city, temperature, humidity, rainfall, sensor_status="OK"):
        super().init(city, temperature, humidity, rainfall)
        self.sensor_status = sensor_status

    def check_sensor(self):
        return f"Sensor status for {self.city}: {self.sensor_status}"

    # Bonus: recommendation() method
    def recommendation(self):
        risk = self.calculate_risk()
        recommendations = {
            "LOW": "Normal monitoring",
            "MODERATE": "Continue monitoring",
            "HIGH": "Increased monitoring recommended",
            "EXTREME": "Immediate attention required",
            "UNKNOWN": "Check sensor/data input"
        }
        return recommendations.get(risk, "No action")


print("=== Exercise 3: OOP Climate Monitoring System ===")

# Create at least 5 ClimateStation/SmartClimateStation objects and place them in a list
stations = [
    SmartClimateStation("Damascus", 38.0, 30, 2.0, "OK"),
    SmartClimateStation("Aleppo", 41.5, 20, 0.0, "OK"),
    SmartClimateStation("Latakia", 29.0, 65, 10.0, "Warning"),
    SmartClimateStation("Homs", 33.0, 35, 12.0, "OK"),
    SmartClimateStation("Sweida", 31.0, 40.0, 14.0, "OK"),
]

# Use a loop to display their information, check sensor, and show recommendations
for station in stations:
    station.display_summary()
    print("  -> Risk:", station.calculate_risk())
    print("  -> Sensor:", station.check_sensor())
    print("  -> Recommendation:", station.recommendation())
    print()