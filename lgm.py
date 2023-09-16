import copy

class LGM:
    def __init__(self):
        self.allLogic = {}
        self.allPins  = {}


    #{'LGC1': [('c', 'AND', 'a', 'b'), ('c',)], 'LGC2': [('c', 'AND', 'a', 'b'), ('x', 'NOT', 'c'), ('c',)]}
    def run(self, name):
        logic = copy.deepcopy(self.allLogic[name])
        outputs = logic.pop()
        for gate in logic:
            if gate[0] not in self.allPins.keys():
                self.allPins[gate[0]] = 0
            if gate[1] != "NOT":
                self.allPins[gate[0]] = str(self.gate(gate[1], int(self.allPins[gate[2]]), int(self.allPins[gate[3]])))
            else:
                self.allPins[gate[0]] = str(self.gate(gate[1], int(self.allPins[gate[2]])))
        result = ""
        for output in outputs:
            result = result + self.allPins[output]

        return (result)

    def dip(self, value, inputs):
        n = 0
        allInputs = inputs[1:-1].split(' ')
        for input in allInputs:
            self.allPins[input] = value[n]
            n = n + 1
    


    # "(c AND a b) c"
    # "(c AND a b)(x NOT c) c"
    def logic(self, name, schema):
        delen = schema.split(')')
        logicList = []
        for deel in delen:
            deel = deel[1:]
            items = deel.split(' ')
            logicItem = tuple(items)
            logicList.append(logicItem)
        self.allLogic[name] = logicList
    
    
    def gate(self, logic, a, b=None):
        if logic == "AND":
            return (a & b)
        
        if logic == "OR":
            return (a | b)
        
        if logic == "XOR":
            return (a ^ b)
        
        if logic == "NOT":
            if a == 1:
                return (0)
            else:
                return (1)




####################################################
def main():

    import lgm as m

    machine = m.LGM()
    schema1 = "(z AND a b)(y AND z c)(yy NOT y) y yy"
    machine.logic('LGC1', schema1)

    machine.dip('110', "(a b c)")

    print(machine.run('LGC1'))


    
    schema2 = "(x NOT A0)(y NOT A1)(D0 AND x y)(D1 AND A0 y)(D2 AND x A1)(D3 AND A0 A1) D0 D1 D2 D3"
    machine.logic('decoder', schema2)

    machine.dip('00', "(A0 A1)")
    print(machine.run('decoder'))

    machine.dip('10', "(A0 A1)")
    print(machine.run('decoder'))

    machine.dip('01', "(A0 A1)")
    print(machine.run('decoder'))

    machine.dip('11', "(A0 A1)")
    print(machine.run('decoder'))

    machine.dip(machine.run('LGC1'), "(A0 A1)")
    print(machine.run('decoder'))


####### ho to compose an chip ########################################
    # machine = m.LGM()

    # machine.dip('0', "(Ci)")
    # machine.dip('11', "(A0 A1)")
    # machine.dip('01', "(B0 B1)")
    # schema3 = "(x XOR A B)(z AND A B)(S XOR x Cx)(y AND x Cx)(Co OR z y) Co S"
    # machine.logic('fadder', schema3)

    #


if __name__ == '__main__':
    main()       