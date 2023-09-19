import copy
import re

class LGM:
    def __init__(self):
        self.allLogic = {}
        self.allPins  = {}
        self.allChips = {}
        self.allBurnt = {}


    #{'LGC1': [('c', 'AND', 'a', 'b'), ('c',)], 'LGC2': [('c', 'AND', 'a', 'b'), ('x', 'NOT', 'c'), ('c',)]}
    def run(self, name, inputs=None):
        if name in self.allLogic.keys():
            logic = copy.deepcopy(self.allLogic[name])
            outputs = logic.pop()
            for gate in logic:
                if gate[1] != "NOT":
                    self.allPins[gate[0]] = str(self.gate(gate[1], int(self.allPins[gate[2]]), int(self.allPins[gate[3]])))
                else:
                    self.allPins[gate[0]] = str(self.gate(gate[1], int(self.allPins[gate[2]])))
            result = ""
            for output in outputs:
                result = result + self.allPins[output]
            return (result)
        elif name in self.allChips.keys():
            chip = copy.deepcopy(self.allChips[name])
            for logic in chip:
                self.dip(self.led(logic[0]), logic[1])
                self.dip(self.run(logic[2]), logic[3])
        elif name in self.allBurnt.keys() and inputs != None:
            burn = copy.deepcopy(self.allBurnt[name])
            outputs = (burn.pop())
            chips = burn.pop().strip('()').split(' ')
            n = 0
            for pinList in burn:
                self.dip(inputs[n], pinList)
                n = n + 1
            for chip in chips:
                self.run(chip)
            self.led(outputs)            
            return(self.led(outputs))
        else:
            return("Unkown or Invalid")

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
    
    def burn(self, name, schema):
        parts = re.findall(r'\([^)]*\)', schema)
        self.allBurnt[name] = parts
    

    def chip(self, name, schema):
        parts = schema.strip('[]').split('], [')
        logicList = []
        for part in parts:
            components = part.split(', ')
            logicList.append(components)
        self.allChips[name] = logicList


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

########## Burn a chip
    machine = m.LGM()

    bit0 = "(x XOR A B)(z AND A B)(S XOR x Cx)(y AND x Cx)(Co OR z y) Co S"
    machine.logic('bit0', bit0)

    chip = "[(A0 B0 Co), (A B Cx), bit0, (Co S0)], [(A1 B1 Co), (A B Cx), bit0, (Co S1)], [(A2 B2 Co), (A B Cx), bit0, (Co S2)], [(A3 B3 Co), (A B Cx), bit0, (Co S3)]"
    machine.chip('chip1', chip)

    burn = "(A3 A2 A1 A0)(B3 B2 B1 B0)(Co)(chip1)(Co S3 S2 S1 S0)"
    machine.burn("burn", burn)

    print(machine.run("burn", ("0101",'1010','0')))
    print(machine.run("burn", ("0000",'0011','0')))
    print(machine.run("burn", ("1111",'0001','0')))


    machine = m.LGM()
    and3 = "(z AND A B)(y AND z C) y"
    machine.logic('and3', and3)

    machine.dip('111', "(A B C)")

    print(machine.run('and3'))

# ############# decoder logic
    
#     decoder = "(x NOT A0)(y NOT A1)(D0 AND x y)(D1 AND A0 y)(D2 AND x A1)(D3 AND A0 A1) D0 D1 D2 D3"
#     machine.logic('decoder', decoder)

#     machine.dip('00', "(A0 A1)")
#     print(machine.run('decoder'))

#     machine.dip('10', "(A0 A1)")
#     print(machine.run('decoder'))

#     machine.dip('01', "(A0 A1)")
#     print(machine.run('decoder'))

#     machine.dip('11', "(A0 A1)")
#     print(machine.run('decoder'))




# ####### how to compose full adder 4 bits ########################################
#     machine = m.LGM()

#     machine.dip('0', "(Co)")
#     machine.dip('1111', "(A3 A2 A1 A0)")
#     machine.dip('0011', "(B3 B2 B1 B0)")

