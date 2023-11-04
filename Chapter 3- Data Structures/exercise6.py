# Original list of guests
guests = ["irti", "cafetaria", "topper", "abdu", "taha"]

# Print a message saying you can invite only two people for dinner
print("I can invite only two people for dinner.")

# Use pop() to remove guests from the list one at a time until only two names remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# Print a message to each of the two people still on your list, letting them know they're still invited
for guest in guests:
    print(f"{guest}, you're still invited to dinner.")

# Use del to remove the last two names from your list
del guests[0]
del guests[0]

# Print your list to make sure you have an empty list at the end of your program
print("Guest list is now empty:", guests)
