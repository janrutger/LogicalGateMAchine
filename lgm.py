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
                if gate[2] not in self.allPins.keys():
                    self.allPins[gate[2]] = '0'
                if gate[1] != "NOT":
                    if gate[3] not in self.allPins.keys():
                        self.allPins[gate[3]] = '0'
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
            if isinstance(inputs, str):
                inputs = (inputs,) 
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
            if output not in self.allPins.keys():
                self.allPins[output] = '0'
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
    pass

if __name__ == '__main__':
    main()       