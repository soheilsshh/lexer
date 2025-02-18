import ply.lex as lex

# List of token names
tokens = (
    'NAME', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LE', 'GE', 'EQ', 'NE', 'AND', 'OR',
    'NOT', 'IF', 'ELSE', 'WHILE', 'PRINT', 'SCAN', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMICOLON', 'COMMA'
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LE      = r'<='
t_GE      = r'>='
t_EQ      = r'=='
t_NE      = r'!='
t_AND     = r'&&'
t_OR      = r'\|\|'
t_NOT     = r'!'
t_IF      = r'if'
t_ELSE    = r'else'
t_WHILE   = r'while'
t_PRINT   = r'print'
t_SCAN    = r'scan'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_SEMICOLON = r';'
t_COMMA   = r','

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t

def t_NUMBER(t):
    r'\d+(\.\d*)?'
    t.value = float(t.value)
    t.type  = 'NUMBER'
    return t

# Define a function for error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer
input_code = """
int main() {
    int x, y;
    x = 10;
    y = 20;
    if (x < y) {
        print "x is less than y";
    } else {
        print "x is not less than y";
    }
    scan = 30;
}
"""

lexer.input(input_code)

# Print out each token
for tok in lexer:
    print(f"{tok.type}||{tok.value}||{tok.lineno}||{tok.lexpos}")
