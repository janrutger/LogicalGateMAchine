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
(machine.run("MEM", ("1111",'11','11')))
(machine.run("MEM", ("0000",'10','10')))
(machine.run("MEM", ("0011",'01','10')))
(machine.run("MEM", ("1111",'00','10')))


## set adrescounter to adres line
print(machine.run("adrescounter", ('0')))
## read first adres
(machine.run("memory", ('00')))
## write to register A
(machine.run("regA", ('10')))

## write next memory adres in register B
(machine.run("adrescounter", ('1')))
(machine.run("memory", ('00')))
(machine.run("regB", ('10')))

## perform alu operation
print(machine.run("alu", ('0101')))

    # Truth table
    # ---------------------
    # | S1 | S2 | An | Bn |
    # ---------------------
    # |  0 |  0 |  0 |  0 |   AND
    # |  1 |  0 |  0 |  0 |   OR
    # |  1 |  0 |  1 |  1 |   NAND
    # |  0 |  0 |  1 |  1 |   NOR 
    # |  x |  1 |  0 |  0 |   ADD 
    # |  x |  1 |  0 |  1 |   SUB
    # ---------------------
 
## Write result to register R
(machine.run("regR", ('10')))
## set adrescounter to 3 adres
(machine.run("adrescounter", ('1')))
# Set Register R to Datalines memory
#(machine.run("regR", ('00')))
# Write datalines to memory adres
(machine.run("memory", ('10')))


## Check result in memory
print(machine.run("MEM", ("1111",'00','00')))
print(machine.run("MEM", ("1111",'01','00')))
print(machine.run("MEM", ("1111",'10','00')))
print(machine.run("MEM", ("1111",'11','00')))




#print(machine.model())
pass