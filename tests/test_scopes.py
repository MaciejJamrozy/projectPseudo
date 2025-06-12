from PseudoInterpreter import run_interpreter
from antlr4 import InputStream
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_proper_var_decl_order(capsys):
    code = """
    function void foo():
        int x = 5;
        { //     { | BEGIN | BLOCK
            int y = 10;  // nowy wewnętrzny scope
            print(x + y); // x z zewnętrznego scope’u też dostępne
        }
        print(y);  // y już niewidoczne
    end; //     } | END | END BLOCK
    foo();
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    output = capsys.readouterr().out.strip().lower()
    assert "undefined" in output.lower()


def test_outer_variable_visible_in_inner_block(capsys):
    code = """
    int x = 5;
    {
        print(x);
    }
    """
    run_interpreter(InputStream(code))
    assert capsys.readouterr().out.strip() == "5"

def test_modify_outer_variable_in_inner_block(capsys):
    code = """
    int x = 5;
    {
        x = 10;
    }
    print(x);
    """
    run_interpreter(InputStream(code))
    assert capsys.readouterr().out.strip() == "10"

def test_variable_shadowing(capsys):
    code = """
    int x = 1;
    {
        int x = 2;
        print(x);
    }
    print(x);
    """
    run_interpreter(InputStream(code))
    output = capsys.readouterr().out.strip().splitlines()
    assert output == ["2", "1"]

def test_nested_blocks(capsys):
    code = """
    int a = 0;
    {
        int b = 1;
        {
            a = a + b;
        }
    }
    print(a);
    """
    run_interpreter(InputStream(code))
    assert capsys.readouterr().out.strip() == "1"

def test_nested_blocks_assignments(capsys):
    code = """
    {
        int x = 10;
        {
            int y = x + 5;
            print(y);
        }
        print(x);
    }
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip().splitlines() == ["15", "10"]

def test_modify_outer_variable(capsys):
    code = """
    {
        int x = 1;
        {
            x = x + 9;
        }
        print(x);
    }
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == "10"

def test_shadow_variable(capsys):
    code = """
    {
        int x = 5;
        {
            int x = 20;
            print(x);
        }
        print(x);
    }
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip().splitlines() == ["20", "5"]

def test_access_global_inside_nested_blocks(capsys):
    code = """
    global int g = 100;
    {
        {
            {
                print(g);
            }
        }
    }
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == "100"

def test_weird_block_usages(capsys):
    code = """
    {}
    {
        int x = 1;
        {}
        {
            x = 2;
            {
                print(x);
            }
        }
    }
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == "2"

def test_access_shadowed_variable_with_parent_scope(capsys):
    code = """
    {
        int a = 5;
        {
            int a = 10;
            print(a);          // should print 10
            print(parent::a);  // should print 5
        }
    }
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip().splitlines() == ["10", "5"]

def test_modify_parent_variable(capsys):
    code = """
    {
        int a = 1;
        {
            parent::a = 9;
        }
        print(a); // should print 9
    }
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == "9"

def test_parent_reference_without_shadowing(capsys):
    code = """
    {
        int a = 42;
        {
            print(parent::a);  // should still print 42
        }
    }
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == "42"

def test_invalid_parent_reference_should_fail(capsys):
    code = """
    {
        {
            print(parent::a);  // 'a' doesn't exist in parent scope
        }
    }
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert 'error' in capsys.readouterr().out.strip().lower()

def test_multiple_nested_parents(capsys):
    code = """
    {
        int a = 100;
        {
            int a = 50;
            {
                print(a);          // 50
                print(parent::parent::a);  // 100
            }
        }
    }
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip().splitlines() == ["50", "100"]


def test_multiple_nested_parents_modified_1(capsys):
    code = """
    {
        int a = 1;
        int b = 3;
        {
            {
                int b = 100;
                parent::parent::a = b + 9;
                print(parent::parent::a);
            }
        }
    }
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == '109'


def test_multiple_nested_parents_modified_2(capsys):
    code = """
    {
        int a = 1;
        int b = 3;
        {
            {
                int b = 100;
                parent::parent::a = parent::parent::b + 9;
                print(parent::parent::a);
            }
        }
    }
    """
    input_stream = InputStream(code)
    run_interpreter(inputStream=input_stream)
    assert capsys.readouterr().out.strip() == '12'