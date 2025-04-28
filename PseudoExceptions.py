def throw_unknown_operator_exception(line, col, op, type1, type2):
        raise Exception(f"Error in line: {line}, column: {col}: you can't use \'{op}\' operator between {type1} and {type2}.")

def throw_var_redeclaration_exception(line, col, var_name):
        raise Exception(f"Error in line: {line}, column: {col}: redeclaration of variable {var_name}.")

def throw_undefined_name_exception(line, col, var_name):
        raise Exception(f"Error in line: {line}, column: {col}: undefined name \'{var_name}\'.")

def throw_wrong_type_exception(line, col, var_type):
        raise Exception(f"Error in line: {line}, column: {col}: you can't assign this value to {var_type} type variable.")
