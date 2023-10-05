import lgm as m

machine = m.LGM()
multi = "(a AND A0 B1)(C0 AND A0 B0)(c AND A1 B0)(d AND A1 B1)(C1 XOR a c)(e AND a c)(C2 XOR e d)(C3 AND e d) C3 C2 C1 C0"
machine.logic('multi', multi)

machine.dip('10', "(A1 A0)")
machine.dip('11', "(B1 B0)")

print(machine.run('multi'))