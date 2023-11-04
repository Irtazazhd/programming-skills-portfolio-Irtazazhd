# Dictionary of rivers and the countries they run through
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states',
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Print just the names of the rivers
print("\nRivers mentioned:")
for river in rivers.keys():
    print(river.title())

# Print just the names of the countries
print("\nCountries mentioned:")
for country in rivers.values():
    print(country.title())
