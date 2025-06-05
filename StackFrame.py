from Variables import Variables
import copy

class StackFrame:
    def __init__(self, globalVariables: Variables = None, returnAddress = None):
        self.localVariables = Variables()
        self.globalVariables = globalVariables
        self.returnAddress = returnAddress

    def geniusCopy(self):
        newStackFrame = StackFrame(globalVariables=self.globalVariables)
        return newStackFrame
    
    def normalCopy(self):
        newStackFrame = StackFrame(globalVariables=self.globalVariables)
        newStackFrame.localVariables = copy.deepcopy(self.localVariables)
        return newStackFrame