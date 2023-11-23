# Get the month as input from the user
month = input("Enter the name of the month: ").lower()

# Define a dictionary to map months to seasons
seasons = {
    "december": "Winter",
    "january": "Winter",
    "february": "Winter",
    "march": "Spring",
    "april": "Spring",
    "may": "Spring",
    "june": "Summer",
    "july": "Summer",
    "august": "Summer",
    "september": "Fall",
    "october": "Fall",
    "november": "Fall"
}

# Determine the season and display the result
season = seasons.get(month, "Invalid input")
print(f"The season for {month} is {season}.")
