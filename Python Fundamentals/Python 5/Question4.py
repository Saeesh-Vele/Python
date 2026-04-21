import json

# Step 1: Create a dictionary of cities and populations
cities = {
    "Mumbai": 20411000,
    "Delhi": 16787941,
    "Bangalore": 8443675
}

# Step 2: Save the dictionary to Q4_cities.json
with open("Q4_cities.json", "w") as file:
    json.dump(cities, file, indent=4)

# Step 3: Load the JSON file and print each city and population
with open("Q4_cities.json", "r") as file:
    data = json.load(file)

print("Current Cities and Populations:")
for city, population in data.items():
    print(city, ":", population)

# Step 4: Ask the user for a new city and its population
new_city = input("Enter a new city: ")
new_population = int(input("Enter its population: "))

# Step 5: Update the dictionary
data[new_city] = new_population

# Step 6: Save the updated data back to the JSON file
with open("Q4_cities.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file updated successfully!")