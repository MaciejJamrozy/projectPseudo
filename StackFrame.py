from Variables import Variables

class StackFrame:
    def __init__(self, globalVariables: Variables = None, returnAddress = None):
        self.localVariables = Variables()
        self.globalVariables = globalVariables
        self.returnAddress = returnAddress

    def geniusCopy(self):
        newStackFrame = StackFrame(globalVariables=self.globalVariables)
        return newStackFrame