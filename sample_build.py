import lgm as m
machine = m.LGM()

from basics import Memory
from basics import ALU
from basics import Adrescounter
from basics import RegisterA
from basics import RegisterB
from basics import RegisterR

Memory.load(machine)
ALU.load(machine)
Adrescounter.load(machine)
RegisterA.load(machine)
RegisterB.load(machine)
RegisterR.load(machine)




print(machine.model())