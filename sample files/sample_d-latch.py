import lgm as m
machine = m.LGM()

nand2 = "(z AND a b)(c NOT z) c"
machine.logic('nand2', nand2)

Dlatch = "[(D E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x Qn), (a b), nand2, (Q)], [(y Q), (a b), nand2, (Qn)], [(x Qn), (a b), nand2, (Q)], [(y Q), (a b), nand2, (Qn)]"

machine.chip('Dlatch', Dlatch)
#machine.dip('10', "(Q Qn)")

burn = "(D E)(Dlatch)(Q Qn)"
machine.burn("CHIP", burn)

print(machine.run("CHIP", ("00")))
print(machine.run("CHIP", ("10")))
print(machine.run("CHIP", ("00")))

print(machine.run("CHIP", ("01")))
print(machine.run("CHIP", ("00")))
print(machine.run("CHIP", ("10")))
print(machine.run("CHIP", ("00")))


print(machine.run("CHIP", ("11")))
print(machine.run("CHIP", ("00")))

print(machine.run("CHIP", ("01")))
print(machine.run("CHIP", ("00")))
