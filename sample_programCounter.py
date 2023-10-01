import lgm as m
machine = m.LGM()

nand2 = "(z AND a b)(c NOT z) c"
machine.logic('nand2', nand2)

and2 = "(c AND a b) c"
machine.logic('and2', and2)


Dlatch0 = "[(D0 E0), (a b), nand2, (x)], [(E0 x), (a b), nand2, (y)], [(x Qn0), (a b), nand2, (Q0)], [(y Q0), (a b), nand2, (Qn0)], [(x Qn0), (a b), nand2, (Q0)], [(y Q0), (a b), nand2, (Qn0)]"
Dlatch1 = "[(Q0 E0), (a b), nand2, (x)], [(E0 x), (a b), nand2, (y)], [(x Qn1), (a b), nand2, (Q1)], [(y Q1), (a b), nand2, (Qn1)], [(x Qn1), (a b), nand2, (Q1)], [(y Q1), (a b), nand2, (Qn1)]"
Dlatch2 = "[(D2 E0), (a b), nand2, (x)], [(E0 x), (a b), nand2, (y)], [(x Qn2), (a b), nand2, (Q2)], [(y Q2), (a b), nand2, (Qn2)], [(x Qn2), (a b), nand2, (Q2)], [(y Q2), (a b), nand2, (Qn2)]"
Dlatch3 = "[(D3 E0), (a b), nand2, (x)], [(E0 x), (a b), nand2, (y)], [(x Qn3), (a b), nand2, (Q3)], [(y Q3), (a b), nand2, (Qn3)], [(x Qn3), (a b), nand2, (Q3)], [(y Q3), (a b), nand2, (Qn3)]"

And1 = "[(Q0 Q1), (a b), and2, (D2)]"
And2 = "[(D2 Q2), (a b), and2, (D3)]"


machine.chip('bit0', Dlatch0)
machine.chip('bit1', Dlatch1)
machine.chip('bit2', Dlatch2)
machine.chip('bit3', Dlatch3)

machine.chip('And1', And1)
machine.chip('And2', And2)


machine.dip('11', "(E0 D0)")

# machine.run('bit0')
# # machine.run('bit0')
# print(machine.led("(Q3 Q2 Q1 Q0)"))
# machine.run('bit1')
# # machine.run('bit1')
# print(machine.led("(Q3 Q2 Q1 Q0)"))
# machine.run('And1')
# machine.run('bit2')
# print(machine.led("(Q3 Q2 Q1 Q0)"))
# machine.run('And2')
# machine.run('bit3')
# print(machine.led("(Q3 Q2 Q1 Q0)"))






# machine.run('bit3')
# machine.run('And2')
# print(machine.led("(Q3 Q2 Q1 Q0)"))
# machine.run('bit2')
# machine.run('And1')
# print(machine.led("(Q3 Q2 Q1 Q0)"))
# machine.run('bit1')
# print(machine.led("(Q3 Q2 Q1 Q0)"))
# machine.run('bit0')
# print(machine.led("(Q3 Q2 Q1 Q0)"))

machine.run('And2')
machine.run('bit3')
print(machine.led("(Q3 Q2 Q1 Q0)"))
machine.run('And1')
machine.run('bit2')
print(machine.led("(Q3 Q2 Q1 Q0)"))
machine.run('bit1')
print(machine.led("(Q3 Q2 Q1 Q0)"))
machine.run('bit0')
print(machine.led("(Q3 Q2 Q1 Q0)"))


machine.run('And2')
machine.run('bit3')
print(machine.led("(Q3 Q2 Q1 Q0)"))
machine.run('And1')
machine.run('bit2')
print(machine.led("(Q3 Q2 Q1 Q0)"))
machine.run('bit1')
print(machine.led("(Q3 Q2 Q1 Q0)"))
machine.run('bit0')
print(machine.led("(Q3 Q2 Q1 Q0)"))