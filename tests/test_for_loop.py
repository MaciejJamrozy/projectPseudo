from antlr4 import InputStream
from io import StringIO
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from PseudoInterpreter import run_interpreter

def test_for_loop():
    code = """
    for (int i = 0; i < 10; i = i + 1):
        print(i);
    end loop;
    """

    captured_output = StringIO()
    sys.stdout = captured_output

    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    sys.stdout = sys.__stdout__
    output_lines = captured_output.getvalue().strip().splitlines()
    assert output_lines == [str(i) for i in range(10)]


def test_nested_for_loops(capsys):
    code = """
    for (int i = 0; i < 2; i++):
        for (int j = 0; j < 2; j++):
            print(i);
            print(j);
        end loop;
    end loop;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    expected = ["0", "0", "0", "1", "1", "0", "1", "1"]
    assert captured == expected


def test_nested_loops_with_condition(capsys):
    code = """
    for (int i = 0; i < 3; i++):
        for (int j = 0; j < 3; j++):
            if (i == j):
                print(i);
                print(j);
            end;
        end loop;
    end loop;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    expected = ["0", "0", "1", "1", "2", "2"]
    assert captured == expected


def test_loop_inside_function(capsys):
    code = """
    function void loopTest():
        for (int i = 0; i < 3; i++):
            print(i);
        end loop;
    end;

    loopTest();
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    expected = ["0", "1", "2"]
    assert captured == expected


def test_loop_with_function_return(capsys):
    code = """
    function int getOne():
        return 1;
    end;

    for (int i = 0; i < 3; i = i + getOne()):
        print(i);
    end loop;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    expected = ["0", "1", "2"]
    assert captured == expected


def test_float_iteration_loop(capsys):
    code = """
    for (float i = 0.0; i < 1.0; i = i + 0.25):
        print(i);
    end loop;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    expected = ["0.0", "0.25", "0.5", "0.75"]
    assert captured == expected


def test_float_decrement_loop(capsys):
    code = """
    for (float i = 1.0; i > 0.0; i = i - 0.25):
        print(i);
    end loop;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    expected = ["1.0", "0.75", "0.5", "0.25"]
    assert captured == expected


def test_modify_loop_variable_inside_loop(capsys):
    code = """
    for (int i = 0; i < 5; i++):
        print(i);
        i = i + 1;
    end loop;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    expected = ["0", "2", "4"]
    assert captured == expected


def test_loop_with_continue(capsys):
    code = """
    for (int i = 1; i < 4; i++):
        if (i == 2):
            continue;
        end if;
        print(i);
    end loop;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    expected = ["0","1", "3","4"]
    assert captured == expected


def test_loop_with_break(capsys):
    code = """
    for (int i = 0; i < 5; i++):
        if (i == 3):
            break;
        end if;
        print(i);
    end loop;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    expected = ["0", "1", "2"]
    assert captured == expected

def test_loop_with_nested_break(capsys):
    code = """
    for (int i = 0; i < 3; i++):
        print(i);
        for (int j = 0; j < 2; j++):
            if j==1:
                break;
            end if;
            print(j);
        end loop;
    end loop;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    expected = ["0", "0", "1", "0", "2", "0"]
    assert captured == expected

def test_loop_with_nested_break(capsys):
    code = """
    int a = 0;
    for (;;):
        print(a);
        a = a + 1;
        if a == 3:
            break;
        end if;
    end loop;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    expected = ["0", "1", "2"]
    assert captured == expected


def test_declaration_inside_while_loop(capsys):
    code = """
   for (int i = 0; i < 1; i++):
        int y = 11;
        for (int j = 0; j < 2; j++):
        end loop;
    end loop;

    print(y);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == "11"


def test_redeclaration_inside_while_loop(capsys):
    code = """
    for (int i = 0; i < 2; i++):
        int y = 11;
        for (int j = 0; j < 2; j++):
        end loop;
    end loop;
    
    print(y);
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    captured = capsys.readouterr().out.strip().lower()
    assert "error" in captured