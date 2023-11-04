# List of places to visit
places_to_visit = ["Pakistan", "palestine", "turkey", "saudia arabia", "oman"]

# Print the list in its original order
print("Original order:", places_to_visit)

# Print the list in alphabetical order using sorted()
print("Alphabetical order:", sorted(places_to_visit))

# Verify that the original order is still preserved
print("Original order (again):", places_to_visit)

# Print the list in reverse alphabetical order using sorted()
print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True))

# Verify that the original order is still preserved
print("Original order (again):", places_to_visit)

# Change the order of the list using reverse()
places_to_visit.reverse()
print("Reversed order:", places_to_visit)

# Change the order of the list again using reverse()
places_to_visit.reverse()
print("Back to original order:", places_to_visit)

# Change the order of the list to alphabetical using sort()
places_to_visit.sort()
print("Alphabetical order:", places_to_visit)

# Change the order of the list to reverse alphabetical using sort()
places_to_visit.sort(reverse=True)
print("Reverse alphabetical order:", places_to_visit)
