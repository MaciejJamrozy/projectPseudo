class Functions:
    def __init__(self):
        self.__functions = {}

    def set_fun(self, fun_name, return_type, params, body, decl_line=None):
        self.__functions[fun_name] = {
            "return_type": return_type,
            "params": params,
            "body": body,
            "decl_line": decl_line if decl_line is not None else -1
        }

    def get_fun(self, fun_name):
        if fun_name in self.__functions.keys():
            return self.__functions[fun_name]
        else:
            raise NameError(f"Function '{fun_name}' not found")
        
    def check_fun(self, fun_name):
        return (fun_name in self.__functions.keys())