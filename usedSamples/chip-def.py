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


machine = m.LGM()
    and2 = "(c AND a b) c"
    machine.logic('and2', and2)

    machine.dip('111', "(A B C)")

    machine.dip(machine.led("(A B)"), "(a b)")
    machine.dip(machine.run('and2'), "(d)")
    machine.dip(machine.led("(d C)"), "(a b)")
    machine.dip(machine.run('and2'), "(D)")



    print(machine.led("(D)"))

    CHIP = "[(A B), (a b), and2, (d)], [(d C), (a b), and2, (D)]"
    machine.chip('CHIP', CHIP)

    
    
    
    
    print(machine.allChips['CHIP'][0])