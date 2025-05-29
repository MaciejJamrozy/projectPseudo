from antlr4 import InputStream
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from PseudoInterpreter import run_interpreter


def test_duplicate_function_args(capsys):
    code = """
    function foo(int x, int x):
        print(x);
    end function;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out
    assert "error in line" in captured.lower()


from antlr4 import InputStream


def test_duplicate_param_names_different_types(capsys):
    code = """
    function bar(int x, float x):
        print(x);
    end function;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out
    assert "error in line" in captured.lower()


def test_function_call_with_args(capsys):
    code = """
    function void add(int a, int b):
        print(a + b);
    end function;

    add(3, 4);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip()
    assert captured == "7"


def test_function_return_value(capsys):
    code = """
    function int getValue():
        return 42;
    end function;

    print(getValue());
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip()
    assert captured == "42"


def test_function_wrong_arg_count(capsys):
    code = """
    function test(int x) -> void:
        print(x);
    end function;

    test(1, 2);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.lower()
    assert "wrong" in captured.lower()


def test_recursive_function(capsys):
    code = """
    function int factorial(int n):
        if n == 0:
            return 1;
        else:
            return n * factorial(n - 1);
        end if;
    end function;

    print(factorial(4));
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip()
    assert captured == "24"


def test_function_string_arg(capsys):
    code = """
    function greet(string name) -> void:
        print("Hello " + name);
    end function;

    greet("Alice");
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip()
    assert captured == "Hello Alice"


def test_indirect_recursion(capsys):
    code = """
    function is_even(int n) -> boolean:
        if n == 0:
            return true;
        else:
            return is_odd(n - 1);
        end if;
    end function;

    function is_odd(int n) -> boolean:
        if n == 0:
            return false;
        else:
            return is_even(n - 1);
        end if;
    end function;

    print(is_even(4));
    print(is_odd(3));
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["True", "True"]


def test_function_with_multiple_params_and_return(capsys):
    code = """
    function int add_and_multiply(int a, int b, int c):
        return (a + b) * c;
    end function;

    print(add_and_multiply(1, 2, 3));
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == "9"


def test_function_call_inside_another_function(capsys):
    code = """
    function int square(int x):
        return x * x;
    end function;

    function int sum_of_squares(int a, int b):
        return square(a) + square(b);
    end function;

    print(sum_of_squares(2, 3));
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == "13"


def test_function_with_boolean_logic(capsys):
    code = """
    function boolean greater_than_five(int x):
        if x > 5:
            return true;
        else:
            return false;
        end if;
    end function;

    print(greater_than_five(7));
    print(greater_than_five(2));
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["True", "False"]


def test_function_with_no_return(capsys):
    code = """
    function void greet(string name):
        print("Hello,");
        print(name);
    end function;

    greet("Alice");
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["Hello,", "Alice"]


def test_function_with_inner_variable_scope(capsys):
    code = """
    int x = 5;

    function void print_local_x():
        int x = 10;
        print(x);
    end function;

    print_local_x();
    print(x);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["10", "5"]
