def load(machine):
    clk1 = "(clk1 AND E Q) clk1"
    machine.logic('clk1', clk1)

    clk2 = "(clk2 AND clk1 Q1) clk2"
    machine.logic('clk2', clk2)

    clk3 = "(clk3 AND clk2 Q2) clk3"
    machine.logic('clk3', clk3)

    #D-latch
    nand2 = "(z AND a b)(c NOT z) c"
    machine.logic('nand2', nand2)

    machine.dip('10', "(H L)")

    dlatch = "[(Qn E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x Qn), (a b), nand2, (Q)], [(y Q), (a b), nand2, (Qn)], [(x Qn), (a b), nand2, (Q)], [(y Q), (a b), nand2, (Qn)]"
    machine.chip('dlatch', dlatch)

    dlatch1 = "[(Qn1 clk1), (a b), nand2, (x)], [(clk1 x), (a b), nand2, (y)], [(x Qn1), (a b), nand2, (Q1)], [(y Q1), (a b), nand2, (Qn1)], [(x Qn1), (a b), nand2, (Q1)], [(y Q1), (a b), nand2, (Qn1)]"
    machine.chip('dlatch1', dlatch1)

    dlatch2 = "[(Qn2 clk2), (a b), nand2, (x)], [(clk2 x), (a b), nand2, (y)], [(x Qn2), (a b), nand2, (Q2)], [(y Q2), (a b), nand2, (Qn2)], [(x Qn2), (a b), nand2, (Q2)], [(y Q2), (a b), nand2, (Qn2)]"
    machine.chip('dlatch2', dlatch2)

    dlatch3 = "[(Qn3 clk3), (a b), nand2, (x)], [(clk3 x), (a b), nand2, (y)], [(x Qn3), (a b), nand2, (Q3)], [(y Q3), (a b), nand2, (Qn3)], [(x Qn3), (a b), nand2, (Q3)], [(y Q3), (a b), nand2, (Qn3)]"
    machine.chip('dlatch3', dlatch3)

    burn = "(E)(dlatch clk1 dlatch1 clk2 dlatch2 clk3 dlatch3)(Qn3 Qn2 Qn1 Qn)"
    machine.burn("counter", burn)