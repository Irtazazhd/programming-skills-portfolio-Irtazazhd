def make_shirt(size="Large", message="I love Python"):
    """Print a sentence summarizing the shirt size and message."""
    print(f"A {size}-sized shirt will be printed with the message: '{message}'")

# Create a large shirt with the default message
make_shirt()

# Create a medium shirt with the default message
make_shirt(size="Medium")

# Create a shirt of any size with a different message
make_shirt(size="Small", message="Python Programmer")
