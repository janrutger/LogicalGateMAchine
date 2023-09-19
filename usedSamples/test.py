# ########## Burn a chip
     machine = m.LGM()

     bit0 = "(x XOR A B)(z AND A B)(S XOR x Cx)(y AND x Cx)(Co OR z y) Co S"
     machine.logic('bit0', bit0)

    chip = "[(A0 B0 Co), (A B Cx), bit0, (Co S0)], [(A1 B1 Co), (A B Cx), bit0, (Co S1)], [(A2 B2 Co), (A B Cx), bit0, (Co S2)], [(A3 B3 Co), (A B Cx), bit0, (Co S3)]"
    machine.chip('chip1', chip)

#     burn = "(A3 A2 A1 A0)(B3 B2 B1 B0)(Co)(chip1)(Co S3 S2 S1 S0)"
#     machine.burn("burn", burn)

#     print(machine.run("burn", ("0101",'1010','0')))
#     print(machine.run("burn", ("0000",'0011','0')))
#     print(machine.run("burn", ("1111",'0001','0')))


#     machine = m.LGM()
#     and3 = "(z AND A B)(y AND z C) y"
#     machine.logic('and3', and3)

#     machine.dip('111', "(A B C)")

#     print(machine.run('and3'))