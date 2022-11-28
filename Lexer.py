# Nombres:

# Edgardo Antonio Rodriguez Galicia - RG18-I04-002
# Marcelo Ariel Mendez Castillo  - MC18-I04-002
# -------------------------------------------------------------------------------------------------------------------
# Documentacion de la lib PLY (Python Lex-Yacc): https://ply.readthedocs.io/en/latest/ply.html

import ply.lex as lex


# noinspection PySingleQuotedDocstring,PyMethodMayBeStatic
class UsoLexer:
    # propiedades

    tokens_reviewed = []
    tokens = (
        'BREAK',
        'ELSE',
        'ECHO',
        'FOR',
        'IF',
        'RETURN',
        'WHILE',
        'REQUIRE',
        'TRUE',
        'FALSE',
        'FUNCTION',
        'SWITCH',
        'CASE',
        'DEFAULT',
        'CLASS',
        'PUBLIC',
        'PRIVATE',
        'PROTECTED',
        'OPEN_TAG',
        'CLOSE_TAG',
        'ID',
        'NUMBER',
        'STRING',
        'FUNCTION_NAME',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'EQUAL',
        'LESS',
        'LESSEQUAL',
        'GREATER',
        'GREATEREQUAL',
        'DEQUAL',
        'ISEQUAL',
        'PLUS',
        'PLUSPLUS',
        'MINUSMINUS',
        'SEMICOLON',
        'COMMA',
        'LPAREN',
        'RPAREN',
        'LBRACKET',
        'RBRACKET',
        'LBLOCK',
        'RBLOCK',
        'COLON',
        'AMPERSANT',
    )

    # Expresiones regulares para los tokens
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_EQUAL = r'='
    t_LESS = r'<'
    t_GREATER = r'>'
    t_SEMICOLON = ';'
    t_COMMA = r','
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_LBLOCK = r'\{'
    t_RBLOCK = r'\}'
    t_COLON = r':'
    t_AMPERSANT = r'\&'

    def __init__(self, file_path):
        self.lexer = None
        self.file_path = file_path

    # Palabras reservadas
    def t_FALSE(self, t):
        r'false'
        return t

    def t_TRUE(self, t):
        r'true'
        return t

    def t_CLASS(self, t):
        r'class'
        return t

    def t_PRIVATE(self, t):
        r'private'
        return t

    def t_PUBLIC(self, t):
        r'public'
        return t

    def t_PROTECTED(self, t):
        r'protected'
        return t

    def t_REQUIRE(self, t):
        r'require'
        return t

    def t_WHILE(self, t):
        r'while'
        return t

    def t_FUNCTION(self, t):
        r'function'
        return t

    def t_SWITCH(self, t):
        r'switch'
        return t

    def t_CASE(self, t):
        r'case'
        return t

    def t_DEFAULT(self, t):
        r'default'
        return t

    def t_BREAK(self, t):
        r'break'
        return t

    def t_ELSE(self, t):
        r'else'
        return t

    def t_ECHO(self, t):
        r'echo'
        return t

    def t_FOR(self, t):
        r'for'
        return t

    def t_IF(self, t):
        r'if'
        return t

    def t_RETURN(self, t):
        r'return'
        return t

    # tags

    def t_OPEN_TAG(self, t):
        r'<[?%](([Pp][Hh][Pp][ \t\r\n]?)|=)?'
        return t

    def t_CLOSE_TAG(self, t):
        r'[?%]>\r?\n?'
        return t

    # ------------------------------------

    def t_STRING(self, t):
        r'(\"(.)*?\"|\'(.)*?\')'
        return t

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        #  print(t.value) # mostrar los valores de las variables
        return t

    def t_ID(self, t):
        r'\$ \w+(_\d\w)*'
        # print(t.value)
        return t

    def t_FUNCTION_NAME(self, t):
        r'[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*'
        return t

    # ------------------------------------

    def t_LESSEQUAL(self, t):
        r'<='
        return t

    def t_GREATEREQUAL(self, t):
        r'>='
        return t

    def t_DEQUAL(self, t):
        r'!='
        return t

    def t_ISEQUAL(self, t):
        r'=='
        return t

    # -------------------------------------

    def t_MINUSMINUS(self, t):
        r'--'
        return t

    def t_PLUSPLUS(self, t):
        r'\+\+'
        return t

    # -------------------------------------

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_comments(self, t):
        r'/\*(.|\n)*?\*/'
        t.lexer.lineno += t.value.count('\n')

    def t_comments_C99(self, t):
        r'//(.)*?\n'
        t.lexer.lineno += 1

    # ------------------------------------------------------------------
    t_ignore = ' \t'

    # get y set
    def getTokenAnalized(self):
        return self.tokens_reviewed

    # Manejador de errores lex
    def t_error(self, t):
        print("Ocurrio un error lexico: " + str(t.value[0]))
        t.lexer.skip(1)

    def test(self, data):
        self.lexer.input(data)  # Asignamos el contenido al lexer
        while True:  # recorremos el texto extraido del documento php
            tok = self.lexer.token()  # Si el token es valido, procede a analizarlo
            if not tok:
                break  # Cerramos el programa si encontramos un token no valido
            self.tokens_reviewed.append(tok)
            print(tok)  # Imprimimos el resultado del analisis

    def buildLexer(self):
        self.lexer = lex.lex(module=self)
        if self.file_path is not None:
            fin = self.file_path  # Asignamos la ubicacion del archivo a ejecutar
            f = open(fin, 'r')  # Abrimos el archivo en modo de lectura
            data = f.read()  # Copiamos el contenido del archivo y lo guardamos
            print(data)  # Imprimimos el contenido
            self.lexer.input(data)  # Enviamos el contenido al lexer
            self.test(data)  # Ejecutamos el contenido del lexer
        else:
            return