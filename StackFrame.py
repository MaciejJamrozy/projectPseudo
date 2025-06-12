from Variables import Variables
from PseudoExceptions import (
    throw_undefined_name_exception
    )

class StackFrame:
    def __init__(self, returnAddress = None, isRoot = False):
        self.localVariables = Variables()
        self.returnAddress: StackFrame = returnAddress
        self.isRoot = isRoot
    
    def check_var(self, var_id):
        if self.localVariables.check_var(var_id):
            return True
        elif not self.isRoot and self.returnAddress.check_var(var_id):
            return True
        else:
            return False
    
    def get_var(self, var_id):
        if self.localVariables.check_var(var_id):
            return self.localVariables.get_var(var_id)
        elif not self.isRoot and self.returnAddress.check_var(var_id):
            return self.returnAddress.get_var(var_id)
        
    def set_value(self, var_name, value):
        if self.localVariables.check_var(var_name):
            self.localVariables.set_value(var_name, value)
        elif not self.isRoot:
            self.returnAddress.set_value(var_name, value)
        else:
            throw_undefined_name_exception(-1,-1, var_name)
    
    def set_var(self, var_name, value, decl_line=None, type=None):
        self.localVariables.set_var(var_name, value, decl_line, type)

    def get_all_identifiers(self):
        if self.isRoot:
            return self.localVariables.get_all_names()
        else:
            return self.localVariables.get_all_names().union(self.returnAddress.get_all_identifiers())