import difflib

def throw_unsupported_operator_exception(line, col, op, type1, type2):
    raise Exception(
        f"Error in line: {line}, column: {col}: you can't use '{op}' operator between {type1} and {type2}."
    )


def throw_var_redeclaration_exception(line, col, var_name, decl_line):
    raise Exception(
        f"Error in line: {line}, column: {col}: redeclaration of variable {var_name}, you have declared it at line {decl_line}."
    )


def throw_undefined_name_exception(line, col, var_name, known_names=set()):
    suggestion = difflib.get_close_matches(var_name, known_names, n=1, cutoff=0.25)
    if suggestion:
        msg = f"Error in line: {line}, column: {col}: undefined name '{var_name}'. Did you mean '{suggestion[0]}'?"
    else:
        msg = f"Error in line: {line}, column: {col}: undefined name '{var_name}'."
    raise Exception(msg)


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


def throw_wrong_parameters_number_exception(line, col, fun_name, given, take):
    take_tailored_string = 'parameter' if take == 1 else 'parameters'
    given_tailored_string = 'was' if given == 1 else 'were'
    raise Exception(f'Error in line: {line}, column: {col}: function \'{fun_name}\' takes {take} {take_tailored_string}, but {given} {given_tailored_string} given.')


def throw_fun_def_in_block_exception(line, col):
    raise Exception(f'Error in line: {line}, column: {col}: functions cannot be declared inside blocks, if-else blocks or loops.')