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


## init memory, 
print(machine.run("MEM", ("0101",'00','10')))
print(machine.run("MEM", ("1010",'01','10')))
print(machine.run("MEM", ("1111",'10','10')))
print(machine.run("MEM", ("0000",'11','10')))



## set adres counter to first adres
print(machine.run("adrescounter", ('1')))
## read first adres
print(machine.run("memory", ('00')))
## write to register A
print(machine.run("regA", ('10')))

## write next memory adres in register B
print(machine.run("adrescounter", ('1')))
print(machine.run("adrescounter", ('1')))
print(machine.run("memory", ('00')))
print(machine.run("regB", ('10')))




print(machine.model())