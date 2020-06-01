from snowLex import snowLexer
from snowParse import snowParser
from snowExecute import snowExecute

lexer = snowLexer()
parser = snowParser()
env = {}

with open('testbed.snow', 'r') as f:
    for line in f:
            print("\n")
            tree = parser.parse(lexer.tokenize(line))
            print('tree: ',tree)
            snowExecute(tree, env)
