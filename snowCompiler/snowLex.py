from sly import Lexer

class snowLexer(Lexer):
    tokens = {IF, THEN, ELSE, EQ, LT, LE, GT, GE, NE, FOR, TO, WHILE, SHOW, VAR, NUMBER, BOOL, STRING, ARRAY}
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    # Define tokens

    # Conditionals
    IF = r'if'
    THEN = r'then'
    ELSE = r'else'

    # Comparators
    EQ = r'=='
    LE = r'<='
    LT = r'<'
    GE = r'>='
    GT = r'>'
    NE = r'!='

    # Loops
    FOR = r'for'
    TO = r'to'
    WHILE = r'while'

    # Built-ins
    SHOW = r'show'

    # Data types
    ARRAY = r'\[.*?\]'
    BOOL = r'true|false'
    STRING = r'".*?"'

    # Variable
    VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'

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
