
import lgm as m
machine = m.LGM()

# # define and activate the logic

and3 = "(z AND A B)(D AND z C) D"
machine.logic('and3', and3)

# To run it: Set the input values and run the logic
machine.dip('110', "(A B C)")
print(machine.run('and3'))

# After you defined and test the logic you can make a chip of one of more logic componentens
chip = "[(1 2 3), (A B C), and3, (D)]"
machine.chip('chip1', chip)

# # To run it: Set the input values and run the chip
machine.dip('111', "(1 2 3)")
print(machine.run('chip1'))
print(machine.led('(D)'))

# # Now we have an working chip definition
# # and glue the inputs and output pins to the chip
#     burn = "(1 2 3)(chip1)(4)"
#     machine.burn("CHIP", burn)

# # # Now the chip is ready ro run
#     print(machine.run("CHIP", ("101")))

# #    print(machine.run("CHIP", ("111")))



#     print('end')