from antlr4 import InputStream
from io import StringIO
import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from PseudoInterpreter import run_interpreter

def test_global_int_assignment_valid(capsys):
    code = """
    global int ala = 0;
    ala = 42;
    print(ala);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["42"]

def test_global_float_assignment_valid(capsys):
    code = """
    global float ala = 0.0;
    ala = 3.14;
    print(ala);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["3.14"]

def test_global_boolean_assignment_valid(capsys):
    code = """
    global boolean ala = False;
    ala = True;
    print(ala);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["True"]

def test_global_string_assignment_valid(capsys):
    code = """
    global string ala = "abc";
    ala = "xyz";
    print(ala);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["xyz"]

def test_assign_string_to_int_should_fail(capsys):
    code = """
    global int ala = 0;
    ala = "not an int";
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.lower()
    assert "error" in captured

def test_assign_boolean_to_string_should_fail(capsys):
    code = """
    global string ala = "hello";
    ala = True;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.lower()
    assert "error" in captured

def test_assign_float_to_int_should_fail(capsys):
    code = """
    global int ala = 1;
    ala = 3.5;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.lower()
    assert "error" in captured


import pytest

def test_global_variable_redefinition(capsys):
    code = """
    global int ala = 3;
    global int ala = 4;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.lower()
    assert "error" in captured

def test_global_variable_used_in_function(capsys):
    code = """
    global int ala = 3;
    function void foo():
        print(ala);
    end;
    foo();
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    expected = ["3"]
    assert captured == expected

def test_nested_function_global_variable_usage(capsys):
    code = """
    global int ala = 5;

    function void inner():
        ala = ala + 1;
    end function;

    function void outer():
        inner();
        ala = ala + 2;
    end function;

    outer();
    print(ala);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["8"]

def test_nested_function_definition_with_global_variable(capsys):
    code = """
    global int ala = 1;

    function void outer():
        function void inner():
            ala = ala + 2;
        end function;
        inner();
        ala = ala + 3;
    end function;

    outer();
    print(ala);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["6"]

def test_deeply_nested_function_modifies_global(capsys):
    code = """
    global int counter = 0;

    function void A():
        function void B():
            function void C():
                counter = counter + 10;
            end function;
            C();
        end function;
        B();
    end function;

    A();
    print(counter);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["10"]


def test_global_modified_inside_loop(capsys):
    code = """
    global int sum = 0;

    for (int i = 0; i < 3; i++):
        sum = sum + i;
    end loop;

    print(sum);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["3"]

def test_invalid_assignment_to_global_variable(capsys):
    code = """
    global int a = 5;

    function void f():
        a = "hello";
    end function;

    f();
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.lower()
    assert "error" in captured

def test_use_global_before_declaration(capsys):
    code = """
    function void f():
        print(x);
    end function;

    global int x = 42;
    f();
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["42"]

def test_global_variable_same_name_as_function(capsys):
    code = """
    global int test = 10;

    function void test():
        print("This is function, not variable");
    end function;

    print(test);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["10"]

def test_global_used_as_loop_counter(capsys):
    code = """
    global int i = 0;

    for (i = 0; i < 3; i++):
        print(i);
    end loop;

    print(i);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["0", "1", "2", "3"]