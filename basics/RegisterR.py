def load(machine):
    reset = "(z NOT K)(Di AND z L) Di"
    nand2 = "(z AND a b)(c NOT z) c"
    machine.logic('nand2', nand2)
    machine.logic('reset', reset)

    RegC0 = "[(Res R0), (K L), reset, (Ri0)], [(Ri0 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QRn0), (a b), nand2, (QR0)], [(y QR0), (a b), nand2, (QRn0)], [(x QRn0), (a b), nand2, (QR0)], [(y QR0), (a b), nand2, (QRn0)]"    
    RegC1 = "[(Res R1), (K L), reset, (Ri1)], [(Ri1 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QRn1), (a b), nand2, (QR1)], [(y QR1), (a b), nand2, (QRn1)], [(x QRn1), (a b), nand2, (QR1)], [(y QR1), (a b), nand2, (QRn1)]"      
    RegC2 = "[(Res R2), (K L), reset, (Ri2)], [(Ri2 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QRn2), (a b), nand2, (QR2)], [(y QR2), (a b), nand2, (QRn2)], [(x QRn2), (a b), nand2, (QR2)], [(y QR2), (a b), nand2, (QRn2)]"       
    RegC3 = "[(Res R3), (K L), reset, (Ri3)], [(Ri3 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QRn3), (a b), nand2, (QR3)], [(y QR3), (a b), nand2, (QRn3)], [(x QRn3), (a b), nand2, (QR3)], [(y QR3), (a b), nand2, (QRn3)]"        

    machine.chip('RegC0', RegC0)
    machine.chip('RegC1', RegC1)
    machine.chip('RegC2', RegC2)
    machine.chip('RegC3', RegC3)


    burn  = "(R3 R2 R1 R0)(E Res)(RegC0 RegC1 RegC2 RegC3)(QR3 QR2 QR1 QR0)"
    machine.burn("registerR", burn)

    burn2  = "(E Res)(RegC0 RegC1 RegC2 RegC3)(QR3 QR2 QR1 QR0)"
    machine.burn("regR", burn2)