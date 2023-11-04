# Define several dictionaries, each representing a different pet
pet_1 = {
    'animal_type': 'cat',
    'owner_name': 'irtaza',
}

pet_2 = {
    'animal_type': 'parrot',
    'owner_name': 'abdu',
}

pet_3 = {
    'animal_type': 'sheep',
    'owner_name': 'taha',
}

# Store these dictionaries in a list called pets
pets = [pet_1, pet_2, pet_3]

# Loop through the list and print information about each pet
for pet in pets:
    print(f"Here is what I know about {pet['owner_name']}'s pet:")
    for key, value in pet.items():
        print(f"  {key.title()}: {value}")
    print()  # Prints a newline for better separation between pets
