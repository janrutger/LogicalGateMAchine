import lgm as m

machine = m.LGM()

decoder = "(x NOT A0)(y NOT A1)(D0 AND x y)(D1 AND A0 y)(D2 AND x A1)(D3 AND A0 A1) D0 D1 D2 D3"
machine.logic('decoder', decoder)

machine.dip('00', "(A0 A1)")
print(machine.run('decoder'))

machine.dip('10', "(A0 A1)")
print(machine.run('decoder'))

machine.dip('01', "(A0 A1)")
print(machine.run('decoder'))

machine.dip('11', "(A0 A1)")
print(machine.run('decoder'))