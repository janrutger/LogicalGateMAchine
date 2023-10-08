def load(machine):
    reset = "(z NOT K)(Di AND z L) Di"
    nand2 = "(z AND a b)(c NOT z) c"
    machine.logic('nand2', nand2)
    machine.logic('reset', reset)

    RegB0 = "[(Res D0), (K L), reset, (Di0)], [(Di0 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QBn0), (a b), nand2, (QB0)], [(y QB0), (a b), nand2, (QBn0)], [(x QBn0), (a b), nand2, (QB0)], [(y QB0), (a b), nand2, (QBn0)]"    
    RegB1 = "[(Res D1), (K L), reset, (Di1)], [(Di1 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QBn1), (a b), nand2, (QB1)], [(y QB1), (a b), nand2, (QBn1)], [(x QBn1), (a b), nand2, (QB1)], [(y QB1), (a b), nand2, (QBn1)]"      
    RegB2 = "[(Res D2), (K L), reset, (Di2)], [(Di2 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QBn2), (a b), nand2, (QB2)], [(y QB2), (a b), nand2, (QBn2)], [(x QBn2), (a b), nand2, (QB2)], [(y QB2), (a b), nand2, (QBn2)]"       
    RegB3 = "[(Res D3), (K L), reset, (Di3)], [(Di3 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QBn3), (a b), nand2, (QB3)], [(y QB3), (a b), nand2, (QBn3)], [(x QBn3), (a b), nand2, (QB3)], [(y QB3), (a b), nand2, (QBn3)]"        

    machine.chip('RegB0', RegB0)
    machine.chip('RegB1', RegB1)
    machine.chip('RegB2', RegB2)
    machine.chip('RegB3', RegB3)


    burn  = "(D3 D2 D1 D0)(E Res)(RegB0 RegB1 RegB2 RegB3)(QB3 QB2 QB1 QB0)"
    machine.burn("registerB", burn)