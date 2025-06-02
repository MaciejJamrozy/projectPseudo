from PseudoInterpreter import run_interpreter
from antlr4 import InputStream
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_proper_var_decl_order(capsys):
    code = """
    function void foo() {
        var x = 5;
        { //     { | BEGIN | BLOCK
            var y = 10;  // nowy wewnętrzny scope
            print(x + y); // x z zewnętrznego scope’u też dostępne
        }
        print(y);  // y już niewidoczne
    } //     } | END | END BLOCK
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    output = capsys.readouterr().out.strip().lower()
    assert "undefined" in output.lower()