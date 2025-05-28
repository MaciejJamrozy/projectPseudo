from antlr4.error.ErrorListener import ErrorListener


class SyntaxErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error in line {line}, column {column}: {msg}")
