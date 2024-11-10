
class token:
    def __init__(self,type,value):
        self.type = type
        self.value = value

class ParseError(Exception):
    pass

class ASTNode:
    def __init__(self, type, value=None):
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
    def __init__(self,operator,left,right):
        super().__init__("CONDITION")
        self.add_child(left)
        self.add_child(ASTNode("OPERATOR", operator))
        self.add_child(right)

class ExpressionNode(ASTNode):
    def __init__(self, operator, left, right):
        super().__init__("EXPRESSION")
        self.add_child(left)
        self.add_child(ASTNode("OPERATOR", operator))
        self.add_child(right)

class AssignmentNode(ASTNode):
    def __init__(self, variable, expression):
        super().__init__("ASSIGNMENT")
        self.add_child(variable)
        self.add_child(expression)


tokens = [ token('KEYWORD', 'castSpell'),
    token('PUNCTUATION', '('),
    token('PUNCTUATION', ')'),
    token('IDENTIFIER', 'princess'),
    token('PUNCTUATION', ':'),
    token('KEYWORD', 'paint'),
    token('PUNCTUATION', '('),
    token('STRING', 'hello princess'),
    token('PUNCTUATION', ')') ]


keywords = ['Paint', 'castSpell', 'if', 'untilClockStrikes','paint']
equality_operator = ['is','is not']
operators = [')', '(', ')=', '(=', '-', '+', '*', '/']

token_index = 0

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

def parse_function():
    token = lookahead()
    
    if token.type == 'KEYWORD' and token.value in keywords:
        # Consume the keyword (it could be castSpell or another function keyword)
        func_keyword = match('KEYWORD', token.value)
        
        # Check if there is an opening parenthesis following the keyword
        if lookahead() and lookahead().value == '(':
            match('PUNCTUATION', '(')
            
            # Check if there’s something inside the parentheses
            inner_token = lookahead()
            if inner_token.value != ')':
                # Handle different possible types inside parentheses, e.g., FUNCTION, id, int, string, CONDITION
                if inner_token.type == 'IDENTIFIER':
                    arg_node = ASTNode("IDENTIFIER", match('IDENTIFIER').value)
                elif inner_token.type == 'INT':
                    arg_node = ASTNode("INT", match('INT').value)
                elif inner_token.type == 'STRING':
                    arg_node = ASTNode("STRING", match('STRING').value)
                elif inner_token.type == 'KEYWORD' and inner_token.value == 'if':
                    arg_node = parse_condition()  # Assuming parse_condition() exists for handling conditions
                
                
                # Add the argument as a child node
                func_node = FunctionNode(func_keyword.value)
                func_node.add_child(arg_node)
            else:
                func_node = FunctionNode(func_keyword.value)  # Empty parentheses
            
            match('PUNCTUATION', ')')
        else:
            func_node = FunctionNode(func_keyword.value)  # No parentheses, just a keyword function
        
        # Optionally match an identifier after the function keyword or parentheses
        if lookahead() and lookahead().type == 'IDENTIFIER':
            identifier_token = match('IDENTIFIER')
            func_node.add_child(ASTNode("IDENTIFIER", identifier_token.value))

        # Check if a statement block follows (starting with a colon `:`)
        if lookahead() and lookahead().value == ':':
            match('PUNCTUATION', ':')
            func_node.add_child(parse_statement_block())

        return func_node
    else:
        raise ParseError("Invalid FUNCTION syntax: Expected a function keyword.")


def parse_statement_block():
    statement_block_node = StatementBlockNode()
    token = lookahead()
    if token.type == 'KEYWORD' and token.value in keywords:
        statement_block_node.add_child(parse_function()) 
    elif token.type == 'IDENTIFIER':
        statement_block_node.add_child(parse_assignment())

    return statement_block_node

def parse_assignment():
    id = match('IDENTIFIER')
    match('PUNCTUATION','=')
    ex_node = parse_expression()

    variable_node = ASTNode("IDENTIFIER", id.value)
    return AssignmentNode(variable_node, ex_node)

def parse_expression():
    left_token = match('IDENTIFIER')
    operator_token = match('PUNCTUATION') 
    right_token = match('IDENTIFIER') 

    left_node = ASTNode("IDENTIFIER", left_token.value)
    right_node = ASTNode("IDENTIFIER", right_token.value)

    return ExpressionNode(operator_token.value, left_node, right_node)

def parse_condition():
    left_token = match('IDENTIFIER')  # or match('INT') / match('BOOL') if literals are supported
    left_node = ASTNode("IDENTIFIER", left_token.value)
    
    operator_token = lookahead()
    if operator_token and operator_token.type == 'PUNCTUATION' and operator_token.value in ['>', '<', '>=', '<=', '==', '!=']:
        operator = match('PUNCTUATION').value
    elif operator_token and operator_token.type == 'KEYWORD' and operator_token.value in ['is', 'is not']:
        operator = match('KEYWORD').value
    else:
        raise ParseError("Expected a relational operator in condition.")

    right_token = lookahead()
    if right_token.type == 'IDENTIFIER':
        right_node = ASTNode("IDENTIFIER", match('IDENTIFIER').value)
    elif right_token.type == 'INT':
        right_node = ASTNode("INT", match('INT').value)
    elif right_token.type == 'BOOL':
        right_node = ASTNode("BOOL", match('BOOL').value)
    else:
        raise ParseError("Expected an identifier or literal on the right side of the condition.")

    # Create and return a ConditionNode with the left node, operator, and right node
    return ConditionNode(operator, left_node, right_node)

def parser():
    try:
        ast = parse_function()
        print(ast)
    except ParseError as e:
        print("Parse Error:", e)

parser()
