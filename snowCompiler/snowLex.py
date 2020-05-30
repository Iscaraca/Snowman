from sly import Lexer

class snowLexer(Lexer):
    tokens = { NAME, NUMBER, STRING, IF, THEN, ELSE, FOR, TO, EQEQ, SHOW }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    # Define tokens

    # Conditionals
    IF = r'if'
    THEN = r'then'
    ELSE = r'else'

    # Loops
    FOR = r'for'
    TO = r'to'

    # Built-ins
    SHOW = r'show'

    # Variable
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

    # Data types
    STRING = r'\".*?\"'

    # Comparators
    EQEQ = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'//.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')