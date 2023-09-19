import lgm as m

machine = m.LGM()
and3 = "(z AND A B)(y AND z C) y"
machine.logic('and3', and3)

machine.dip('111', "(A B C)")

print(machine.run('and3'))