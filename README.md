# Logic Gate Machine
Welkom to the "hello World" page of this project

With this machine you can build logic circuits, using AND/OR/XOR and NOT gates and call them as an Python function.


## Demo

An simple example how to create an function with executes an 3 way AND gate circuit


## Usage/Examples

```python
import lgm as m
machine = m.LGM()

# define and activate the logic
and3 = "(z AND A B)(D AND z C) D"
machine.logic('and3', and3)

# To run it: Set the input values and run the logic
machine.dip('110', "(A B C)")
print(machine.run('and3'))

> 1

# After you defined and test the logic you can make a chip of one of more logic componentens
chip = "[(1 2 3), (A B C), and3, (4)]"
machine.chip('chip1', chip)

# To run it: Set the input values and run the chip
machine.dip('101', "(1 2 3)")
machine.run('chip1')
# and outputs the rsult
print(machine.led('(4)'))

> 0

# Now we have an working chip definition, we can
# glue the inputs and output pins to the chip
burn = "(1 2 3)(chip1)(4)"
machine.burn("CHIP", burn)

# Now the chip is ready ro run
print(machine.run("CHIP", ("101")))

> 0

print(machine.run("CHIP", ("111")))

> 1

print(machine.run("CHIP", ("011")))

> 0

```
## Whitout all extra test instructions
```python
import lgm as m
machine = m.LGM()

# define and activate the logic
and3 = "(z AND A B)(D AND z C) D"
machine.logic('and3', and3)

# After you defined and test the logic you can make a chip of one of more logic componentens
chip = "[(1 2 3), (A B C), and3, (4)]"
machine.chip('chip1', chip)

# Now we have an working chip definition, we can
# glue the inputs and output pins to the chip
burn = "(1 2 3)(chip1)(4)"
machine.burn("CHIP", burn)


# Now the chip is ready ro run
print(machine.run("CHIP", ("101")))

> 0

print(machine.run("CHIP", ("111")))

> 1

print(machine.run("CHIP", ("011")))

> 0

```
