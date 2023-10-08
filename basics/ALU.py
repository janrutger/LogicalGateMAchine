def load(machine):
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

    ## Glue the logic to 4 one Bits ALU's 
    lsb0 = "[(QA0), (a), not1, (An)], [(QB0), (a), not1, (Bn)], [(QA0 An Anot), (D0 D1 X), plexer21, (Ain)], [(QB0 Bn Bnot), (D0 D1 X), plexer21, (Bin)], [(Ain Bin Bnot), (A B Cx), adder, (Cout r2)], [(Ain Bin), (a b), or2, (r1)], [(Ain Bin), (a b), and2, (r0)], [(r0 r1 r2 S1 S2), (D0 D1 D2 X1 X2), plexer31, (R0)]"
    bit1 = "[(QA1), (a), not1, (An)], [(QB1), (a), not1, (Bn)], [(QA1 An Anot), (D0 D1 X), plexer21, (Ain)], [(QB1 Bn Bnot), (D0 D1 X), plexer21, (Bin)], [(Ain Bin Cout), (A B Cx), adder, (Cout r2)], [(Ain Bin), (a b), or2, (r1)], [(Ain Bin), (a b), and2, (r0)], [(r0 r1 r2 S1 S2), (D0 D1 D2 X1 X2), plexer31, (R1)]"
    bit2 = "[(QA2), (a), not1, (An)], [(QB2), (a), not1, (Bn)], [(QA2 An Anot), (D0 D1 X), plexer21, (Ain)], [(QB2 Bn Bnot), (D0 D1 X), plexer21, (Bin)], [(Ain Bin Cout), (A B Cx), adder, (Cout r2)], [(Ain Bin), (a b), or2, (r1)], [(Ain Bin), (a b), and2, (r0)], [(r0 r1 r2 S1 S2), (D0 D1 D2 X1 X2), plexer31, (R2)]"
    bit3 = "[(QA3), (a), not1, (An)], [(QB3), (a), not1, (Bn)], [(QA3 An Anot), (D0 D1 X), plexer21, (Ain)], [(QB3 Bn Bnot), (D0 D1 X), plexer21, (Bin)], [(Ain Bin Cout), (A B Cx), adder, (Cout r2)], [(Ain Bin), (a b), or2, (r1)], [(Ain Bin), (a b), and2, (r0)], [(r0 r1 r2 S1 S2), (D0 D1 D2 X1 X2), plexer31, (R3)]"

    machine.chip('bit0', lsb0)
    machine.chip('bit1', bit1)
    machine.chip('bit2', bit2)
    machine.chip('bit3', bit3)

    # Burn an 4 bit ALU 
    burn = "(QA3 QA2 QA1 QA0)(QB3 QB2 QB1 QB0)(S1 S2 Anot Bnot)(bit0 bit1 bit2 bit3)(Cout R3 R2 R1 R0)"
    machine.burn('ALU', burn)
 
    burn2 = "(S1 S2 Anot Bnot)(bit0 bit1 bit2 bit3)(Cout R3 R2 R1 R0)"
    machine.burn('alu', burn2)


    # Truth table
    # ---------------------
    # | S1 | S2 | An | Bn |
    # ---------------------
    # |  0 |  0 |  0 |  0 |   AND
    # |  1 |  0 |  0 |  0 |   OR
    # |  1 |  0 |  1 |  1 |   NAND
    # |  0 |  0 |  1 |  1 |   NOR 
    # |  x |  1 |  0 |  0 |   ADD 
    # |  x |  1 |  0 |  1 |   SUB
    # ---------------------