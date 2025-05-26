import copy

class Memory:
    def __init__(self):
        self.variables = {}
        self.functions = {}
    
    def __deepcopy__(self, memo):
        copied = Memory()
        copied.functions = self.functions
        return copied
