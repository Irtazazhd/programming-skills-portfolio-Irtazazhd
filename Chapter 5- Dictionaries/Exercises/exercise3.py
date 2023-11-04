# Initial glossary dictionary with programming terms
glossary = {
    'variable': 'A named location in memory that stores a value and whose value can be changed during program execution.',
    'loop': 'A sequence of instructions that is continually repeated until a certain condition is met.',
    'list': 'A collection of items in a particular order that can be modified, with duplicate items allowed.',
    'dictionary': 'A collection of key-value pairs that maps from keys to values, with no duplicate keys allowed.',
    'function': 'A block of organized, reusable code that is used to perform a single, related action.'
}

# Loop through the glossary items and print them out
for term, definition in glossary.items():
    print(f"{term.title()}:\n{definition}\n")

# Add five more Python terms to the glossary
glossary['tuple'] = 'An immutable sequence of Python objects.'
glossary['set'] = 'A collection of items where each item is unique and unordered.'
glossary['comprehension'] = 'A compact way to process all or part of the elements in a sequence and return a list, dictionary, or set.'
glossary['decorator'] = 'A design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.'
glossary['generator'] = 'A type of iterable, like a list or tuple, that allows the user to iterate over it only once; it generates values on the fly and does not store them in memory.'

# Print the entire glossary with the new terms
print("Updated Glossary:")
for term, definition in glossary.items():
    print(f"{term.title()}:\n{definition}\n")
