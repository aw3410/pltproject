#parser.py 
class token:
    def __init__(self,type,value):
        self.type = type
        self.value = value


class ParseError(Exception):
    pass

class ASTNode:
    def __init__(self, type=None, value=None):
        self.type = type
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self, level =0):
        indent = "  " * level
        value_str = f" ({self.value})" if self.value else ""
        result = f"{indent}{self.type}{value_str}\n"
        i=0
        for child in self.children:
            if i < len(self.children)-1:
                branch = "├── " 
            else:
                branch = "└── "
            result += f"{indent}{branch}{child.__repr__(level + 1)}"
            i +=1
        return result

class FunctionNode(ASTNode):
    def __init__(self, name):
        super().__init__("FUNCTION", name)

class StatementBlockNode(ASTNode):
    def __init__(self):
        super().__init__("STATEMENT_BLOCK")

class ConditionNode(ASTNode):
    def __init__(self, left, operator=None, right=None, is_equality=False):
        super().__init__("CONDITION")
        self.add_child(left)
        if operator:
            operator_type = "EQUALITY_OPERATOR" if is_equality else "OPERATOR"
            self.add_child(ASTNode(operator_type, operator))
        if right:
            self.add_child(right)

class ExpressionNode(ASTNode):
    def __init__(self, operator, left, right):
        super().__init__("EXPRESSION")
        self.add_child(left)
        self.add_child(ASTNode(operator))
        self.add_child(right)

class AssignmentNode(ASTNode):
    def __init__(self, variable, expression):
        super().__init__("ASSIGNMENT")
        self.add_child(variable)
        self.add_child(ASTNode('='))
        self.add_child(expression)


keywords = ['castSpell', 'if', 'untilClockStrikes','paint','happilyEverAfter']
equality_operator = ['is','is not']
operators = ['>=', '<=','>','<','-', '+', '*', '/']
assignment_operator = '='


def get_token():
    global token_index
    if token_index < len(tokens):
        token = tokens[token_index]
        token_index += 1
        return token
    return None

def lookahead():
    if token_index < len(tokens):
        return tokens[token_index]
    return None

def match(expected_type, expected_value=None):
    token = lookahead()
    if token and token.type == expected_type and (expected_value is None or token.value == expected_value):
        return get_token()
    raise ParseError(f"Expected {expected_type} with value {expected_value}, but got {token.type} with value {token.value if token else 'None'}.")

# FUNCTION → ( FUNCTION ) | CONDITION | STATEMENT_BLOCK |
# id  | int | string | keyword | keyword FUNCTION | 
# id STATEMENT_BLOCK | keyword id(): STATEMENT_BLOCK 

def parse_function():
    token = lookahead()
    
    # FUNCTION →  keyword | keyword FUNCTION 
    if token.type == 'KEYWORD' and token.value in keywords:
        func_keyword = match('KEYWORD', token.value)
        func_node = FunctionNode(func_keyword.value)

        if lookahead() and lookahead().type == 'IDENTIFIER': 
            arg_node = ASTNode("IDENTIFIER", match('IDENTIFIER').value)
            func_node.add_child(arg_node)

            if lookahead() and lookahead().value == '(':
                match('PUNCTUATION', '(')
                if lookahead() and lookahead().value == ')':
                    match('PUNCTUATION', ')')  
                else:
                    raise ParseError("Expected close parenthesis.")
            elif token.value == 'castSpell':
                # Raise an error if parentheses are missing after identifier
                raise ParseError("Function declaration must have parentheses after the identifier.")

        # Check if there is an opening parenthesis following the keyword (alternative function format)
        elif lookahead() and lookahead().value == '(':
            match('PUNCTUATION', '(')
            if token.type == 'KEYWORD' and token.value == 'if':
                    arg_node = parse_condition()  # Assuming parse_condition() exists for handling conditions
                    func_node.add_child(arg_node)

            # Check if there’s something inside the parentheses
            # FUNCTION → ( FUNCTION )
            inner_token = lookahead()
            if inner_token.value != ')':
                
                # Handle different possible types inside parentheses
                if inner_token.type == 'IDENTIFIER':
                    arg_node = ASTNode("IDENTIFIER", match('IDENTIFIER').value)
                elif inner_token.type == 'INT':
                    arg_node = ASTNode("INT", match('INT').value)
                elif inner_token.type == 'STRING':
                    arg_node = ASTNode("STRING", match('STRING').value)
                
    
                # Add the argument as a child node
                func_node.add_child(arg_node)
            
            match('PUNCTUATION', ')')
        
        else: 
            raise ParseError("Invalid function use: Missing parentheses or unexpected syntax.")

        if lookahead() and lookahead().value == ':':
            match('PUNCTUATION', ':')
            func_node.add_child(parse_statement_block())

        return func_node

    # Handle cases where token is an id, int, string
    # FUNCTION → id  | int | string | id STATEMENT_BLOCK 
    elif token.type == 'IDENTIFIER':
        left_node = ASTNode("IDENTIFIER", match('IDENTIFIER').value)
        return parse_assignment(left_node)  
    
    elif token.type in {'INT', 'STRING', 'BOOL'}:
        return ASTNode("LITERAL", match(token.type).value)
    
    elif token.type == '(': 
        arg_node = parse_function()

    
    else:
        raise ParseError("Invalid FUNCTION syntax: Expected a function keyword.")
    
