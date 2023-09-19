Welcome to the Hello World page of my Logic Gate Machine.
With this machine you can build logic circuits with AND/OR/XOR/NOT gates and call them as a Python function.

A simple example:

import the module and create a machine

    import lgm as m
    machine = m.LGM()

Define and activate the logic for a 3 input AND circuit
    and3 = "(z AND A B)(y AND z C) y"
    machine.logic('and3', and3)

to test the logic now you have to create the INPUT signals
    machine.dip('111', "(A B C)"

and execute the logic
    print(machine.run('and3'))