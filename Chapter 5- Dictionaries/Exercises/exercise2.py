# Create a glossary dictionary with programming terms as keys and their meanings as values
glossary = {
    'variable': 'A named location in memory that stores a value and whose value can be changed during program execution.',
    'loop': 'A sequence of instructions that is continually repeated until a certain condition is met.',
    'list': 'A collection of items in a particular order that can be modified, with duplicate items allowed.',
    'dictionary': 'A collection of key-value pairs that maps from keys to values, with no duplicate keys allowed.',
    'function': 'A block of organized, reusable code that is used to perform a single, related action.'
}

# Print each word and its meaning with a newline in between
for term, definition in glossary.items():
    print(f"{term.title()}:\n{definition}\n")
