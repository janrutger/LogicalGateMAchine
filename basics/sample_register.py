import lgm as m
machine = m.LGM()

reset = "(z NOT K)(Di AND z L) Di"
nand2 = "(z AND a b)(c NOT z) c"
machine.logic('nand2', nand2)
machine.logic('reset', reset)

dlatch0 = "[(Res D0), (K L), reset, (Di0)], [(Di0 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x Qn0), (a b), nand2, (Q0)], [(y Q0), (a b), nand2, (Qn0)], [(x Qn0), (a b), nand2, (Q0)], [(y Q0), (a b), nand2, (Qn0)]"    
dlatch1 = "[(Res D1), (K L), reset, (Di1)], [(Di1 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x Qn1), (a b), nand2, (Q1)], [(y Q1), (a b), nand2, (Qn1)], [(x Qn1), (a b), nand2, (Q1)], [(y Q1), (a b), nand2, (Qn1)]"      
dlatch2 = "[(Res D2), (K L), reset, (Di2)], [(Di2 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x Qn2), (a b), nand2, (Q2)], [(y Q2), (a b), nand2, (Qn2)], [(x Qn2), (a b), nand2, (Q2)], [(y Q2), (a b), nand2, (Qn2)]"       
dlatch3 = "[(Res D3), (K L), reset, (Di3)], [(Di3 E), (a b), nand2, (x)], [(E x), (a b), nand2, (y)], [(x Qn3), (a b), nand2, (Q3)], [(y Q3), (a b), nand2, (Qn3)], [(x Qn3), (a b), nand2, (Q3)], [(y Q3), (a b), nand2, (Qn3)]"        

machine.chip('dlatch0', dlatch0)
machine.chip('dlatch1', dlatch1)
machine.chip('dlatch2', dlatch2)
machine.chip('dlatch3', dlatch3)


burn  = "(D3 D2 D1 D0)(E Res)(dlatch0 dlatch1 dlatch2 dlatch3)(Q3 Q2 Q1 Q0)"
machine.burn("register", burn)

print(machine.run("register", ("0000",'00')))
print(machine.run("register", ("0000",'00')))
print(machine.run("register", ("1010",'11')))
print(machine.run("register", ("1010",'10')))
print(machine.run("register", ("0101",'00')))

print(machine.run("register", ("0101",'10')))
print(machine.run("register", ("1010",'00')))

print(machine.run("register", ("1111",'11')))
print(machine.run("register", ("1010",'00')))

