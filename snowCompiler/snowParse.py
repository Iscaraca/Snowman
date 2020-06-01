from sly import Parser
from snowLex import snowLexer

class snowParser(Parser):
    tokens = snowLexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
        )

    def __init__(self):
        self.env = { }
    @_('')
    def statement(self, p):
        pass

    @_('FOR var_assign TO expr THEN statement')
    def statement(self, p):
        print("this is a for loop")
        return ('for_loop', ('for_loop_setup', p.var_assign, p.expr), p.statement)

    @_('IF condition THEN statement ELSE statement')
    def statement(self, p):
        print("this is an if conditional")
        return ('if_stmt', p.condition, ('branch', p.statement0, p.statement1))

    @_('expr EQ expr')
    def condition(self, p):
        print("this is an equality operator")
        return ('condition_eq', p.expr0, p.expr1)

    @_('expr LE expr')
    def condition(self, p):
        print("this is a less-than-equal operator")
        return ('condition_le', p.expr0, p.expr1)

    @_('expr LT expr')
    def condition(self, p):
        print("this is an less-than operator")
        return ('condition_lt', p.expr0, p.expr1)

    @_('expr GE expr')
    def condition(self, p):
        print("this is an greater-than-equal operator")
        return ('condition_ge', p.expr0, p.expr1)

    @_('expr GT expr')
    def condition(self, p):
        print("this is an greater-than operator")
        return ('condition_gt', p.expr0, p.expr1)
    
    @_('expr NE expr')
    def condition(self, p):
        print("this is a not-equal operator")
        return ('condition_ne', p.expr0, p.expr1)

    @_('var_assign')
    def statement(self, p):
        print("this is a variable assignment")
        return p.var_assign

    @_('VAR "=" expr')
    def var_assign(self, p):
        print("this is an evaulated variable assignment")
        return ('var_assign', p.VAR, p.expr)

    @_('VAR "=" STRING')
    def var_assign(self, p):
        print("this is a string variable assignment")
        return ('var_assign', p.VAR, p.STRING)

    @_('VAR "=" BOOL')
    def var_assign(self, p):
        print("this is a boolean variable assignment")
        return ('var_assign', p.VAR, p.BOOL)

    @_('showing_console')
    def statement(self, p):
        print("this is a console statement")
        return p.showing_console
    
    @_('SHOW "(" STRING ")"')
    def showing_console(self, p):
        print("this is to show a string")
        return ('show', p.STRING)

    @_('SHOW "(" BOOL ")"')
    def showing_console(self, p):
        print("this is to show a boolean")
        return ('show', p.BOOL)
    
    @_('SHOW "(" expr ")"')
    def showing_console(self, p):
        print('this is to show an expression')
        return ('show', p.expr)

    @_('SHOW "(" VAR ")"')
    def showing_console(self, p):
        print('this is to show a variable')
        return ('show_var', p.VAR)

    @_('expr')
    def statement(self, p):
        print('this is to return an expression')
        return (p.expr)

    @_('expr "+" expr')
    def expr(self, p):
        print('add')
        return ('add', p.expr0, p.expr1)

    @_('expr "-" expr')
    def expr(self, p):
        print('sub')
        return ('sub', p.expr0, p.expr1)

    @_('expr "*" expr')
    def expr(self, p):
        print('mul')
        return ('mul', p.expr0, p.expr1)

    @_('expr "/" expr')
    def expr(self, p):
        print('div')
        return ('div', p.expr0, p.expr1)

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        print("unary minus")
        return p.expr

    @_('VAR')
    def expr(self, p):
        print('variable')
        return ('var', p.VAR)

    @_('NUMBER')
    def expr(self, p):
        print('number')
        return ('num', p.NUMBER)
