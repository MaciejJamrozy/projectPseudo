from antlr4 import *
from PseudoVisitor import PseudoVisitor
from PseudoLexer import PseudoLexer
from PseudoParser import PseudoParser
from PseudoListener import PseudoListener

class PseudoInterpreter(PseudoVisitor):
    def __init__(self):
        self.variables = {}
    
    def visitPrintStatement(self, ctx):
        print(ctx.STRING().getText().strip('"'))

def run_interpreter(input_text):
    lexer = PseudoLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = PseudoParser(stream)
    tree = parser.program()
    
    interpreter = PseudoInterpreter()
    interpreter.visit(tree)

code = '''
print("Hello, World!")
'''

run_interpreter(code)
