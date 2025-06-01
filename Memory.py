class Memory:
    def __init__(self, name="global"):
        self.variables = {}
        self.name = name
        self.children = []
        self.parent = None
        self.level = 0

    def add_child(self, child):
        if self.level >= 20:
            raise Exception(
                "Memory level limit reached, cannot add more nested scopes."
            )
        child.parent = self
        self.children.append(child)
        child.level = self.level + 1

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        raise NameError(f"Child scope '{name}' not found")

    def set_value(self, var_name, value):
        if var_name in self.variables:
            self.variables[var_name]["value"] = value
        elif self.parent:
            self.parent.set_value(var_name, value)
        else:
            raise NameError(f"Variable '{var_name}' not found")

    def set_var(self, var_name, value, decl_line=None, type=None):
        self.variables[var_name] = {
            "value": value,
            "type": type if type is not None else "unknown",
            "decl_line": decl_line if decl_line is not None else -1,
        }

    def check_var(self, var_name):
        if var_name in self.variables:
            return True
        elif self.parent:
            return self.parent.check_var(var_name)
        else:
            return False

    def get_var(self, var_name):
        if var_name in self.variables:
            return self.variables[var_name]
        elif self.parent and  not self.name.startswith("function_scope"):
            return self.parent.get_var(var_name)
        else:
            raise NameError(f"Variable '{var_name}' not found")
        
