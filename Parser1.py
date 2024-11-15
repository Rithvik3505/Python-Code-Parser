# import ply.yacc as y
# from lexer1 import tokens, lexer

# # Define precedence to help resolve conflicts
# precedence = (
#     ('left', 'GT', 'LT'),            # Comparison operators
#     ('left', 'Add', 'Minus'),        # Addition and subtraction
#     ('left', 'Multiply', 'Divide'),  # Multiplication and division
# )

# # Starting rule
# def p_program(p):
#     '''program : statement_list'''
#     p[0] = ("program", p[1])

# def p_statement_list(p):
#     '''statement_list : statement
#                       | statement statement_list'''
#     if len(p) == 2:
#         p[0] = ("statement_list", [p[1]])  # Correct list construction
#     else:
#         p[0] = ("statement_list", [p[1]] + p[2][1])  # Combine lists correctly

# def p_statement(p):
#     '''statement : assign_statement
#                  | if_statement
#                  | for_loop
#                  | while_loop
#                  | func_decl
#                  | expression_statement'''
#     p[0] = ("statement", p[1])

# def p_assign_statement(p):
#     '''assign_statement : Id Assignment expression
#                         | Id SLbrac expression SRbrac Assignment expression'''
#     if len(p) == 4:
#         p[0] = ("assign_statement", p[1], p[2], p[3])
#     else:
#         p[0] = ("assign_statement", p[1], p[2], p[3], p[4], p[5], p[6])

# def p_expression_statement(p):
#     '''expression_statement : expression'''
#     p[0] = ("expression_statement", p[1])

# def p_expression(p):
#     '''expression : term
#                   | expression Add term
#                   | expression Minus term
#                   | comparison'''
#     if len(p) == 2:
#         p[0] = ("expression", p[1])
#     else:
#         p[0] = ("expression", p[1], p[2], p[3])

# def p_term(p):
#     '''term : factor
#             | term Multiply factor
#             | term Divide factor'''
#     if len(p) == 2:
#         p[0] = ("term", p[1])
#     else:
#         p[0] = ("term", p[1], p[2], p[3])

# def p_factor(p):
#     '''factor : Number
#               | Id
#               | String
#               | Lpar expression Rpar
#               | array_literal
#               | array_indexing'''
#     if len(p) == 2:
#         p[0] = ("factor", p[1])
#     else:
#         p[0] = ("factor", p[2])

# def p_array_indexing(p):
#     '''array_indexing : Id SLbrac expression SRbrac'''
#     p[0] = ("array_indexing", p[1], p[3])

# def p_array_literal(p):
#     '''array_literal : SLbrac elements SRbrac'''
#     p[0] = ("array_literal", p[2])

# def p_elements(p):
#     '''elements : expression
#                 | expression Comma elements
#                 | empty'''
#     if len(p) == 2:
#         p[0] = ("elements", [p[1]])  # Single expression
#     else:
#         p[0] = ("elements", [p[1]] + p[3][1])  # Concatenate elements correctly

# def p_comparison(p):
#     '''comparison : expression GT expression
#                   | expression LT expression'''
#     p[0] = ("comparison", p[1], p[2], p[3])

# def p_if_statement(p):
#     '''if_statement : if comparison Colon statement_list else_clause'''
#     p[0] = ("if_statement", p[2], p[4], p[5])

# def p_else_clause(p):
#     '''else_clause : else Colon statement_list
#                    | empty'''
#     if len(p) == 4:
#         p[0] = ("else_clause", p[3])
#     else:
#         p[0] = ("else_clause", None)

# def p_for_loop(p):
#     '''for_loop : for Id in range Lpar expression Rpar Colon statement_list'''
#     p[0] = ("for_loop", p[2], p[6], p[9])

# def p_while_loop(p):
#     '''while_loop : while comparison Colon statement_list'''
#     p[0] = ("while_loop", p[2], p[4])

# def p_func_decl(p):
#     '''func_decl : Func Id Lpar parameters Rpar Colon statement_list'''
#     p[0] = ("func_decl", p[2], p[4], p[7])

# def p_parameters(p):
#     '''parameters : Id
#                   | Id Comma parameters
#                   | empty'''
#     if len(p) == 2:
#         p[0] = ("parameters", [p[1]])
#     elif len(p) == 4:
#         p[0] = ("parameters", [p[1]] + p[3][1])
#     else:
#         p[0] = ("parameters", [])

# def p_keywords(p):
#     '''keywords:'''

# def p_empty(p):
#     '''empty :'''
#     p[0] = None

