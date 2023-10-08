def load(machine):
    reset = "(z NOT K)(Di AND z L) Di"
    nand2 = "(z AND a b)(c NOT z) c"
    machine.logic('nand2', nand2)
    machine.logic('reset', reset)

    RegB0 = "[(Res Q0), (K L), reset, (Qi0)], [(Qi0 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QBn0), (a b), nand2, (QB0)], [(y QB0), (a b), nand2, (QBn0)], [(x QBn0), (a b), nand2, (QB0)], [(y QB0), (a b), nand2, (QBn0)]"    
    RegB1 = "[(Res Q1), (K L), reset, (Qi1)], [(Qi1 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QBn1), (a b), nand2, (QB1)], [(y QB1), (a b), nand2, (QBn1)], [(x QBn1), (a b), nand2, (QB1)], [(y QB1), (a b), nand2, (QBn1)]"      
    RegB2 = "[(Res Q2), (K L), reset, (Qi2)], [(Qi2 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QBn2), (a b), nand2, (QB2)], [(y QB2), (a b), nand2, (QBn2)], [(x QBn2), (a b), nand2, (QB2)], [(y QB2), (a b), nand2, (QBn2)]"       
    RegB3 = "[(Res Q3), (K L), reset, (Qi3)], [(Qi3 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QBn3), (a b), nand2, (QB3)], [(y QB3), (a b), nand2, (QBn3)], [(x QBn3), (a b), nand2, (QB3)], [(y QB3), (a b), nand2, (QBn3)]"        

    machine.chip('RegB0', RegB0)
    machine.chip('RegB1', RegB1)
    machine.chip('RegB2', RegB2)
    machine.chip('RegB3', RegB3)


    burn  = "(Q3 Q2 Q1 Q0)(E Res)(RegB0 RegB1 RegB2 RegB3)(QB3 QB2 QB1 QB0)"
    machine.burn("registerB", burn)

    burn2  = "(E Res)(RegA0 RegA1 RegA2 RegA3)(QA3 QA2 QA1 QA0)"
    machine.burn("regB", burn2)