#     bit0 = "(x XOR A0 B0)(z AND A0 B0)(S XOR x Co)(y AND x Co)(Co OR z y) Co S"
#     bit1 = "(x XOR A1 B1)(z AND A1 B1)(S XOR x Co)(y AND x Co)(Co OR z y) Co S"
#     bit2 = "(x XOR A2 B2)(z AND A2 B2)(S XOR x Co)(y AND x Co)(Co OR z y) Co S"
#     bit3 = "(x XOR A3 B3)(z AND A3 B3)(S XOR x Co)(y AND x Co)(Co OR z y) Co S"

#     machine.logic('bit0', bit0)
#     machine.logic('bit1', bit1) 
#     machine.logic('bit2', bit2)
#     machine.logic('bit3', bit3)  
    
#     machine.dip(machine.run('bit0'), "(Co S0)")  
#     machine.dip(machine.run('bit1'), "(Co S1)") 
#     machine.dip(machine.run('bit2'), "(Co S2)")  
#     machine.dip(machine.run('bit3'), "(Co S3)")  

#     print(machine.led("(Co S3 S2 S1 S0)"))


#     ####### how to compose full adder 4 bits ########################################
#     machine = m.LGM()

#     machine.dip('0', "(Co)")
#     machine.dip('0111', "(A3 A2 A1 A0)")
#     machine.dip('0011', "(B3 B2 B1 B0)")

#     bit0 = "(x XOR A B)(z AND A B)(S XOR x Cx)(y AND x Cx)(Co OR z y) Co S"
#     machine.logic('bit0', bit0)

#     machine.dip(machine.led("(A0 B0 Co)"), "(A B Cx)")
#     machine.dip(machine.run('bit0'), "(Co S0)")

#     machine.dip(machine.led("(A1 B1 Co)"), "(A B Cx)")
#     machine.dip(machine.run('bit0'), "(Co S1)")

#     machine.dip(machine.led("(A2 B2 Co)"), "(A B Cx)")
#     machine.dip(machine.run('bit0'), "(Co S2)")

#     machine.dip(machine.led("(A3 B3 Co)"), "(A B Cx)")
#     machine.dip(machine.run('bit0'), "(Co S3)")

#     print(machine.led("(Co S3 S2 S1 S0)"))

# ########## On chip
#     machine = m.LGM()

#     bit0 = "(x XOR A B)(z AND A B)(S XOR x Cx)(y AND x Cx)(Co OR z y) Co S"
#     machine.logic('bit0', bit0)

#     chip = "[(A0 B0 Co), (A B Cx), bit0, (Co S0)], [(A1 B1 Co), (A B Cx), bit0, (Co S1)], [(A2 B2 Co), (A B Cx), bit0, (Co S2)], [(A3 B3 Co), (A B Cx), bit0, (Co S3)]"
#     machine.chip('chip1', chip)

#     machine.dip('0', "(Co)")
#     machine.dip('0011', "(A3 A2 A1 A0)")
#     machine.dip('0011', "(B3 B2 B1 B0)")

#     machine.run("chip1")

#     print(machine.led("(Co S3 S2 S1 S0)"))


# ##### first chip example ####################################
#     machine = m.LGM()
#     and2 = "(c AND a b) c"
#     machine.logic('and2', and2)

#     machine.dip('110', "(A B C)")

#     machine.dip(machine.led("(A B)"), "(a b)")
#     machine.dip(machine.run('and2'), "(d)")
#     machine.dip(machine.led("(d C)"), "(a b)")
#     machine.dip(machine.run('and2'), "(D)")

#     print(machine.led("(D)"))

# ### chip starts here, same logic 
#     machine = m.LGM()
#     and2 = "(c AND a b) c"
#     machine.logic('and2', and2)

#     and3 = "[(A B), (a b), and2, (d)], [(d C), (a b), and2, (D)]"
#     machine.chip('and3', and3)

#     machine.dip('111', "(A B C)") 
#     machine.run('and3')
#     print(machine.led("(D)"))
#     print(machine.allChips)

# ######### Multiplier 2 bit
#     machine = m.LGM()
#     multi = "(a AND A0 B1)(C0 AND A0 B0)(c AND A1 B0)(d AND A1 B1)(C1 XOR a c)(e AND a c)(C2 XOR e d)(C3 AND e d) C3 C2 C1 C0"
#     machine.logic('multi', multi)

#     machine.dip('10', "(A1 A0)")
#     machine.dip('11', "(B1 B0)")

#     print(machine.run('multi'))


    
    


if __name__ == '__main__':
    main()       