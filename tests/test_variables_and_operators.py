from antlr4 import InputStream
from PseudoInterpreter import run_interpreter
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_variable_declaration_and_assignment(capsys):
    code = """
    int x = 5;
    print(x);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == "5"

def test_string_assignment_to_int_variable(capsys):
    code = """
    int a = 5;

    a = '5';
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().lower()
    assert 'error' in captured

def test_int_assignment_to_string_variable(capsys):
    code = """
    string a = 's';

    a = 5;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().lower()
    assert 'error' in captured

def test_boolean_assignment_to_int_variable(capsys):
    code = """
    int a = 5;

    a = True;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().lower()
    assert 'error' in captured

def test_boolean_assignment_to_string_variable(capsys):
    code = """
    string a = 'a';

    a = True;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().lower()
    assert 'error' in captured

def test_variable_reassignment(capsys):
    code = """
    int x = 5;
    x = 10;
    print(x);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == "10"


def test_variable_scope(capsys):
    code = """
    int x = 1;
    function int test():
        int x = 2;
        print(x);
        return x;
    end;

    test();
    print(x);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip().splitlines() == ["2", "1"]


def test_type_mismatch_error(capsys):
    code = """
    int x = 5;
    x = "hello";
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    output = capsys.readouterr().out.strip()
    assert "error" in output.lower()


def test_undefined_variable(capsys):
    code = """
    print(y);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    output = capsys.readouterr().out.strip()
    assert "error" in output.lower()


def test_declaration_then_assignment(capsys):
    code = """
    int x;
    x = 42;
    print(x);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == "42"


def test_declaration_without_assignment_then_use(capsys):
    code = """
    int x;
    print(x);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    output = capsys.readouterr().out.strip()
    assert output == "None"


def test_int_to_float_conversion(capsys):
    code = """
    float x;
    x = float(2);
    print(x);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == "2.0"


def test_float_to_int_conversion(capsys):
    code = """
    int x;
    x = int(2.9);
    print(x);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == "2"


def test_int_to_string_conversion(capsys):
    code = """
    string x;
    x = string(42);
    print(x);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == "42"


def test_float_to_string_conversion(capsys):
    code = """
    string x;
    x = string(3.14);
    print(x);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == "3.14"


def test_boolean_to_string_conversion(capsys):
    code = """
    string x;
    x = string(True);
    print(x);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == "True"


def test_invalid_cast(capsys):
    code = """
    int x;
    x = int("hello");
    print(x);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    output = capsys.readouterr().out.strip().lower()
    assert "error" in output.lower()


def test_arithmetic_operators(capsys):
    code = """
    int a = 10;
    int b = 3;
    print(a + b);
    print(a - b);
    print(a * b);
    print(a /# b);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["13", "7", "30", "3"]


def test_logical_operators(capsys):
    code = """
    boolean x = True;
    boolean y = False;
    print(x and y);
    print(x or y);
    print(not x);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["False", "True", "False"]


def test_comparison_operators(capsys):
    code = """
    int a = 5;
    int b = 10;
    print(a == b);
    print(a != b);
    print(a < b);
    print(a > b);
    print(a <= b);
    print(a >= b);
    int c = 5;
    print(a == c);
    print(a <= c);
    print(a >= c);
    print(a < c);
    print(a > c);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["False", "True", "True", "False", "True", "False","True", "True", "True", "False", "False"]

def test_negative_integer_assignment(capsys):
    code = """
    int x = -10;
    print(x);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["-10"]


def test_negative_in_condition(capsys):
    code = """
    int x = -5;
    if x < 0:
        print("negative");
    end;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["negative"]


def test_negative_in_arithmetic(capsys):
    code = """
    int x = 5;
    int y = -2;
    int z = x + y;
    print(z);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["3"]


def test_negative_float_assignment(capsys):
    code = """
    float x = -3.14;
    print(x);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["-3.14"]


def test_negative_float_arithmetic(capsys):
    code = """
    float a = -2.5;
    float b = 1.5;
    float c = a + b;
    print(c);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["-1.0"]


def test_negative_float_condition(capsys):
    code = """
    float temp = -0.5;
    if temp < 0:
        print("cold");
    end;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["cold"]


def test_proper_var_decl_order(capsys):
    code = """
    print(y);

    int y = 11;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    output = capsys.readouterr().out.strip().lower()
    assert "undefined" in output.lower()

def test_global_variable_declaration_and_assignment(capsys):
    code = """
    global int x = 5;

    print(x);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == "5"

# def test_global_variable_declaration_and_assignment(capsys):
#     code = """
#     global int x = 5;

#     int x = 6;
#     """
#     input_stream = InputStream(code)
#     run_interpreter(inputStream=input_stream)
#     captured = capsys.readouterr().out.lower()
#     assert 'redeclaration' in captured

def test_global_variable_used_inside_function(capsys):
    code = """
    global int x = 5;

    function void foo():
        print(x);
    end;
    
    foo();
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == "5"