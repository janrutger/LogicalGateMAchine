import lgm as m
machine = m.LGM()
## All needed logic
plexer21 = "(z NOT X)(y AND D1 X)(x AND D0 z)(O OR x y) O"
machine.logic('plexer21', plexer21)

plexer31 = "(z NOT X1)(y AND D1 X1)(x AND D0 z)(r OR x y)(z1 NOT X2)(y1 AND D2 X2)(x1 AND r z1)(O OR x1 y1) O"
machine.logic('plexer31', plexer31)

adder = "(x XOR A B)(z AND A B)(S XOR x Cx)(y AND x Cx)(Co OR z y) Co S"
machine.logic('adder', adder)

and2 = "(c AND a b) c"
machine.logic('and2', and2)

or2 = "(c OR a b) c"
machine.logic('or2', or2)

not1 = "(b NOT a) b"
machine.logic('not1', not1)



## Glue the logic to on bit ALU
ALU = "[(A0), (a), not1, (An)], [(B0), (a), not1, (Bn)], [(A0 An Anot), (D0 D1 X), plexer21, (Ain)], [(B0 Bn Bnot), (D0 D1 X), plexer21, (Bin)], [(Ain Bin Cin), (A B Cx), adder, (Cout r2)], [(Ain Bin), (a b), or2, (r1)], [(Ain Bin), (a b), and2, (r0)], [(r0 r1 r2 S1 S2), (D0 D1 D2 X1 X2), plexer31, (R0)]"
machine.chip('ALU', ALU)




## Run de ALU
machine.dip('11', "(A0 B0)")
machine.dip('000', "(Anot Bnot Cin)")
machine.dip('00', "(S2 S1)")

machine.run("ALU")
print(machine.led('(Cout R0)'))