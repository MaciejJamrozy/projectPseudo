def throw_unsupported_operator_exception(line, col, op, type1, type2):
    raise Exception(
        f"Error in line: {line}, column: {col}: you can't use '{op}' operator between {type1} and {type2}."
    )


def throw_var_redeclaration_exception(line, col, var_name, decl_line):
    raise Exception(
        f"Error in line: {line}, column: {col}: redeclaration of variable {var_name}, you have declared it at line {decl_line}."
    )


def throw_undefined_name_exception(line, col, var_name):
    raise Exception(
        f"Error in line: {line}, column: {col}: undefined name '{var_name}'."
    )


def throw_wrong_type_exception(line, col, var_type):
    raise Exception(
        f"Error in line: {line}, column: {col}: you can't assign this value to {var_type} type variable."
    )


def throw_non_defined_function_exception(line, col, fun_name):
    raise Exception(
        f"Error in line: {line}, column: {col}: function {fun_name} is non-defined."
    )


def throw_redeclaration_in_function_def_exception(line, col, name, line_defined):
    raise Exception(
        f"Error in line: {line}, column: {col}: you can't have two arguments with the same name ({name}), in function definition."
    )


def throw_function_redeclaration_exception(line, col, name, decl_line):
    raise Exception(
        f"Error in line: {line}, column: {col}: Redeclaration of function \'{name}\'. It was declared at line {decl_line}."
    )


def throw_unknown_operator_exception(line, col, op):
    raise Exception(f'Error in line: {line}, column: {col}: unkown operator "{op}".')


def throw_conversion_exception(line, col, type, value):
    raise Exception(
        f"Error in line: {line}, column: {col}: cannot convert {value} to {type}."
    )

def throw_no_parent_scope_exception(line, col):
    raise Exception(f'Error in line: {line}, column: {col}: there is no superior scope.')