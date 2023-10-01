import lgm as m

machine = m.LGM()

#CLOCK
logic = "(O AND A On)(On NOT O) O"
machine.logic('logic', logic)
chip = "[(1), (A), logic, (Clk)]"
machine.chip('chip1', chip)
burn = "(1)(chip1)(Clk)"
machine.burn("clock", burn)

logic = "(Clk2 AND Clk Q) Clk2"
machine.logic('Clk2', logic)



# machine.dip(machine.run('clock', ("1")), "(Clk)")
# print(machine.led("(Clk)"))

#D-latch
nand2 = "(z AND a b)(c NOT z) c"
machine.logic('nand2', nand2)

dlatch = "[(Qn Clk), (a b), nand2, (x)], [(Clk x), (a b), nand2, (y)], [(x Qn), (a b), nand2, (Q)], [(y Q), (a b), nand2, (Qn)], [(x Qn), (a b), nand2, (Q)], [(y Q), (a b), nand2, (Qn)]"
machine.chip('dlatch', dlatch)
burn = "(Clk)(dlatch)(Q)"
machine.burn("Dlatch", burn)

dlatch1 = "[(Qn1 Clk2), (a b), nand2, (x)], [(Clk2 x), (a b), nand2, (y)], [(x Qn1), (a b), nand2, (Q1)], [(y Q1), (a b), nand2, (Qn1)], [(x Qn1), (a b), nand2, (Q1)], [(y Q1), (a b), nand2, (Qn1)]"
machine.chip('dlatch1', dlatch1)
burn1 = "(Q)(dlatch1)(Q1)"
machine.burn("Dlatch1", burn1)

machine.dip('1001', "(Q Qn Q1 Qn1)")


machine.run('Dlatch', (machine.run('clock', ("1"))))
machine.run('Clk2')
machine.run('dlatch1')
print(machine.led("(Qn1 Qn Clk)"))

machine.run('Dlatch', (machine.run('clock', ("1"))))
machine.run('Clk2')
machine.run('dlatch1')
print(machine.led("(Qn1 Qn Clk)"))

machine.run('Dlatch', (machine.run('clock', ("1"))))
machine.run('Clk2')
machine.run('dlatch1')
print(machine.led("(Qn1 Qn Clk)"))

machine.run('Dlatch', (machine.run('clock', ("1"))))
machine.run('Clk2')
machine.run('dlatch1')
print(machine.led("(Qn1 Qn Clk)"))

machine.run('Dlatch', (machine.run('clock', ("1"))))
machine.run('Clk2')
machine.run('dlatch1')
print(machine.led("(Qn1 Qn Clk)"))

machine.run('Dlatch', (machine.run('clock', ("1"))))
machine.run('Clk2')
machine.run('dlatch1')
print(machine.led("(Qn1 Qn Clk)"))

machine.run('Dlatch', (machine.run('clock', ("1"))))
machine.run('Clk2')
machine.run('dlatch1')
print(machine.led("(Qn1 Qn Clk)"))

machine.run('Dlatch', (machine.run('clock', ("1"))))
machine.run('Clk2')
machine.run('dlatch1')
print(machine.led("(Qn1 Qn Clk)"))

machine.run('Dlatch', (machine.run('clock', ("1"))))
machine.run('Clk2')
machine.run('dlatch1')
print(machine.led("(Qn1 Qn Clk)"))

machine.run('Dlatch', (machine.run('clock', ("1"))))
machine.run('Clk2')
machine.run('dlatch1')
print(machine.led("(Qn1 Qn Clk)"))

machine.run('Dlatch', (machine.run('clock', ("1"))))
machine.run('Clk2')
machine.run('dlatch1')
print(machine.led("(Qn1 Qn Clk)"))

machine.run('Dlatch', (machine.run('clock', ("1"))))
machine.run('Clk2')
machine.run('dlatch1')
print(machine.led("(Qn1 Qn Clk)"))








