# Original guest list
guest_list = ["abdur rehman", "taha", "basim"]

# Print the guest who can't make it
guest_cant_make_it = "Leonardo da Vinci"
print(f"{guest_cant_make_it} can't make it to the dinner.")

# Replace the guest who can't make it with a new person
new_guest = "faseeh"
guest_list.remove(guest_cant_make_it)
guest_list.append(new_guest)

# Generate new invitation messages
for guest in guest_list:
    print(f"Dear {guest},\nYou are cordially invited to dinner at my place. It would be an honor to have you join us for an evening of great conversation and delicious food. Please let me know if you can make it.\n\nSincerely, [irtaza]\n")
