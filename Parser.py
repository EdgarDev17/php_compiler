# Nombres:
# Edgardo Antonio Rodriguez Galicia - RG18-I04-002
# Marcelo Ariel Mendez Castillo  - MC18-I04-002

import ply.yacc as yacc
import Lexer


# Importamos los tokens del lexer
# noinspection PySingleQuotedDocstring,PyMethodMayBeStatic

class UsoParser:
    # Propiedades
    VERBOSE = 1
    tokens = Lexer.UsoLexer.tokens
    result = ''
    error = ''

    def __init__(self, file_path):
        self.parser = None
        self.file_path = file_path

    def p_program(self, p):
        """program : OPEN_TAG declaration_list CLOSE_TAG"""
        print(p)
        pass

    def p_statement_expr(self, p):
        """statement : expression"""
        print('valor', p)

    def p_expression_plus(self, p):
        """expression : expression PLUS term"""
        p[0] = p[1] + p[3]

    def p_expression_minus(self, p):
        'expression : expression MINUS term'
        p[0] = p[1] - p[3]

    def p_term_times(self, p):
        'term : term TIMES factor'
        p[0] = p[1] * p[3]

    def p_term_div(self, p):
        'term : term DIVIDE factor'
        p[0] = p[1] / p[3]

    def p_declaration_list_1(self, p):
        'declaration_list : declaration_list declaration'
        pass

    def p_declaration_list_2(self, p):
        'declaration_list : declaration'
        pass

    def p_declaration(self, p):
        '''declaration : var_declaration
                    | fun_declaration
                    | header_declaration
                    | class_declaration
                    | print_stmt
                    | selection_stmt
                    | iteration_stmt
        '''
        pass

    def p_print_stmt(self, p):
        '''print_stmt : print_stmt ECHO STRING SEMICOLON
                        | print_stmt ECHO ID SEMICOLON
                        | empty
        '''
        pass

    def p_header_declaration(self, p):
        '''header_declaration : REQUIRE LPAREN STRING RPAREN SEMICOLON'''
        pass

    def p_class_declaration(self, p):
        'class_declaration : CLASS FUNCTION_NAME class_stmt'
        pass

    def p_class_stmt1(self, p):
        'class_stmt : LBLOCK attributes methods RBLOCK'
        pass

    def p_class_stmt2(self, p):
        'class_stmt : LBLOCK empty RBLOCK'
        pass

    def p_class_stmt3(self, p):
        'class_stmt : LBLOCK attributes RBLOCK'
        pass

    def p_attributes1(self, p):
        'attributes : attributes scope var_declaration'
        pass

    def p_attributes2(self, p):
        'attributes : scope var_declaration'
        pass

    def p_methods1(self, p):
        'methods : methods scope fun_declaration'
        pass

    def p_methods2(self, p):
        'methods : scope fun_declaration'
        pass

    def p_scope(self, p):
        '''scope : PRIVATE
                    | PUBLIC
                    | PROTECTED
        '''
        pass

    def p_var_declaration(self, p):
        '''var_declaration : ID SEMICOLON var_declaration
                            | ID SEMICOLON
                            | ID EQUAL NUMBER SEMICOLON var_declaration
                            | ID EQUAL NUMBER SEMICOLON
                            | ID EQUAL boolean SEMICOLON var_declaration
                            | ID EQUAL boolean SEMICOLON
                            | ID EQUAL ID SEMICOLON var_declaration
                            | ID EQUAL ID SEMICOLON
                            | AMPERSANT ID SEMICOLON var_declaration
                            | AMPERSANT ID SEMICOLON
        '''
        pass

    def p_fun_declaration(self, p):
        'fun_declaration : FUNCTION FUNCTION_NAME LPAREN params RPAREN compount_stmt'
        pass

    def p_params_1(self, p):
        'params : param_list'
        pass

    def p_params_2(self, p):
        'params : empty'
        pass

    def p_param_list_1(self, p):
        'param_list : param_list COMMA param'
        pass

    def p_param_list_2(self, p):
        'param_list : param'
        pass

    def p_param_1(self, p):
        'param : ID'
        pass

    def p_param_2(self, p):
        'param : ID LBRACKET RBRACKET'
        pass

    def p_compount_stmt(self, p):
        'compount_stmt : LBLOCK print_stmt local_declarations print_stmt statement_list print_stmt RBLOCK'
        pass

    def p_local_declarations_1(self, p):
        'local_declarations : local_declarations var_declaration'
        pass

    def p_local_declarations_2(self, p):
        'local_declarations : empty'
        pass

    def p_statement_list_1(self, p):
        'statement_list : statement_list statement'
        pass

    def p_statement_list_2(self, p):
        'statement_list : empty'
        pass

    def p_statement(self, p):
        '''statement : expression_stmt
                                | compount_stmt
                                | selection_stmt
                                | iteration_stmt
                                | return_stmt
        '''
        pass

    def p_expression_stmt_1(self, p):
        'expression_stmt : expression SEMICOLON'
        pass

    def p_expression_stmt_2(self, p):
        'expression_stmt : SEMICOLON'
        pass

    def p_selection_stmt(self, p):
        '''selection_stmt : IF LPAREN expression RPAREN statement
                                                | IF LPAREN expression RPAREN statement ELSE statement
                                                | SWITCH LPAREN var RPAREN statement
                                                | CASE NUMBER COLON statement BREAK SEMICOLON
                                                | DEFAULT COLON statement BREAK SEMICOLON
                                                | print_stmt
        '''
        pass

    def p_iteration_stmt(self, p):
        '''iteration_stmt :  FOR LPAREN var_declaration SEMICOLON expression SEMICOLON additive_expression RPAREN statement
            | WHILE LPAREN expression RPAREN statement
        '''
        pass

    def p_iteration_stmt_3(self, p):
        'iteration_stmt : print_stmt'
        pass

    def p_return_stmt_1(self, p):
        'return_stmt : RETURN SEMICOLON'
        pass

    def p_return_stmt_2(self, p):
        'return_stmt : RETURN expression SEMICOLON'
        pass

    def p_expression_1(self, p):
        'expression : var EQUAL expression'
        pass

    def p_expression_2(self, p):
        'expression : simple_expression'
        pass

    def p_expression_3(self, p):
        'expression : var EQUAL AMPERSANT ID'
        pass

    def p_var_1(self, p):
        'var : ID'
        pass

    def p_var_2(self, p):
        'var : ID LBRACKET expression RBRACKET'
        pass

    def p_simple_expression_1(self, p):
        'simple_expression : additive_expression relop additive_expression'
        pass

    def p_simple_expression_2(self, p):
        'simple_expression : additive_expression'
        pass

    def p_relop(self, p):
        '''relop : LESS
                        | LESSEQUAL
                        | GREATER
                        | GREATEREQUAL
                        | DEQUAL
                        | ISEQUAL
        '''
        pass

    def p_additive_expression_1(self, p):
        'additive_expression : additive_expression addop term'
        pass

    def p_additive_expression_2(self, p):
        'additive_expression : term'
        pass

    def p_additive_expression_3(self, p):
        'additive_expression : term MINUSMINUS'
        pass

    def p_additive_expression_4(self, p):
        'additive_expression : term PLUSPLUS'
        pass

    def p_addop(self, p):
        '''addop : PLUS
                        | MINUS
        '''
        pass

    def p_term_1(self, p):
        'term : term mulop factor'
        pass

    def p_term_2(self, p):
        'term : factor'
        pass

    def p_mulop(self, p):
        '''mulop : TIMES
                        | DIVIDE
        '''
        pass

    def p_factor_1(self, p):
        'factor : LPAREN expression RPAREN'
        pass

    def p_factor_2(self, p):
        'factor : var'
        pass

    def p_factor_3(self, p):
        'factor : call'
        pass

    def p_factor_4(self, p):
        'factor : NUMBER'
        pass

    def p_factor_5(self, p):
        'factor : boolean'
        pass

    def p_call(self, p):
        'call : ID LPAREN args RPAREN'
        pass

    def p_args(self, p):
        '''args : args_list
                        | empty
        '''
        pass

    def p_args_list_1(self, p):
        'args_list : args_list COMMA expression'
        pass

    def p_args_list_2(self, p):
        'args_list : expression'
        pass

    def p_boolean(self, p):
        '''boolean : TRUE
                                        | FALSE
        '''
        pass

    def p_empty(self, p):
        'empty : '
        pass

    def p_error(self, p):
        if self.VERBOSE:
            if p is not None:
                print("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) +
                      " NO SE ESPERABA EL Token  " + str(p.value))
                self.error = "ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(
                    p.value)
            else:
                self.error = "ERROR SINTACTICO EN LA LINEA: " + str(Lexer.UsoLexer.buildLexer(self.file_path))
        else:
            raise Exception('syntax', 'error')

    def get_error(self):
        return self.error

    def get_result(self):
        return self.result

    def buildParser(self):
        self.parser = yacc.yacc(module=self)

        file = open(self.file_path, 'r')
        data = file.read()
        self.parser.parse(data, tracking=True)
        print("El parser reconocio correctamente todo")
        self.result = "PARSER: El archivo esta correcto"
