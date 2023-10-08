import lgm as m
machine = m.LGM()

## 4 to 1 decoder and E(nable / write) bit
decoder = "(x NOT A0)(y NOT A1)(e0 AND x y)(E0 AND e0 E)(e1 AND A0 y)(E1 AND e1 E)(e2 AND x A1)(E2 AND e2 E)(e3 AND A0 A1)(E3 AND e3 E) E3 E2 E1 E0"
machine.logic('decoder', decoder)


## 4x4 memory cells, and reset bit
reset = "(z NOT K)(Di AND z L) Di"
nand2 = "(z AND a b)(c NOT z) c"
machine.logic('nand2', nand2)
machine.logic('reset', reset)

bit00 = "[(Res D0), (K L), reset, (Di00)], [(Di00 E0), (a b), nand2, (x)], [(E0 x), (a b), nand2, (y)], [(x Qn00), (a b), nand2, (Q00)], [(y Q00), (a b), nand2, (Qn00)], [(x Qn00), (a b), nand2, (Q00)], [(y Q00), (a b), nand2, (Qn00)]"    
bit01 = "[(Res D1), (K L), reset, (Di01)], [(Di01 E0), (a b), nand2, (x)], [(E0 x), (a b), nand2, (y)], [(x Qn01), (a b), nand2, (Q01)], [(y Q01), (a b), nand2, (Qn01)], [(x Qn01), (a b), nand2, (Q01)], [(y Q01), (a b), nand2, (Qn01)]"      
bit02 = "[(Res D2), (K L), reset, (Di02)], [(Di02 E0), (a b), nand2, (x)], [(E0 x), (a b), nand2, (y)], [(x Qn02), (a b), nand2, (Q02)], [(y Q02), (a b), nand2, (Qn02)], [(x Qn02), (a b), nand2, (Q02)], [(y Q02), (a b), nand2, (Qn02)]"       
bit03 = "[(Res D3), (K L), reset, (Di03)], [(Di03 E0), (a b), nand2, (x)], [(E0 x), (a b), nand2, (y)], [(x Qn03), (a b), nand2, (Q03)], [(y Q03), (a b), nand2, (Qn03)], [(x Qn03), (a b), nand2, (Q03)], [(y Q03), (a b), nand2, (Qn03)]"        

bit10 = "[(Res D0), (K L), reset, (Di10)], [(Di00 E1), (a b), nand2, (x)], [(E1 x), (a b), nand2, (y)], [(x Qn10), (a b), nand2, (Q10)], [(y Q10), (a b), nand2, (Qn10)], [(x Qn10), (a b), nand2, (Q10)], [(y Q10), (a b), nand2, (Qn10)]"    
bit11 = "[(Res D1), (K L), reset, (Di11)], [(Di01 E1), (a b), nand2, (x)], [(E1 x), (a b), nand2, (y)], [(x Qn11), (a b), nand2, (Q11)], [(y Q11), (a b), nand2, (Qn11)], [(x Qn11), (a b), nand2, (Q11)], [(y Q11), (a b), nand2, (Qn11)]"      
bit12 = "[(Res D2), (K L), reset, (Di12)], [(Di02 E1), (a b), nand2, (x)], [(E1 x), (a b), nand2, (y)], [(x Qn12), (a b), nand2, (Q12)], [(y Q12), (a b), nand2, (Qn12)], [(x Qn12), (a b), nand2, (Q12)], [(y Q12), (a b), nand2, (Qn12)]"       
bit13 = "[(Res D3), (K L), reset, (Di13)], [(Di03 E1), (a b), nand2, (x)], [(E1 x), (a b), nand2, (y)], [(x Qn13), (a b), nand2, (Q13)], [(y Q13), (a b), nand2, (Qn13)], [(x Qn13), (a b), nand2, (Q13)], [(y Q13), (a b), nand2, (Qn13)]"        

bit20 = "[(Res D0), (K L), reset, (Di20)], [(Di00 E2), (a b), nand2, (x)], [(E2 x), (a b), nand2, (y)], [(x Qn20), (a b), nand2, (Q20)], [(y Q20), (a b), nand2, (Qn20)], [(x Qn20), (a b), nand2, (Q20)], [(y Q20), (a b), nand2, (Qn20)]"    
bit21 = "[(Res D1), (K L), reset, (Di21)], [(Di01 E2), (a b), nand2, (x)], [(E2 x), (a b), nand2, (y)], [(x Qn21), (a b), nand2, (Q21)], [(y Q21), (a b), nand2, (Qn21)], [(x Qn21), (a b), nand2, (Q21)], [(y Q21), (a b), nand2, (Qn21)]"      
bit22 = "[(Res D2), (K L), reset, (Di22)], [(Di02 E2), (a b), nand2, (x)], [(E2 x), (a b), nand2, (y)], [(x Qn22), (a b), nand2, (Q22)], [(y Q22), (a b), nand2, (Qn22)], [(x Qn22), (a b), nand2, (Q22)], [(y Q22), (a b), nand2, (Qn22)]"       
bit23 = "[(Res D3), (K L), reset, (Di23)], [(Di03 E2), (a b), nand2, (x)], [(E2 x), (a b), nand2, (y)], [(x Qn23), (a b), nand2, (Q23)], [(y Q23), (a b), nand2, (Qn23)], [(x Qn23), (a b), nand2, (Q23)], [(y Q23), (a b), nand2, (Qn23)]"        

