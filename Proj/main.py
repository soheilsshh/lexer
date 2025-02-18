from ply import lex
# List of token names :
tokens = (
    'IDENTIFIER',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'ASSIGN',
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'SEMICOLON',
    'COUT',
    'CIN',
    'UNTIL',
    'EXTRACTOR',
    'REVERSE_EXTRACTOR',
    "INT",
    'STRING',
    'LT',
    'LTE',
    'GT',
    'GTE',
    'CBOPEN',
    'CBCLOSE',
    'IF',
    'ELSE',
    'RETURN'
)
# Key_Word
reserved = {
    'write': 'COUT',
    'read': 'CIN',
    'for': 'LOOP',
    'while': 'UNTIL',
    'if': 'IF',
    'so': 'ELSE',
    'int': 'INT',
    'return': 'RETURN'
}
# Regular expression rules :
t_PLUS = r'\+'
t_EXTRACTOR = r'<<'
t_REVERSE_EXTRACTOR = r'>>'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MOD = r'\%'
t_ASSIGN = r'='
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_EQUALS = r'=='
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'
t_CBOPEN = r'{'
t_CBCLOSE = r'}'
t_ignore = ' \t'   # A string containing ignored characters (spaces and tabs)
# Regular expression
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

symbol_table = {}
latest_id = 0
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    global latest_id

    t.type = reserved.get(t.value, 'IDENTIFIER')
    if t.type == 'IDENTIFIER':
        if (val := t.value) in symbol_table:
            t.value = symbol_table[val]
        else:
            symbol_table[t.value] = latest_id
            t.value = latest_id
            latest_id += 1
        # breakpoint()
    return t
# Define a rule so we can track line numbers
def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)

# C string
def t_ccode_string(t):
   r'\"([^\\\n]|(\\.))*?\"'
   t.type = reserved.get(t.value, 'STRING')
   return t

# Build the lexer
lexer = lex.lex()
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    lexer.input(data)

    print("Tokens:")
    for token in lexer:
        print(token)
#  main
def main():
    process_file("test.txt")

if __name__ == "__main__":
    main()