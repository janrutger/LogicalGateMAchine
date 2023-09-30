# An Johnson-Counter (ring-countr)

import lgm as m
machine = m.LGM()

nand2 = "(z AND a b)(c NOT z) c"
machine.logic('nand2', nand2)

Dlatch1 ="[(Qn5 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x Qn1), (a b), nand2, (Q1)], [(y Q1), (a b), nand2, (Qn1)], [(x Qn1), (a b), nand2, (Q1)], [(y Q1), (a b), nand2, (Qn1)]"
Dlatch2 = "[(Q1 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x Qn2), (a b), nand2, (Q2)], [(y Q2), (a b), nand2, (Qn2)], [(x Qn2), (a b), nand2, (Q2)], [(y Q2), (a b), nand2, (Qn2)]"
Dlatch3 = "[(Q2 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x Qn3), (a b), nand2, (Q3)], [(y Q3), (a b), nand2, (Qn3)], [(x Qn3), (a b), nand2, (Q3)], [(y Q3), (a b), nand2, (Qn3)]"
Dlatch4 = "[(Q3 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x Qn4), (a b), nand2, (Q4)], [(y Q4), (a b), nand2, (Qn4)], [(x Qn4), (a b), nand2, (Q4)], [(y Q4), (a b), nand2, (Qn4)]"
Dlatch5 = "[(Q4 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x Qn5), (a b), nand2, (Q5)], [(y Q5), (a b), nand2, (Qn5)], [(x Qn5), (a b), nand2, (Q5)], [(y Q5), (a b), nand2, (Qn5)]"

machine.chip('Dlatch1', Dlatch1)
machine.chip('Dlatch2', Dlatch2)
machine.chip('Dlatch3', Dlatch3)
machine.chip('Dlatch4', Dlatch4)
machine.chip('Dlatch5', Dlatch5)

burn = "(E)(Dlatch5 Dlatch4 Dlatch3 Dlatch2 Dlatch1)(Q4 Q3 Q2 Q1)"
machine.burn("counter", burn)

print(machine.run("counter", ("1")))
print(machine.run("counter", ("1")))
print(machine.run("counter", ("1")))
print(machine.run("counter", ("1")))
print(machine.run("counter", ("1")))
print(machine.run("counter", ("1")))
print(machine.run("counter", ("1")))
print(machine.run("counter", ("1")))
print(machine.run("counter", ("1")))