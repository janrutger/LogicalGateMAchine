import lgm as m
machine = m.LGM()

reset = "(z NOT K)(Di AND z L) Di"
nand2 = "(z AND a b)(c NOT z) c"
machine.logic('nand2', nand2)
machine.logic('reset', reset)

bit00 = "[(Res D0), (K L), reset, (Di00)], [(Di00 E0), (a b), nand2, (x)], [(E0 x), (a b), nand2, (y)], [(x Qn00), (a b), nand2, (Q000)], [(y Q00), (a b), nand2, (Qn00)], [(x Qn00), (a b), nand2, (Q00)], [(y Q00), (a b), nand2, (Qn00)]"    
bit01 = "[(Res D1), (K L), reset, (Di01)], [(Di01 E0), (a b), nand2, (x)], [(E0 x), (a b), nand2, (y)], [(x Qn01), (a b), nand2, (Q001)], [(y Q01), (a b), nand2, (Qn01)], [(x Qn01), (a b), nand2, (Q01)], [(y Q01), (a b), nand2, (Qn01)]"      
bit02 = "[(Res D2), (K L), reset, (Di02)], [(Di02 E0), (a b), nand2, (x)], [(E0 x), (a b), nand2, (y)], [(x Qn02), (a b), nand2, (Q002)], [(y Q02), (a b), nand2, (Qn02)], [(x Qn02), (a b), nand2, (Q02)], [(y Q02), (a b), nand2, (Qn02)]"       
bit03 = "[(Res D3), (K L), reset, (Di03)], [(Di03 E0), (a b), nand2, (x)], [(E0 x), (a b), nand2, (y)], [(x Qn03), (a b), nand2, (Q003)], [(y Q03), (a b), nand2, (Qn03)], [(x Qn03), (a b), nand2, (Q03)], [(y Q03), (a b), nand2, (Qn03)]"        

bit10 = "[(Res D0), (K L), reset, (Di10)], [(Di00 E1), (a b), nand2, (x)], [(E1 x), (a b), nand2, (y)], [(x Qn10), (a b), nand2, (Q010)], [(y Q10), (a b), nand2, (Qn10)], [(x Qn10), (a b), nand2, (Q10)], [(y Q10), (a b), nand2, (Qn10)]"    
bit11 = "[(Res D1), (K L), reset, (Di11)], [(Di01 E1), (a b), nand2, (x)], [(E1 x), (a b), nand2, (y)], [(x Qn11), (a b), nand2, (Q011)], [(y Q11), (a b), nand2, (Qn11)], [(x Qn11), (a b), nand2, (Q11)], [(y Q11), (a b), nand2, (Qn11)]"      
bit12 = "[(Res D2), (K L), reset, (Di12)], [(Di02 E1), (a b), nand2, (x)], [(E1 x), (a b), nand2, (y)], [(x Qn12), (a b), nand2, (Q012)], [(y Q12), (a b), nand2, (Qn12)], [(x Qn12), (a b), nand2, (Q12)], [(y Q12), (a b), nand2, (Qn12)]"       
bit13 = "[(Res D3), (K L), reset, (Di13)], [(Di03 E1), (a b), nand2, (x)], [(E1 x), (a b), nand2, (y)], [(x Qn13), (a b), nand2, (Q013)], [(y Q13), (a b), nand2, (Qn13)], [(x Qn13), (a b), nand2, (Q13)], [(y Q13), (a b), nand2, (Qn13)]"        

bit20 = "[(Res D0), (K L), reset, (Di20)], [(Di00 E2), (a b), nand2, (x)], [(E2 x), (a b), nand2, (y)], [(x Qn20), (a b), nand2, (Q020)], [(y Q20), (a b), nand2, (Qn20)], [(x Qn20), (a b), nand2, (Q20)], [(y Q20), (a b), nand2, (Qn20)]"    
bit21 = "[(Res D1), (K L), reset, (Di21)], [(Di01 E2), (a b), nand2, (x)], [(E2 x), (a b), nand2, (y)], [(x Qn21), (a b), nand2, (Q021)], [(y Q21), (a b), nand2, (Qn21)], [(x Qn21), (a b), nand2, (Q21)], [(y Q21), (a b), nand2, (Qn21)]"      
bit22 = "[(Res D2), (K L), reset, (Di22)], [(Di02 E2), (a b), nand2, (x)], [(E2 x), (a b), nand2, (y)], [(x Qn22), (a b), nand2, (Q022)], [(y Q22), (a b), nand2, (Qn22)], [(x Qn22), (a b), nand2, (Q22)], [(y Q22), (a b), nand2, (Qn22)]"       
bit23 = "[(Res D3), (K L), reset, (Di23)], [(Di03 E2), (a b), nand2, (x)], [(E2 x), (a b), nand2, (y)], [(x Qn23), (a b), nand2, (Q023)], [(y Q23), (a b), nand2, (Qn23)], [(x Qn23), (a b), nand2, (Q23)], [(y Q23), (a b), nand2, (Qn23)]"        

bit30 = "[(Res D0), (K L), reset, (Di30)], [(Di00 E3), (a b), nand2, (x)], [(E3 x), (a b), nand2, (y)], [(x Qn30), (a b), nand2, (Q030)], [(y Q30), (a b), nand2, (Qn30)], [(x Qn30), (a b), nand2, (Q30)], [(y Q30), (a b), nand2, (Qn30)]"    
bit31 = "[(Res D1), (K L), reset, (Di31)], [(Di01 E3), (a b), nand2, (x)], [(E3 x), (a b), nand2, (y)], [(x Qn31), (a b), nand2, (Q031)], [(y Q31), (a b), nand2, (Qn31)], [(x Qn31), (a b), nand2, (Q31)], [(y Q31), (a b), nand2, (Qn31)]"      
bit32 = "[(Res D2), (K L), reset, (Di32)], [(Di02 E3), (a b), nand2, (x)], [(E3 x), (a b), nand2, (y)], [(x Qn32), (a b), nand2, (Q032)], [(y Q32), (a b), nand2, (Qn32)], [(x Qn32), (a b), nand2, (Q32)], [(y Q32), (a b), nand2, (Qn32)]"       
bit33 = "[(Res D3), (K L), reset, (Di33)], [(Di03 E3), (a b), nand2, (x)], [(E3 x), (a b), nand2, (y)], [(x Qn33), (a b), nand2, (Q033)], [(y Q33), (a b), nand2, (Qn33)], [(x Qn33), (a b), nand2, (Q33)], [(y Q33), (a b), nand2, (Qn33)]"        


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

decoder = "(x NOT A0)(y NOT A1)(E0 AND x y)(E1 AND A0 y)(E2 AND x A1)(E3 AND A0 A1) E0 E1 E2 E3"
machine.logic('decoder', decoder)


burn  = "(D3 D2 D1 D0)(A0 A1)(E Res)(bit00 bit01 bit02 bit03 bit10 bit11 bit12 bit13 bit20 bit21 bit22 bit23 bit30 bit31 bit32 bit33)(Q3 Q2 Q1 Q0)"
machine.burn("register", burn)