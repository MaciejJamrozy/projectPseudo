from antlr4 import InputStream
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from PseudoInterpreter import run_interpreter


def test_simple_while_loop(capsys):
    code = """
    int i = 0;
    while (i < 3):
        print(i);
        i = i + 1;
    end loop;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip().splitlines() == ["0", "1", "2"]




def test_nested_while_loops(capsys):
    code = """
    int i = 0;
    while (i < 2):
        int j = 0;
        while (j < 2):
            print(i);
            print(j);
            j = j + 1;
        end loop;
        i = i + 1;
    end loop;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip().splitlines() == [
        "0",
        "0",
        "0",
        "1",
        "1",
        "0",
        "1",
        "1",
    ]


def test_while_loop_with_float_variable(capsys):
    code = """
    float x = 0.0;
    while (x < 1.0):
        print(x);
        x = x + 0.5;
    end loop;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip().splitlines() == ["0.0", "0.5"]


def test_while_loop_with_continue(capsys):
    code = """
    int i = 0;
    while (i < 3):
        i = i + 1;
        if i == 2:
            continue;
        end if;
        print(i);
    end loop;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip().splitlines() == ["1", "3"]

def test_while_with_break_condition(capsys):
    code = """
    int i = 0;
    while (true):
        print(i);
        i = i + 1;
        if i == 2:
            break;
        end if;
    end loop;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip().splitlines() == ["0", "1"]
