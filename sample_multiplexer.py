
# 2 to 1 multiplexor
import lgm as m
machine = m.LGM()

plexer = "(z NOT S)(y AND D1 S)(x AND D0 z)(O OR x y) O"
machine.logic('plexer', plexer)



machine.dip('10', "(D0 D1)")

machine.dip('0', "(S)")
print(machine.run('plexer'))

machine.dip('1', "(S)")
print(machine.run('plexer'))

# 3 to 1 multiplexer

import lgm as m
machine = m.LGM()

plexer = "(z NOT S1)(y AND D1 S1)(x AND D0 z)(r OR x y)(z1 NOT S2)(y1 AND D2 S1)(x1 AND r z1)(O OR x y) O"

machine.logic('plexer', plexer)

machine.dip('101', "(D0 D1 D2)")

machine.dip('00', "(S2 S1)")
print(machine.run('plexer'))

machine.dip('01', "(S2 S1)")
print(machine.run('plexer'))

machine.dip('10', "(S2 S1)")
print(machine.run('plexer'))




