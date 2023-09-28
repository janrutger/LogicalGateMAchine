# Logic Gate Machine
Welkom to the "Hello World" page of this project

With this class you can build logic circuits, using AND/OR/XOR and NOT gates and call them as an Python function.
Watch this serie for inspriration: https://www.youtube.com/watch?v=Pa9PEtLu7no&list=PL1C2GgOjAF-KY0zekzeMtFcYSlACDHyOK


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
machine.dip('111', "(A B C)")
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
## Without all extra test instructions
```python
import lgm as m
machine = m.LGM()

and3 = "(z AND A B)(D AND z C) D"
machine.logic('and3', and3)

chip = "[(1 2 3), (A B C), and3, (4)]"
machine.chip('chip1', chip)

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


## Example: 4bit full adder logic burned on a chip
```python
machine = m.LGM()

logic = "(x XOR A B)(z AND A B)(S XOR x Cx)(y AND x Cx)(Co OR z y) Co S"
machine.logic('bit0', logic)

chip = "[(A0 B0 Co), (A B Cx), bit0, (Co S0)], [(A1 B1 Co), (A B Cx), bit0, (Co S1)], [(A2 B2 Co), (A B Cx), bit0, (Co S2)], [(A3 B3 Co), (A B Cx), bit0, (Co S3)]"
machine.chip('adder', chip)

burn = "(A3 A2 A1 A0)(B3 B2 B1 B0)(Co)(adder)(Co S3 S2 S1 S0)"
machine.burn("CHIP", burn)

print(machine.run("CHIP", ("0101",'1010','0')))
print(machine.run("CHIP", ("0000",'0011','0')))
print(machine.run("CHIP", ("1111",'0001','0')))

```