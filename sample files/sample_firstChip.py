import lgm as m

##### first chip example ####################################
machine = m.LGM()
and2 = "(c AND a b) c"
machine.logic('and2', and2)

machine.dip('110', "(A B C)")

machine.dip(machine.led("(A B)"), "(a b)")
machine.dip(machine.run('and2'), "(d)")
machine.dip(machine.led("(d C)"), "(a b)")
machine.dip(machine.run('and2'), "(D)")

print(machine.led("(D)"))

### chip starts here, same logic 
machine = m.LGM()
and2 = "(c AND a b) c"
machine.logic('and2', and2)

and3 = "[(A B), (a b), and2, (d)], [(d C), (a b), and2, (D)]"
machine.chip('and3', and3)

machine.dip('111', "(A B C)") 
machine.run('and3')
print(machine.led("(D)"))
print(machine.allChips)