import config
import difflib

def throw_unsupported_operator_exception(line, col, op, type1, type2):
    surr_info = get_error_surroundings_information(line, col)
    raise Exception(
        f"\033[31mError in line: {line}, column: {col}:\033[0m you can't use '{op}' operator between {type1} and {type2}.{surr_info}"
    )


def throw_var_redeclaration_exception(line, col, var_name, decl_line):
    surr_info = get_error_surroundings_information(line, col)
    raise Exception(
        f"\033[31mError in line: {line}, column: {col}:\033[0m redeclaration of variable {var_name}, you have declared it at line {decl_line}.{surr_info}"
    )


def throw_undefined_name_exception(line, col, var_name, known_names=set()):
    surr_info = get_error_surroundings_information(line, col)
    suggestion = difflib.get_close_matches(var_name, known_names, n=1, cutoff=0.25)
    if suggestion:
        msg = f"\033[31mError in line: {line}, column: {col}:\033[0m undefined name '{var_name}'. Did you mean '{suggestion[0]}'?{surr_info}"
    else:
        msg = f"\033[31mError in line: {line}, column: {col}:\033[0m undefined name '{var_name}'.{surr_info}"
    raise Exception(msg)


def throw_wrong_type_exception(line, col, var_type):
    surr_info = get_error_surroundings_information(line, col)
    raise Exception(
        f"\033[31mError in line: {line}, column: {col}:\033[0m you can't assign this value to {var_type} type variable.{surr_info}"
    )


def throw_non_defined_function_exception(line, col, fun_name):
    surr_info = get_error_surroundings_information(line, col)
    raise Exception(
        f"\033[31mError in line: {line}, column: {col}:\033[0m function {fun_name} is non-defined.{surr_info}"
    )


def throw_redeclaration_in_function_def_exception(line, col, name, decl_column):
    surr_info = get_error_surroundings_information(line, col)
    raise Exception(
        f"\033[31mError in line: {line}, column: {col}:\033[0m argument \'{name}\' was already declared at column {decl_column}, in this function definition.{surr_info}"
    )


def throw_function_redeclaration_exception(line, col, name, decl_line):
    surr_info = get_error_surroundings_information(line, col)
    raise Exception(
        f"\033[31mError in line: {line}, column: {col}:\033[0m Redeclaration of function \'{name}\'. It was declared at line {decl_line}.{surr_info}"
    )


def throw_unknown_operator_exception(line, col, op):
    surr_info = get_error_surroundings_information(line, col)
    raise Exception(f'\033[31mError in line: {line}, column: {col}:\033[0m unkown operator "{op}".{surr_info}')


def throw_conversion_exception(line, col, type, value):
    surr_info = get_error_surroundings_information(line, col)
    raise Exception(
        f"\033[31mError in line: {line}, column: {col}:\033[0m cannot convert {value} to {type}.{surr_info}"
    )

def throw_no_parent_scope_exception(line, col):
    surr_info = get_error_surroundings_information(line, col)
    raise Exception(f'\033[31mError in line: {line}, column: {col}:\033[0m there is no superior scope.{surr_info}')


def throw_wrong_parameters_number_exception(line, col, fun_name, given, take):
    surr_info = get_error_surroundings_information(line, col)
    take_tailored_string = 'parameter' if take == 1 else 'parameters'
    given_tailored_string = 'was' if given == 1 else 'were'
    raise Exception(f'\033[31mError in line: {line}, column: {col}:\033[0m function \'{fun_name}\' takes {take} {take_tailored_string}, but {given} {given_tailored_string} given.{surr_info}')


def throw_fun_def_in_block_exception(line, col):
    surr_info = get_error_surroundings_information(line, col)
    raise Exception(f'\033[31mError in line: {line}, column: {col}:\033[0m functions cannot be declared inside blocks, if-else blocks or loops.{surr_info}')


def throw_wrong_parameter_typw_exception(line, col, f_def_line, f_par_col, exp_type, given_type):
    surr_info_1 = get_error_surroundings_information(f_def_line, f_par_col)
    surr_info_2 = get_error_surroundings_information(line, col)
    raise Exception(f'\033[31mError in line: {line}, column: {col}:\033[0m \'{given_type}\' doesn\'t match with \'{exp_type}\' type.{surr_info_1}{surr_info_2}')


def throw_dividing_by_zero_exception(line, col):
    surr_info = get_error_surroundings_information(line, col)
    raise Exception(f'\033[31mError in line: {line}, column: {col}:\033[0m cannot divide by zero.{surr_info}')


def throw_function_doesnt_return_exception(line, col):
    surr_info = get_error_surroundings_information(line, col)
    raise Exception(f'\033[31mError in line: {line}, column: {col}:\033[0m function doesn\'t return value, but it should.{surr_info}')


def throw_void_function_returns_exception(line, col):
    surr_info = get_error_surroundings_information(line, col)
    raise Exception(f'\033[31mError in line: {line}, column: {col}:\033[0m void functions cannot return values.{surr_info}')


def throw_function_returns_types_dont_match_exception(line, col):
    surr_info = get_error_surroundings_information(line, col)
    raise Exception(f'\033[31mError in line: {line}, column: {col}:\033[0m returned value doesn\'t match with declared in function.{surr_info}')


def throw_bool_op_with_another_type_exception(line, col):
    surr_info = get_error_surroundings_information(line, col)
    raise Exception(f'\033[31mError in line: {line}, column: {col}:\033[0m this value is not boolean.{surr_info}')


def get_error_surroundings_information(line, col):
    source_file_name = config.source_file_name

    if source_file_name:
        with open(source_file_name) as f:
            for i, line_f in enumerate(f, start=1):
                if i == line:
                    return f'\n\n{line_f.rstrip()}\n\033[{col+1}G\033[31m^\033[0m'
    else:
        return ""