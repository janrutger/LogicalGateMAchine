def load(machine):
    reset = "(z NOT K)(Di AND z L) Di"
    nand2 = "(z AND a b)(c NOT z) c"
    machine.logic('nand2', nand2)
    machine.logic('reset', reset)

    RegC0 = "[(Res D0), (K L), reset, (Di0)], [(Di0 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QRn0), (a b), nand2, (QR0)], [(y QR0), (a b), nand2, (QRn0)], [(x QRn0), (a b), nand2, (QR0)], [(y QR0), (a b), nand2, (QRn0)]"    
    RegC1 = "[(Res D1), (K L), reset, (Di1)], [(Di1 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QRn1), (a b), nand2, (QR1)], [(y QR1), (a b), nand2, (QRn1)], [(x QRn1), (a b), nand2, (QR1)], [(y QR1), (a b), nand2, (QRn1)]"      
    RegC2 = "[(Res D2), (K L), reset, (Di2)], [(Di2 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QRn2), (a b), nand2, (QR2)], [(y QR2), (a b), nand2, (QRn2)], [(x QRn2), (a b), nand2, (QR2)], [(y QR2), (a b), nand2, (QRn2)]"       
    RegC3 = "[(Res D3), (K L), reset, (Di3)], [(Di3 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x QRn3), (a b), nand2, (QR3)], [(y QR3), (a b), nand2, (QRn3)], [(x QRn3), (a b), nand2, (QR3)], [(y QR3), (a b), nand2, (QRn3)]"        

    machine.chip('RegC0', RegC0)
    machine.chip('RegC1', RegC1)
    machine.chip('RegC2', RegC2)
    machine.chip('RegC3', RegC3)


    burn  = "(D3 D2 D1 D0)(E Res)(RegC0 RegC1 RegC2 RegC3)(QR3 QR2 QR1 QR0)"
    machine.burn("registerR", burn)