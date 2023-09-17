input_string = "[(A1 A2 A3), (a b c), gate, (o1 o2 o3)], [(A1 A2 A3), (a b c), gate, (o1 o2 o3)]"

# Remove the square brackets and split the string into individual parts using ', '
parts = input_string.strip('[]').split('], [')

# Create a list to store the lists of strings
list_of_lists = []

# Iterate through the parts and split them into individual components
for part in parts:
    components = part.split(', ')
    
    # Append the components as a list to the list_of_lists
    list_of_lists.append(components)

# Print the list of lists
print(list_of_lists)
