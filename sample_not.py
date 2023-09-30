import lgm as m

## Single NOT with only 1 input and only one output

##### first chip example ####################################
machine = m.LGM()
not1 = "(b NOT a) b"

machine.logic('not', not1)

machine.dip('1', '(a)')
print(machine.run("not"))
machine.dip('0', '(a)')
print(machine.run("not"))


chip = "[(1), (a), not, (2)]"
machine.chip('chip1', chip)

machine.dip('1', '(1)')
(machine.run("chip1"))
print(machine.led('(2)'))

machine.dip('0', '(1)')
(machine.run("chip1"))
print(machine.led('(2)'))


burn = "(1)(chip1)(2)"
machine.burn("NOT", burn)


print(machine.run("NOT", ("1")))
print(machine.run("NOT", ("0")))

print(machine.model())
