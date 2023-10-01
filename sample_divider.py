import lgm as m

machine = m.LGM()

#CLOCK and Clock2
logic = "(O AND A On)(On NOT O) O On"
machine.logic('logic', logic)
chip = "[(E), (A), logic, (Clk Clkn)]"
machine.chip('clock', chip)
# burn = "(E)(clock)(Clk Clkn)"
# machine.burn("Clock", burn)

logic = "(clk1 AND Clk Q) clk1"
machine.logic('clk1', logic)


#D-latch
nand2 = "(z AND a b)(c NOT z) c"
machine.logic('nand2', nand2)

dlatch = "[(Qn Clk), (a b), nand2, (x)], [(Clk x), (a b), nand2, (y)], [(x Qn), (a b), nand2, (Q)], [(y Q), (a b), nand2, (Qn)], [(x Qn), (a b), nand2, (Q)], [(y Q), (a b), nand2, (Qn)]"
machine.chip('dlatch', dlatch)
#burn = "(Clk)(dlatch)(Q)"
#machine.burn("Dlatch", burn)

dlatch1 = "[(Qn1 clk1), (a b), nand2, (x)], [(clk1 x), (a b), nand2, (y)], [(x Qn1), (a b), nand2, (Q1)], [(y Q1), (a b), nand2, (Qn1)], [(x Qn1), (a b), nand2, (Q1)], [(y Q1), (a b), nand2, (Qn1)]"
machine.chip('dlatch1', dlatch1)
#burn1 = "(Q)(dlatch1)(Q1)"
#machine.burn("Dlatch1", burn1)

burn = "(E)(clock dlatch clk1 dlatch1)(Qn1 Qn Clkn)"
machine.burn("divider", burn)

## Run logic

print(machine.run('divider', ("1")))
print(machine.run('divider', ("1")))
print(machine.run('divider', ("1")))
print(machine.run('divider', ("1")))
print(machine.run('divider', ("1")))
print(machine.run('divider', ("1")))
print(machine.run('divider', ("1")))
print(machine.run('divider', ("1")))



# machine.run('Dlatch', (machine.run('Clock', ("1"))))
# machine.run('Clk2')
# machine.run('dlatch1')
# print(machine.led("(Qn1 Qn Clkn)"))

# machine.run('Dlatch', (machine.run('Clock', ("1"))))
# machine.run('Clk2')
# machine.run('dlatch1')
# print(machine.led("(Qn1 Qn Clkn)"))

# machine.run('Dlatch', (machine.run('Clock', ("1"))))
# machine.run('Clk2')
# machine.run('dlatch1')
# print(machine.led("(Qn1 Qn Clkn)"))

# machine.run('Dlatch', (machine.run('Clock', ("1"))))
# machine.run('Clk2')
# machine.run('dlatch1')
# print(machine.led("(Qn1 Qn Clkn)"))

# machine.run('Dlatch', (machine.run('Clock', ("1"))))
# machine.run('Clk2')
# machine.run('dlatch1')
# print(machine.led("(Qn1 Qn Clkn)"))

# machine.run('Dlatch', (machine.run('Clock', ("1"))))
# machine.run('Clk2')
# machine.run('dlatch1')
# print(machine.led("(Qn1 Qn Clkn)"))

# machine.run('Dlatch', (machine.run('Clock', ("1"))))
# machine.run('Clk2')
# machine.run('dlatch1')
# print(machine.led("(Qn1 Qn Clkn)"))

# machine.run('Dlatch', (machine.run('Clock', ("1"))))
# machine.run('Clk2')
# machine.run('dlatch1')
# print(machine.led("(Qn1 Qn Clkn)"))

# machine.run('Dlatch', (machine.run('Clock', ("1"))))
# machine.run('Clk2')
# machine.run('dlatch1')
# print(machine.led("(Qn1 Qn Clkn)"))

# machine.run('Dlatch', (machine.run('Clock', ("1"))))
# machine.run('Clk2')
# machine.run('dlatch1')
# print(machine.led("(Qn1 Qn Clkn)"))

# machine.run('Dlatch', (machine.run('Clock', ("1"))))
# machine.run('Clk2')
# machine.run('dlatch1')
# print(machine.led("(Qn1 Qn Clkn)"))

# machine.run('Dlatch', (machine.run('Clock', ("1"))))
# machine.run('Clk2')
# machine.run('dlatch1')
# print(machine.led("(Qn1 Qn Clkn)"))

# machine.run('Dlatch', (machine.run('Clock', ("1"))))
# machine.run('Clk2')
# machine.run('dlatch1')
# print(machine.led("(Qn1 Qn Clkn)"))

# machine.run('Dlatch', (machine.run('Clock', ("1"))))
# machine.run('Clk2')
# machine.run('dlatch1')
# print(machine.led("(Qn1 Qn Clkn)"))

# machine.run('Dlatch', (machine.run('Clock', ("1"))))
# machine.run('Clk2')
# machine.run('dlatch1')
# print(machine.led("(Qn1 Qn Clkn)"))








