import lgm as m

machine = m.LGM()

#CLOCK
logic = "(O AND A On)(On NOT O) O"
machine.logic('logic', logic)
chip = "[(1), (A), logic, (2)]"
machine.chip('chip1', chip)
burn = "(1)(chip1)(2)"
machine.burn("clock", burn)

machine.dip(machine.run('clock', ("1")), "(Clk)")
print(machine.led("(Clk)"))

#D-latch
nand2 = "(z AND a b)(c NOT z) c"
machine.logic('nand2', nand2)
dlatch = "[(Qn Clk), (a b), nand2, (x)], [(Clk x), (a b), nand2, (y)], [(x Qn), (a b), nand2, (Q)], [(y Q), (a b), nand2, (Qn)], [(x Qn), (a b), nand2, (Q)], [(y Q), (a b), nand2, (Qn)]"
machine.chip('dlatch', dlatch)
burn = "(Clk)(dlatch)(Q)"
machine.burn("Dlatch", burn)


#machine.dip(machine.run('clock', ("1")), "(Clk)")
machine.run('Dlatch', (machine.run('clock', ("1"))))
print(machine.led("(Clk Q)"))

machine.run('Dlatch', (machine.run('clock', ("1"))))
print(machine.led("(Clk Q)"))

machine.run('Dlatch', (machine.run('clock', ("1"))))
print(machine.led("(Clk Q)"))

machine.run('Dlatch', (machine.run('clock', ("1"))))
print(machine.led("(Clk Q)"))

machine.run('Dlatch', (machine.run('clock', ("1"))))
print(machine.led("(Clk Q)"))

machine.run('Dlatch', (machine.run('clock', ("1"))))
print(machine.led("(Clk Q)"))

machine.run('Dlatch', (machine.run('clock', ("1"))))
print(machine.led("(Clk Q)"))

machine.run('Dlatch', (machine.run('clock', ("1"))))
print(machine.led("(Clk Q)"))