# def p_error(p):
#     if p:
#         print(f"Syntax error at '{p.value}' on line {p.lineno}")
#     else:
#         print("Syntax error at EOF")

# # Input file processing
# file = input("Enter the file path: ")
# data = open(file, "r").read()
# parser = y.yacc()

# try:
#     print("Parsing : \n")
#     print(data)
#     error_occurred = False  # Reset error flag
#     parse_tree = parser.parse(data)  # Parse the data

#     if not error_occurred:
#         lexer.input(data)  # Perform lexical analysis
#         print("Parse Tree:")
#         print(parse_tree)
#         print("\n")
#         print("Lexer Table : \n")
#         while True:
#             tok = lexer.token()
#             if not tok:
#                 break
#             print(tok)
#         print("\n")
#         print("Valid Syntax")
#         print("\n")
#         print("Code Parsed Successfully")
# except Exception as e:
#     print("Parsing error:", e)
#     exit(1)

# import ply.yacc as y
# from lexerr import tokens,lexer

# # Define precedence to help resolve conflicts
# precedence = (
#     ('left', 'GT', 'LT'),            # Comparison operators
#     ('left', 'Add', 'Minus'),        # Addition and subtraction
#     ('left', 'Multiply', 'Divide'),  # Multiplication and division
# )

# # Starting rule
# def p_program(p):
#     '''program : statement_list'''
#     pass

# # Refactor statement list to be right-recursive to avoid left recursion issues
# def p_statement_list(p):
#     '''statement_list : statement
#                       | statement statement_list'''
#     pass

# def p_statement(p):
#     '''statement : assign_statement
#                  | if_statement
#                  | for_loop
#                  | while_loop
#                  | func_decl
#                  | expression_statement'''
#     pass

# # Separate assignment statement to include array indexing
# def p_assign_statement(p):
#     '''assign_statement : Id Assignment expression
#                         | Id SLbrac expression SRbrac Assignment expression'''
#     pass

# # Expression as a standalone statement
# def p_expression_statement(p):
#     '''expression_statement : expression'''
#     pass

# # Simplify expression and term rules
# def p_expression(p):
#     '''expression : term
#                   | expression Add term
#                   | expression Minus term
#                   | comparison'''
#     pass

# def p_term(p):
#     '''term : factor
#             | term Multiply factor
#             | term Divide factor'''
#     pass

# # Modify factor to include array literals and array indexing
# def p_factor(p):
#     '''factor : Number
#               | Id
#               | String
#               | Lpar expression Rpar
#               | array_literal
#               | array_indexing'''
#     pass

# # Separate array indexing as a unique rule
# def p_array_indexing(p):
#     '''array_indexing : Id SLbrac expression SRbrac'''
#     pass

# # Array literal definition, e.g., [1, 2, 3]
# def p_array_literal(p):
#     '''array_literal : SLbrac elements SRbrac'''
#     pass

# # Elements within an array literal
# def p_elements(p):
#     '''elements : expression
#                 | expression Comma elements
#                 | empty'''
#     pass

# # New rule for comparison expressions using GT and LT
# def p_comparison(p):
#     '''comparison : expression GT expression
#                   | expression LT expression'''
#     pass

# # Refine if-else structure to avoid conflicts
# def p_if_statement(p):
#     '''if_statement : if comparison Colon statement_list else_clause'''
#     pass

# def p_else_clause(p):
#     '''else_clause : else Colon statement_list
#                    | empty'''
#     pass

# # Keep for and while loops as-is but use the comparison rule for conditions
# def p_for_loop(p):
#     '''for_loop : for Id in range Lpar expression Rpar Colon statement_list'''
#     pass

# def p_while_loop(p):
#     '''while_loop : while comparison Colon statement_list'''
#     pass

# # Function declaration with parameters
# def p_func_decl(p):
#     '''func_decl : Func Id Lpar parameters Rpar Colon statement_list'''
#     pass

# def p_parameters(p):
#     '''parameters : Id
#                   | Id Comma parameters
#                   | empty'''
#     pass

# def p_empty(p):
#     '''empty :'''
#     pass

# # Error handling
# def p_error(p):
#     if p:
#         print(f"Syntax error at '{p.value}' on line {p.lineno}")
#     else:
#         print("Syntax error at EOF")

# # Input file processing
# file = input("Enter the file path: ")
# data = open(file, "r").read()
# parser = y.yacc()

# try:
#     error_occurred = False  
#     parser.parse(data) 

#     if(error_occurred==False):
#         lexer.input(data)  
#         while True:
#             tok = lexer.token()
#             if not tok:
#                 break
#             print(tok)
#         print("Valid Syntax")
#         print("Code Parsed Sucessfully")
# except Exception as e:
#     print("Parsing error:", e)
#     exit(1)

