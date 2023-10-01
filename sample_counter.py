import lgm as m

machine = m.LGM()

#CLOCK and Clock2
logic = "(O AND A On)(On NOT O) O On"
machine.logic('logic', logic)
chip = "[(E), (A), logic, (Clk Clkn)]"
machine.chip('clock', chip)

clk1 = "(clk1 AND Clk Q) clk1"
machine.logic('clk1', clk1)

clk2 = "(clk2 AND clk1 Q1) clk2"
machine.logic('clk2', clk2)

#D-latch
nand2 = "(z AND a b)(c NOT z) c"
machine.logic('nand2', nand2)

dlatch = "[(Qn Clk), (a b), nand2, (x)], [(Clk x), (a b), nand2, (y)], [(x Qn), (a b), nand2, (Q)], [(y Q), (a b), nand2, (Qn)], [(x Qn), (a b), nand2, (Q)], [(y Q), (a b), nand2, (Qn)]"
machine.chip('dlatch', dlatch)

dlatch1 = "[(Qn1 clk1), (a b), nand2, (x)], [(clk1 x), (a b), nand2, (y)], [(x Qn1), (a b), nand2, (Q1)], [(y Q1), (a b), nand2, (Qn1)], [(x Qn1), (a b), nand2, (Q1)], [(y Q1), (a b), nand2, (Qn1)]"
machine.chip('dlatch1', dlatch1)

dlatch2 = "[(Qn2 clk2), (a b), nand2, (x)], [(clk2 x), (a b), nand2, (y)], [(x Qn2), (a b), nand2, (Q2)], [(y Q2), (a b), nand2, (Qn2)], [(x Qn2), (a b), nand2, (Q2)], [(y Q2), (a b), nand2, (Qn2)]"
machine.chip('dlatch2', dlatch2)


burn = "(E)(clock dlatch clk1 dlatch1 clk2 dlatch2)(Qn2 Qn1 Qn Clkn)"
machine.burn("counter", burn)

## Run logic

print(machine.run('counter', ("1")))
print(machine.run('counter', ("1")))
print(machine.run('counter', ("1")))
print(machine.run('counter', ("1")))
print(machine.run('counter', ("1")))
print(machine.run('counter', ("1")))
print(machine.run('counter', ("1")))
print(machine.run('counter', ("1")))

print(machine.run('counter', ("1")))
print(machine.run('counter', ("1")))
print(machine.run('counter', ("1")))
print(machine.run('counter', ("1")))
print(machine.run('counter', ("1")))
print(machine.run('counter', ("1")))
print(machine.run('counter', ("1")))
print(machine.run('counter', ("1")))
print(machine.run('counter', ("1")))


