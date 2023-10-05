
# 2 to 1 multiplexor (in logic)
import lgm as m
machine = m.LGM()

plexer = "(z NOT S)(y AND D1 S)(x AND D0 z)(O OR x y) O"
machine.logic('plexer', plexer)



machine.dip('10', "(D0 D1)")

# machine.dip('0', "(S)")
# print(machine.run('plexer'))

# machine.dip('1', "(S)")
# print(machine.run('plexer'))


# 4to1 Multiplexer (in chip)
import lgm as m
machine = m.LGM()

not1 = "(An NOT a) An"
and3 = "(z AND a b)(d AND z c) d"
or4  = "(z OR a b)(y OR c d)(r OR z y) r"

machine.logic('not1', not1)
machine.logic('and3', and3)
machine.logic('or4',  or4)

plexer0 = "[(A0), (a), not1, (A0n)], [(A1), (a), not1, (A1n)], [(Q00 A0n A1n), (a b c), and3, (y0)], [(Q10 A0 A1n), (a b c), and3, (y1)], [(Q20 A0n A1), (a b c), and3, (y2)], [(Q30 A0 A1), (a b c), and3, (y3)], [(y0 y1 y2 y3), (a b c d), or4, (E0)]"
plexer1 = "[(A0), (a), not1, (A0n)], [(A1), (a), not1, (A1n)], [(Q01 A0n A1n), (a b c), and3, (y0)], [(Q11 A0 A1n), (a b c), and3, (y1)], [(Q21 A0n A1), (a b c), and3, (y2)], [(Q31 A0 A1), (a b c), and3, (y3)], [(y0 y1 y2 y3), (a b c d), or4, (E1)]"
plexer2 = "[(A0), (a), not1, (A0n)], [(A1), (a), not1, (A1n)], [(Q02 A0n A1n), (a b c), and3, (y0)], [(Q12 A0 A1n), (a b c), and3, (y1)], [(Q22 A0n A1), (a b c), and3, (y2)], [(Q32 A0 A1), (a b c), and3, (y3)], [(y0 y1 y2 y3), (a b c d), or4, (E2)]"
plexer3 = "[(A0), (a), not1, (A0n)], [(A1), (a), not1, (A1n)], [(Q03 A0n A1n), (a b c), and3, (y0)], [(Q13 A0 A1n), (a b c), and3, (y1)], [(Q23 A0n A1), (a b c), and3, (y2)], [(Q33 A0 A1), (a b c), and3, (y3)], [(y0 y1 y2 y3), (a b c d), or4, (E3)]"


machine.chip('plexer0', plexer0)
machine.chip('plexer1', plexer1)
machine.chip('plexer2', plexer2)
machine.chip('plexer3', plexer3)

machine.dip('0011', "(Q30 Q20 Q10 Q00)")
machine.dip('10', "(A1 A0)")

machine.run('plexer0')

print(machine.led('(E0)'))



# 3 to 1 multiplexer

import lgm as m
machine = m.LGM()

plexer = "(z NOT S1)(y AND D1 S1)(x AND D0 z)(r OR x y)(z1 NOT S2)(y1 AND D2 S2)(x1 AND r z1)(O OR x1 y1) O"

machine.logic('plexer', plexer)

machine.dip('110', "(D0 D1 D2)")

# machine.dip('00', "(S2 S1)")
# print(machine.run('plexer'))

# machine.dip('01', "(S2 S1)")
# print(machine.run('plexer'))

# machine.dip('10', "(S2 S1)")
# print(machine.run('plexer'))