import ply.yacc as y
from lexer1 import tokens, lexer

precedence = (
    ('left', 'GT', 'LT'),            
    ('left', 'Add', 'Minus'),        
    ('left', 'Multiply', 'Divide'),  
)

def p_program(p):
    '''program : statement_list'''
    p[0] = ("program", p[1])

def p_statement_list(p):
    '''statement_list : statement
                      | statement statement_list'''
    if len(p) == 2:
        p[0] = ("statement_list", [p[1]])  
    else:
        p[0] = ("statement_list", [p[1]] + p[2][1])  

def p_statement(p):
    '''statement : assign_statement
                 | if_statement
                 | for_loop
                 | while_loop
                 | func_decl
                 | expression_statement'''
    p[0] = ("statement", p[1])

def p_assign_statement(p):
    '''assign_statement : Id Assignment expression
                        | Id SLbrac expression SRbrac Assignment expression'''
    if len(p) == 4:
        p[0] = ("assign_statement", p[1], p[2], p[3])
    else:
        p[0] = ("assign_statement", p[1], p[2], p[3], p[4], p[5], p[6])

def p_expression_statement(p):
    '''expression_statement : expression'''
    p[0] = ("expression_statement", p[1])

def p_expression(p):
    '''expression : term
                  | expression Add term
                  | expression Minus term
                  | comparison'''
    if len(p) == 2:
        p[0] = ("expression", p[1])
    else:
        p[0] = ("expression", p[1], p[2], p[3])

def p_term(p):
    '''term : factor
            | term Multiply factor
            | term Divide factor'''
    if len(p) == 2:
        p[0] = ("term", p[1])
    else:
        p[0] = ("term", p[1], p[2], p[3])

def p_factor(p):
    '''factor : Number
              | Id
              | String
              | Lpar expression Rpar
              | array_literal
              | array_indexing'''
    if len(p) == 2:
        p[0] = ("factor", p[1])
    else:
        p[0] = ("factor", p[2])

def p_array_indexing(p):
    '''array_indexing : Id SLbrac expression SRbrac'''
    p[0] = ("array_indexing", p[1], p[3])

def p_array_literal(p):
    '''array_literal : SLbrac elements SRbrac'''
    p[0] = ("array_literal", p[2])

def p_elements(p):
    '''elements : expression
                | expression Comma elements
                | empty'''
    if len(p) == 2:
        p[0] = ("elements", [p[1]])  
    else:
        p[0] = ("elements", [p[1]] + p[3][1])  

def p_comparison(p):
    '''comparison : expression GT expression
                  | expression LT expression'''
    p[0] = ("comparison", p[1], p[2], p[3])

def p_if_statement(p):
    '''if_statement : if comparison Colon statement_list else_clause'''
    p[0] = ("if_statement", p[2], p[4], p[5])

def p_else_clause(p):
    '''else_clause : else Colon statement_list
                   | empty'''
    if len(p) == 4:
        p[0] = ("else_clause", p[3])
    else:
        p[0] = ("else_clause", None)

def p_for_loop(p):
    '''for_loop : for Id in range Lpar expression Rpar Colon statement_list'''
    p[0] = ("for_loop", p[2], p[6], p[9])

def p_while_loop(p):
    '''while_loop : while comparison Colon statement_list'''
    p[0] = ("while_loop", p[2], p[4])

def p_func_decl(p):
    '''func_decl : Func Id Lpar parameters Rpar Colon statement_list'''
    p[0] = ("func_decl", p[2], p[4], p[7])

def p_parameters(p):
    '''parameters : Id
                  | Id Comma parameters
                  | empty'''
    if len(p) == 2:
        p[0] = ("parameters", [p[1]])
    elif len(p) == 4:
        p[0] = ("parameters", [p[1]] + p[3][1])
    else:
        p[0] = ("parameters", [])

def p_empty(p):
    '''empty :'''
    p[0] = None

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' on line {p.lineno}")
    else:
        print("Syntax error at EOF")

file = input("Enter the file path: ")
data = open(file, "r").read()
parser = y.yacc()

try:
    print("Parsing : \n")
    print(data)
    error_occurred = False  
    parse_tree = parser.parse(data)  

    if not error_occurred:
        lexer.input(data)  
        print("Parse Tree:")
        print(parse_tree)
        print("\n")
        print("Lexer Table : \n")
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)
        print("\n")
        print("Valid Syntax, Code Parsed Successfully")
except Exception as e:
    print("Parsing error:", e)
    exit(1)