# input_string = "(a1 a2)(b1 b2)(chip chip)(o1 o2)"

# # Split the input string into individual parts using the pattern ')( '
# parts = input_string.split(')(')

# # Add a closing parenthesis to the last part of each split
# parts[-1] = parts[-1] + ')'

# # Add an opening parenthesis to the first part of each split
# parts[0] = '(' + parts[0]

# # Create a list of tuples
# list_of_tuples = [tuple(parts)]

# # Print the list of tuples
# print(list_of_tuples)




# input_string = "(a1 a2)(b1 b2)(chip chip)(o1 o2)"

# # Split the input string into individual parts using the pattern ')( '
# parts = input_string.split(')(')

# # Add a closing parenthesis to the last part of each split
# parts[-1] = parts[-1] + ')'

# # Add an opening parenthesis to the first part of each split
# parts[0] = '(' + parts[0]

# # Create a tuple
# my_tuple = tuple(parts)

# # Print the tuple
# print(my_tuple)







import re

input_string = "(a1 a2)(b1 b2)(chip chip)(o1 o2)"

# Use regular expression to split the input string while preserving parentheses
parts = re.findall(r'\([^)]*\)', input_string)
print(parts)
print(type(parts))

print(parts[0])
print(parts[1])
print(parts[2])
print(parts[3])




chips = tuple(parts[2].strip('()').split(' '))
print(chips)
# Create a tuple
#my_tuple = tuple(parts)

# Print the tuple
#print(my_tuple)




