from antlr4 import InputStream
from PseudoInterpreter import run_interpreter
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test_if_true_branch(capsys):
    code = """
    int x = 5;
    if x > 0:
        print("positive");
    end;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ['positive']


def test_if_else_branch(capsys):
    code = """
    int x = -1;
    if x > 0:
        print("positive");
    else:
        print("not positive");
    end;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ['not positive']


def test_if_elseif_else(capsys):
    code = """
    int x = 0;
    if x > 0:
        print("positive");
    elseif x == 0:
        print("zero");
    else:
        print("negative");
    end;
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)

    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ['zero']