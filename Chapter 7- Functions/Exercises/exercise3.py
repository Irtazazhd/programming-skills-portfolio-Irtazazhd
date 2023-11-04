def make_shirt(size, message):
    """Print a sentence summarizing the shirt size and message."""
    print(f"A {size}-sized shirt will be printed with the message: '{message}'")

# Call the function using positional arguments
make_shirt("Medium", "I Love Python")

# Call the function using keyword arguments
make_shirt(size="Large", message="Python Developer")
