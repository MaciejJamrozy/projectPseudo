from antlr4 import *
from PseudoVisitor import PseudoVisitor
from PseudoLexer import PseudoLexer
from PseudoParser import PseudoParser
from PseudoListener import PseudoListener
import re

class PseudoInterpreter(PseudoVisitor):
    def __init__(self):
        self.variables = {}
    
    def visitPrintStatement(self, ctx):
        text = ctx.STRING().getText()
        text = text[1:len(text)-1]
        text = re.sub(r'\\(.)', r'\1', text)
        print(text)

def run_interpreter(input_text):
    lexer = PseudoLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = PseudoParser(stream)
    tree = parser.program()
    
    interpreter = PseudoInterpreter()
    interpreter.visit(tree)

code = r'''
shout("Hello, \"World!\"");
'''

run_interpreter(code)