bit30 = "[(Res D0), (K L), reset, (Di30)], [(Di00 E3), (a b), nand2, (x)], [(E3 x), (a b), nand2, (y)], [(x Qn30), (a b), nand2, (Q30)], [(y Q30), (a b), nand2, (Qn30)], [(x Qn30), (a b), nand2, (Q30)], [(y Q30), (a b), nand2, (Qn30)]"    
bit31 = "[(Res D1), (K L), reset, (Di31)], [(Di01 E3), (a b), nand2, (x)], [(E3 x), (a b), nand2, (y)], [(x Qn31), (a b), nand2, (Q31)], [(y Q31), (a b), nand2, (Qn31)], [(x Qn31), (a b), nand2, (Q31)], [(y Q31), (a b), nand2, (Qn31)]"      
bit32 = "[(Res D2), (K L), reset, (Di32)], [(Di02 E3), (a b), nand2, (x)], [(E3 x), (a b), nand2, (y)], [(x Qn32), (a b), nand2, (Q32)], [(y Q32), (a b), nand2, (Qn32)], [(x Qn32), (a b), nand2, (Q32)], [(y Q32), (a b), nand2, (Qn32)]"       
bit33 = "[(Res D3), (K L), reset, (Di33)], [(Di03 E3), (a b), nand2, (x)], [(E3 x), (a b), nand2, (y)], [(x Qn33), (a b), nand2, (Q33)], [(y Q33), (a b), nand2, (Qn33)], [(x Qn33), (a b), nand2, (Q33)], [(y Q33), (a b), nand2, (Qn33)]"        


machine.chip('bit00', bit00)
machine.chip('bit01', bit01)
machine.chip('bit02', bit02)
machine.chip('bit03', bit03)

machine.chip('bit10', bit10)
machine.chip('bit11', bit11)
machine.chip('bit12', bit12)
machine.chip('bit13', bit13)

machine.chip('bit20', bit20)
machine.chip('bit21', bit21)
machine.chip('bit22', bit22)
machine.chip('bit23', bit23)

machine.chip('bit30', bit30)
machine.chip('bit31', bit31)
machine.chip('bit32', bit32)
machine.chip('bit33', bit33)

## 4x4 to 4x1 multiplexor
not1 = "(An NOT a) An"
and3 = "(z AND a b)(d AND z c) d"
or4  = "(z OR a b)(y OR c d)(r OR z y) r"

machine.logic('not1', not1)
machine.logic('and3', and3)
machine.logic('or4',  or4)

plexer0 = "[(A0), (a), not1, (A0n)], [(A1), (a), not1, (A1n)], [(Q00 A0n A1n), (a b c), and3, (y0)], [(Q10 A0 A1n), (a b c), and3, (y1)], [(Q20 A0n A1), (a b c), and3, (y2)], [(Q30 A0 A1), (a b c), and3, (y3)], [(y0 y1 y2 y3), (a b c d), or4, (Q0)]"
plexer1 = "[(A0), (a), not1, (A0n)], [(A1), (a), not1, (A1n)], [(Q01 A0n A1n), (a b c), and3, (y0)], [(Q11 A0 A1n), (a b c), and3, (y1)], [(Q21 A0n A1), (a b c), and3, (y2)], [(Q31 A0 A1), (a b c), and3, (y3)], [(y0 y1 y2 y3), (a b c d), or4, (Q1)]"
plexer2 = "[(A0), (a), not1, (A0n)], [(A1), (a), not1, (A1n)], [(Q02 A0n A1n), (a b c), and3, (y0)], [(Q12 A0 A1n), (a b c), and3, (y1)], [(Q22 A0n A1), (a b c), and3, (y2)], [(Q32 A0 A1), (a b c), and3, (y3)], [(y0 y1 y2 y3), (a b c d), or4, (Q2)]"
plexer3 = "[(A0), (a), not1, (A0n)], [(A1), (a), not1, (A1n)], [(Q03 A0n A1n), (a b c), and3, (y0)], [(Q13 A0 A1n), (a b c), and3, (y1)], [(Q23 A0n A1), (a b c), and3, (y2)], [(Q33 A0 A1), (a b c), and3, (y3)], [(y0 y1 y2 y3), (a b c d), or4, (Q3)]"


machine.chip('plexer0', plexer0)
machine.chip('plexer1', plexer1)
machine.chip('plexer2', plexer2)
machine.chip('plexer3', plexer3)


## burn a chip and test it!!
burn  = "(D3 D2 D1 D0)(A0 A1)(E Res)(decoder bit00 bit01 bit02 bit03 bit10 bit11 bit12 bit13 bit20 bit21 bit22 bit23 bit30 bit31 bit32 bit33 plexer0 plexer1 plexer2 plexer3)(Q3 Q2 Q1 Q0)"
machine.burn("MEM", burn)

print(machine.run("MEM", ("0001",'00','11')))
print(machine.run("MEM", ("0011",'01','11')))
print(machine.run("MEM", ("0111",'10','11')))
print(machine.run("MEM", ("1111",'11','11')))


print(machine.run("MEM", ("0000",'00','10')))
print(machine.run("MEM", ("0001",'01','10')))
print(machine.run("MEM", ("0010",'10','10')))
print(machine.run("MEM", ("1011",'11','10')))

print(machine.run("MEM", ("1111",'00','00')))
print(machine.run("MEM", ("1111",'01','00')))
print(machine.run("MEM", ("1111",'10','00')))
print(machine.run("MEM", ("1111",'11','00')))


print(machine.run("MEM", ("1110",'00','10')))
print(machine.run("MEM", ("1101",'01','10')))
print(machine.run("MEM", ("1011",'10','10')))
print(machine.run("MEM", ("0111",'11','10')))


print(machine.model())