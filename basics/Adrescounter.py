def load(machine):
    clk1 = "(clk1 AND E Qac) clk1"
    machine.logic('clk1', clk1)

    # clk2 = "(clk2 AND clk1 Qac1) clk2"
    # machine.logic('clk2', clk2)

    # clk3 = "(clk3 AND clk2 Qac2) clk3"
    # machine.logic('clk3', clk3)

    #D-latch
    nand2 = "(z AND a b)(c NOT z) c"
    machine.logic('nand2', nand2)

    AC0 = "[(Qacn E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x Qacn), (a b), nand2, (Qac)], [(y Qac), (a b), nand2, (Qacn)], [(x Qacn), (a b), nand2, (Qac)], [(y Qac), (a b), nand2, (Qacn)]"
    machine.chip('AC0', AC0)

    AC1 = "[(Qacn1 clk1), (a b), nand2, (x)], [(clk1 x), (a b), nand2, (y)], [(x Qacn1), (a b), nand2, (Qac1)], [(y Qac1), (a b), nand2, (Qacn1)], [(x Qacn1), (a b), nand2, (Qac1)], [(y Qac1), (a b), nand2, (Qacn1)]"
    machine.chip('AC1', AC1)

    burn = "(E)(AC0 clk1 AC1)(Qacn1 Qacn)"
    machine.burn("adrescounter", burn)

    # dlatch2 = "[(Qacn2 clk2), (a b), nand2, (x)], [(clk2 x), (a b), nand2, (y)], [(x Qacn2), (a b), nand2, (Qac2)], [(y Qac2), (a b), nand2, (Qacn2)], [(x Qacn2), (a b), nand2, (Qac2)], [(y Qac2), (a b), nand2, (Qacn2)]"
    # machine.chip('dlatch2', dlatch2)

    # dlatch3 = "[(Qacn3 clk3), (a b), nand2, (x)], [(clk3 x), (a b), nand2, (y)], [(x Qacn3), (a b), nand2, (Qac3)], [(y Qac3), (a b), nand2, (Qacn3)], [(x Qacn3), (a b), nand2, (Qac3)], [(y Qac3), (a b), nand2, (Qacn3)]"
    # machine.chip('dlatch3', dlatch3)

    # burn = "(E)(dlatch clk1 dlatch1 clk2 dlatch2 clk3 dlatch3)(Qacn3 Qacn2 Qacn1 Qacn)"
    # machine.burn("counter", burn)