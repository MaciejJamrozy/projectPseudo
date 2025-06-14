class Variables:
    def __init__(self):
        self.__localVariables = {}
    
    def set_value(self, var_name, value):
        if var_name in self.__localVariables:
            self.__localVariables[var_name]["value"] = value
        else:
            raise NameError(f"Variable '{var_name}' not found")

    def set_var(self, var_name, value, decl_line=None, type=None, decl_column=None):
        self.__localVariables[var_name] = {
            "value": value,
            "type": type if type is not None else "unknown",
            "decl_line": decl_line if decl_line is not None else -1,
            "decl_column": decl_column if decl_column is not None else -1
        }

    def check_var(self, var_name):
        if var_name in self.__localVariables:
            return True
        else:
            return False

    def get_var(self, var_name):
        if var_name in self.__localVariables:
            return self.__localVariables[var_name]
        else:
            raise NameError(f"Variable '{var_name}' not found")
        
    def del_var(self, var_name):
        if var_name in self.__localVariables:
            self.__localVariables.pop(var_name)

    def get_all_names(self) -> set:
        return set(self.__localVariables.keys())