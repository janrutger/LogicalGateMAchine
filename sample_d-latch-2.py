# SR AND-OR latch
import lgm as m
machine = m.LGM()

dlatch = "(x NOT R)(y OR S Q)(Q AND x y) Q"
machine.logic('dlatch', dlatch)


machine.dip('00', "(S R)")
print(machine.run('dlatch'))

machine.dip('10', "(S R)")
print(machine.run('dlatch'))
machine.dip('00', "(S R)")
print(machine.run('dlatch'))

machine.dip('01', "(S R)")
print(machine.run('dlatch'))
machine.dip('00', "(S R)")
print(machine.run('dlatch'))

machine.dip('11', "(S R)")
print(machine.run('dlatch'))
machine.dip('00', "(S R)")
print(machine.run('dlatch'))
