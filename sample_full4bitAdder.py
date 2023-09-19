import lgm as m


machine = m.LGM()

# each bit his own Logic gates
machine.dip('0', "(Co)")
machine.dip('1111', "(A3 A2 A1 A0)")
machine.dip('0011', "(B3 B2 B1 B0)")

bit0 = "(x XOR A0 B0)(z AND A0 B0)(S XOR x Co)(y AND x Co)(Co OR z y) Co S"
bit1 = "(x XOR A1 B1)(z AND A1 B1)(S XOR x Co)(y AND x Co)(Co OR z y) Co S"
bit2 = "(x XOR A2 B2)(z AND A2 B2)(S XOR x Co)(y AND x Co)(Co OR z y) Co S"
bit3 = "(x XOR A3 B3)(z AND A3 B3)(S XOR x Co)(y AND x Co)(Co OR z y) Co S"

machine.logic('bit0', bit0)
machine.logic('bit1', bit1) 
machine.logic('bit2', bit2)
machine.logic('bit3', bit3)  

machine.dip(machine.run('bit0'), "(Co S0)")  
machine.dip(machine.run('bit1'), "(Co S1)") 
machine.dip(machine.run('bit2'), "(Co S2)")  
machine.dip(machine.run('bit3'), "(Co S3)")  

print(machine.led("(Co S3 S2 S1 S0)"))

# 1x logic runs on alle bits
machine = m.LGM()

machine.dip('0', "(Co)")
machine.dip('0111', "(A3 A2 A1 A0)")
machine.dip('0011', "(B3 B2 B1 B0)")

bit0 = "(x XOR A B)(z AND A B)(S XOR x Cx)(y AND x Cx)(Co OR z y) Co S"
machine.logic('bit0', bit0)

machine.dip(machine.led("(A0 B0 Co)"), "(A B Cx)")
machine.dip(machine.run('bit0'), "(Co S0)")

machine.dip(machine.led("(A1 B1 Co)"), "(A B Cx)")
machine.dip(machine.run('bit0'), "(Co S1)")

machine.dip(machine.led("(A2 B2 Co)"), "(A B Cx)")
machine.dip(machine.run('bit0'), "(Co S2)")

machine.dip(machine.led("(A3 B3 Co)"), "(A B Cx)")
machine.dip(machine.run('bit0'), "(Co S3)")

print(machine.led("(Co S3 S2 S1 S0)"))

########## On chip runs 4 bits in once
machine = m.LGM()

bit0 = "(x XOR A B)(z AND A B)(S XOR x Cx)(y AND x Cx)(Co OR z y) Co S"
machine.logic('bit0', bit0)

chip = "[(A0 B0 Co), (A B Cx), bit0, (Co S0)], [(A1 B1 Co), (A B Cx), bit0, (Co S1)], [(A2 B2 Co), (A B Cx), bit0, (Co S2)], [(A3 B3 Co), (A B Cx), bit0, (Co S3)]"
machine.chip('chip1', chip)

machine.dip('0', "(Co)")
machine.dip('0011', "(A3 A2 A1 A0)")
machine.dip('0011', "(B3 B2 B1 B0)")

machine.run("chip1")

print(machine.led("(Co S3 S2 S1 S0)"))


########## 4bit full adder burned on a chip
machine = m.LGM()

bit0 = "(x XOR A B)(z AND A B)(S XOR x Cx)(y AND x Cx)(Co OR z y) Co S"
machine.logic('bit0', bit0)

chip = "[(A0 B0 Co), (A B Cx), bit0, (Co S0)], [(A1 B1 Co), (A B Cx), bit0, (Co S1)], [(A2 B2 Co), (A B Cx), bit0, (Co S2)], [(A3 B3 Co), (A B Cx), bit0, (Co S3)]"
machine.chip('chip1', chip)

burn = "(A3 A2 A1 A0)(B3 B2 B1 B0)(Co)(chip1)(Co S3 S2 S1 S0)"
machine.burn("burn", burn)

print(machine.run("burn", ("0101",'1010','0')))
print(machine.run("burn", ("0000",'0011','0')))
print(machine.run("burn", ("1111",'0001','0')))