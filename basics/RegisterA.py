def load(machine):
    reset = "(z NOT K)(Di AND z L) Di"
    nand2 = "(z AND a b)(c NOT z) c"
    machine.logic('nand2', nand2)
    machine.logic('reset', reset)

    RegA0 = "[(Res D0), (K L), reset, (Di0)], [(Di0 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QAn0), (a b), nand2, (QA0)], [(y QA0), (a b), nand2, (QAn0)], [(x QAn0), (a b), nand2, (QA0)], [(y QA0), (a b), nand2, (QAn0)]"    
    RegA1 = "[(Res D1), (K L), reset, (Di1)], [(Di1 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QAn1), (a b), nand2, (QA1)], [(y QA1), (a b), nand2, (QAn1)], [(x QAn1), (a b), nand2, (QA1)], [(y QA1), (a b), nand2, (QAn1)]"      
    RegA2 = "[(Res D2), (K L), reset, (Di2)], [(Di2 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QAn2), (a b), nand2, (QA2)], [(y QA2), (a b), nand2, (QAn2)], [(x QAn2), (a b), nand2, (QA2)], [(y QA2), (a b), nand2, (QAn2)]"       
    RegA3 = "[(Res D3), (K L), reset, (Di3)], [(Di3 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QAn3), (a b), nand2, (QA3)], [(y QA3), (a b), nand2, (QAn3)], [(x QAn3), (a b), nand2, (QA3)], [(y QA3), (a b), nand2, (QAn3)]"        

    machine.chip('RegA0', RegA0)
    machine.chip('RegA1', RegA1)
    machine.chip('RegA2', RegA2)
    machine.chip('RegA3', RegA3)


    burn  = "(D3 D2 D1 D0)(E Res)(RegA0 RegA1 RegA2 RegA3)(QA3 QA2 QA1 QA0)"
    machine.burn("registerA", burn)