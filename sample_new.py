import lgm as m

## AND gate with B input is the NOT output of the gate
## Preserve pinstates 

##### first chip example ####################################
#Single logic, Single (burnded)Chip Example
machine = m.LGM()

logic = "(O AND A On)(On NOT O) O"
machine.logic('logic', logic)

machine.dip('1', "(A)")
print(machine.run('logic'))
print(machine.run('logic'))
print(machine.run('logic'))

chip = "[(1), (A), logic, (2)]"
machine.chip('chip1', chip)

machine.dip('1', "(1)")

machine.run('chip1')
print(machine.led('(2)'))
machine.run('chip1')
print(machine.led('(2)'))

burn = "(1)(chip1)(2)"
machine.burn("CHIP", burn)

print(machine.run("CHIP", ("1")))
print(machine.run("CHIP", ("1")))
print(machine.run("CHIP", ("1")))

#Twice logic, two Chips, ONE burned Chip Example

machine = m.LGM()

and2 = "(c AND a b) c"
not1 = "(b NOT a) b"
machine.logic('and2', and2)
machine.logic('not1', not1)

and2C = "[(1 2), (a b), and2, (3)]"
not1C = "[(3), (a), not1, (2)]"

machine.chip('and2C', and2C)
machine.chip('not1C', not1C)

burn = "(1)(and2C not1C)(3)"
machine.burn("CHIP", burn)

print(machine.run("CHIP", ("1")))
print(machine.run("CHIP", ("1")))
print(machine.run("CHIP", ("1")))

#Twice logic, two Chips, ONE burned Chip Example

machine = m.LGM()

and2 = "(c AND A b) c"
not1 = "(x NOT b) x"
machine.logic('and2', and2)
machine.logic('not1', not1)

chip = "[(1 On), (A b), and2, (2)], [(2), (b), not1, (On)]"
machine.chip('chip', chip)

burn = "(1)(chip)(2)"
machine.burn("CHIP", burn)

print(machine.run("CHIP", ("1")))
print(machine.run("CHIP", ("1")))
print(machine.run("CHIP", ("1")))
print(machine.run("CHIP", ("1")))
