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
            # if gate[0] not in self.allPins.keys():
            #     self.allPins[gate[0]] = 0
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

    def led(self, outputs):
        result = ""
        allOutputs = outputs[1:-1].split(' ')
        for output in allOutputs:
            result = result + self.allPins[output]
        return (result)
    


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
    machine.logic('LGM1', schema1)

    machine.dip('110', "(a b c)")

    print(machine.run('LGM1'))

############# decoder logic
    
    decoder = "(x NOT A0)(y NOT A1)(D0 AND x y)(D1 AND A0 y)(D2 AND x A1)(D3 AND A0 A1) D0 D1 D2 D3"
    machine.logic('decoder', decoder)

    machine.dip('00', "(A0 A1)")
    print(machine.run('decoder'))

    machine.dip('10', "(A0 A1)")
    print(machine.run('decoder'))

    machine.dip('01', "(A0 A1)")
    print(machine.run('decoder'))

    machine.dip('11', "(A0 A1)")
    print(machine.run('decoder'))




####### how to compose full adder 4 bits ########################################
    machine = m.LGM()

    machine.dip('0', "(Co)")
    machine.dip('1111', "(A3 A2 A1 A0)")
    machine.dip('0011', "(B3 B2 B1 B0)")

    bit0 = "(x XOR A0 B0)(z AND A0 B0)(S XOR x Co)(y AND x Co)(Co OR z y) Co S"
    bit1 = "(x XOR A1 B1)(z AND A1 B1)(S XOR x Co)(y AND x Co)(Co OR z y) Co S"
    bit2 = "(x XOR A2 B2)(z AND A2 B2)(S XOR x Co)(y AND x Co)(Co OR z y) Co S"
    bit3 = "(x XOR A3 B3)(z AND A3 B3)(S XOR x Co)(y AND x Co)(Co OR z y) Co S"

    machine.logic('bit0', bit0)
    machine.logic('bit1', bit1) 
    machine.logic('bit2', bit2)
    machine.logic('bit3', bit3)  
    
    machine.dip(machine.run('bit0'), "(Co S0)")  
    machine.dip(machine.run('bit1'), "(Co S1)") 
    machine.dip(machine.run('bit2'), "(Co S2)")  
    machine.dip(machine.run('bit3'), "(Co S3)")  

    print(machine.led("(Co S3 S2 S1 S0)"))


    ####### how to compose full adder 4 bits ########################################
    machine = m.LGM()

    machine.dip('0', "(Co)")
    machine.dip('0111', "(A3 A2 A1 A0)")
    machine.dip('0011', "(B3 B2 B1 B0)")

    bit0 = "(x XOR A B)(z AND A B)(S XOR x Cx)(y AND x Cx)(Co OR z y) Co S"
    machine.logic('bit0', bit0)

    machine.dip(machine.led("(A0 B0 Co)"), "(A B Cx)")
    machine.dip(machine.run('bit0'), "(Co S0)")

    machine.dip(machine.led("(A1 B1 Co)"), "(A B Cx)")
    machine.dip(machine.run('bit0'), "(Co S1)")

    machine.dip(machine.led("(A2 B2 Co)"), "(A B Cx)")
    machine.dip(machine.run('bit0'), "(Co S2)")

    machine.dip(machine.led("(A3 B3 Co)"), "(A B Cx)")
    machine.dip(machine.run('bit0'), "(Co S3)")

    print(machine.led("(Co S3 S2 S1 S0)"))



if __name__ == '__main__':
    main()       