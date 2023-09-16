class LGM:
    def __init__(self):
        self.allLogic = {}

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
    
        
        