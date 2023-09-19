# Logic Gate Machine
Welkom to the "hello World" page of this project

With this machine you can build logic circuits, using AND/OR/XOR and NOT gates and call them as an Python function.


## Demo

An simple example how to create an 3 way AND gate


## Usage/Examples

```python
import lgm as m
machine = m.LGM()

# define and activate the logic

and3 = "(z AND A B)(y AND z C) y"
machine.logic('and3', and3)

# To run it: Set the input values and run the logic
machine.dip('111', "(A B C)"
print(machine.run('and3'))

> 1

# After you defined and test the logic you can make a chip of one of more logic componentens
chip = "[(1 2 3), (a b c), and2, (d)], (4)]"
machine.chip('chip1', chip)

# To run it: Set the input values and run the chip
machine.dip('111', "(1 2 3)"
machine.run('chip1')
print(machine.led('4'))

> 1

# Now we have an working chip definition
# and glue the inputs and output pins to the chip
burn = "(1 2 3)(chip1)(4)"
machine.burn("CHIP", burn)

# Now the chip is ready ro run
print(machine.run("CHIP", ("101")))

> 0

print(machine.run("CHIP", ("111")))

> 1

```