def parse_statement_block():
    statement_block_node = StatementBlockNode()

    while lookahead(): 
        token = lookahead()
        #STATEMENT_BLOCK → FUNCTION STATEMENT_BLOCK
        if token.type == 'KEYWORD' and token.value in keywords:
            function_node = parse_function()
            statement_block_node.add_child(function_node)
        
        #STATEMENT_BLOCK → CONDITION STATEMENT_BLOCK
        elif token.type in {'IDENTIFIER', 'INT', 'BOOL'}:
            condition_node = parse_condition()
            statement_block_node.add_child(condition_node)
        
        else: 
            break

    return statement_block_node

# ASSIGNMENT → id = int | id = string | id = bool | id = EXPRESSION

def parse_assignment(left_node):
    match('ASSIGNMENT_OPERATOR','=')

    next_token = lookahead()
    
    if next_token.type == 'INT':
        next_token = ASTNode("INT", match('INT').value)
    elif next_token.type == 'STRING':
        next_token = ASTNode("STRING", match('STRING').value)
    elif next_token.type == 'BOOL':
        next_token = ASTNode("BOOL", match('BOOL').value)
    else:
        next_token = ASTNode("IDENTIFIER", match('IDENTIFIER').value)
        next_token = parse_expression(next_token)
    
    return AssignmentNode(left_node, next_token)
    
# EXPRESSION →  int operator int | id operator id | id operator int | 
#                 id equality_operator bool | id equality_operator int | 
#                   bool 
def parse_expression(left_node):  
    
    operator_token = lookahead()
  
    if operator_token.type == 'OPERATOR' and operator_token.value in operators:
        match('OPERATOR').value
    else: 
        raise ParseError(f"Invalid expression syntax: Expected an operator, got type: {operator_token.type}, value: {operator_token.value if operator_token else 'None'}")

    #right token, could be int, id, boolean
    right_node = lookahead()

    if not right_node:
        raise ParseError("Invalid expression syntax: Expected an int, id, or bool")
    
    elif right_node.type == 'BOOL':  
        right_node = ASTNode("BOOL", match('BOOL').value)
    elif right_node.type == 'IDENTIFIER': 
        right_node = ASTNode("IDENTIFIER", match('IDENTIFIER').value)
    elif right_node.type == 'INT': 
        right_node = ASTNode("INT", match('INT').value)

    return ExpressionNode(operator_token.value, left_node, right_node)

def parse_condition():
    


    left_token = lookahead() 
   
    if left_token.type == 'IDENTIFIER':
        left_node = ASTNode('IDENTIFIER', match('IDENTIFIER').value)
        next_token = lookahead()
         #CONDITION → ASSIGNMENT 
         # ASSIGNMENT always starts with id = 
        if next_token and next_token.value == assignment_operator:
            return parse_assignment(left_node) 
        
      #CONDITION → EXPRESSION  
      # EXPRESSION can start with id, int, bool 
    elif left_token.type == 'INT': 
        left_token = ASTNode("INT", match('INT').value)
    elif left_token.type == 'BOOL': 
        left_token = ASTNode("BOOL", match('BOOL').value)
    return parse_expression(left_node)


def parser(input):
    global token_index, tokens
    tokens = input
    token_index = 0
    try:
        ast = parse_function()
        print(ast)
    except ParseError as e:
        print("Parse Error:", e)

