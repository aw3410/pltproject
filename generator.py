from parser import parser

class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast
        self.generated_code = []
        self.errors = []
        self.unreachable = False;
        self.unreachablestart = False; 

    def generate_code(self, node=None, level=0):
        if node is None:
            node = self.ast  

        indent = "    " * level  
        
        if node.type == "FUNCTION":
            id = node.value
            if id == 'castSpell':
                func_name = next((child.value for child in node.children), None)
                if func_name:
                    self.generated_code.append(f"{indent}def {func_name}():")
            if id == 'paint':
                str = next((child for child in node.children), None)
                if str:
                    self.generated_code.append(f"{indent}print({str.value})")
                else:
                    self.errors.append(f"paint is missing an argument at stage {node.type}")
            if id =='untilClockStrikes':
                number = next((child for child in node.children if child.type == 'INT'), None)
                if number:
                    self.generated_code.append(f"while clock > 0:")
                else:
                    self.errors.append(f"untilClockStrikes is missing an int argument at stage {node.type}")
            if id == 'if': 
                expression = next((child for child in node.children if child.type == 'EXPRESSION'), None)
                if expression:
                    ifcondition = self.expression(expression)
                    self.generated_code.append(f"{indent}if {ifcondition}:")
                else:
                    self.errors.append(f"if is missing a condition at stage {node.type}")
            if id == 'happilyEverAfter': 
                identifier = next((child for child in node.children), None)
                if identifier:
                    self.generated_code.append(f"{indent}return({identifier.value})")
                    self.unreachable = True
                else:
                    self.errors.append(f"happilyEverAfter is missing an identifier or integer at stage {node.type}")
            for child in node.children:
                self.generate_code(child, level + 1)

        elif node.type == "STATEMENT_BLOCK":
            for child in node.children:
                self.generate_code(child, level)
            self.unreachable = False
            
        elif node.type == "ASSIGNMENT":
            variable = node.children[0].value
            right_side = node.children[2]
            if right_side.type == 'EXPRESSION':
                value = self.expression(right_side)
            else:
                value = right_side.value
            self.generated_code.append(f"{indent}{variable} = {value}")
            for child in node.children:
                self.generate_code(child,level)

        elif node.type == "CONDITION":
            condition = f"{node.children[0].value} {node.children[1].value} {node.children[2].value}"
            self.generated_code.append(f"{indent}if {condition}:")
            self.generate_code(node.children[3], level + 1)

        if self.unreachable: 
            if not self.errors: 
                self.errors.append(f"unreachable code detected at stage {node.type} and value {node.value}")
            return;


    def expression(self, node):
        left_variable = node.children[0].value
        op = node.children[1].type
        right_value = node.children[2].value
        return f"{left_variable}{op}{right_value}"

    def output_code(self):
        if (self.errors):
            return "\n".join(self.errors)
        return "\n".join(self.generated_code)



def main(scan_output):
    ast = parser(scan_output)
    codegen = CodeGenerator(ast)
    codegen.generate_code()
    generated_code = codegen.output_code()
    print(generated_code)

# scan_output = ['<KEYWORD, castSpell>', 
#           '<IDENTIFIER, repeat>', 
#           '<PUNCTUATION, (>', 
#           '<PUNCTUATION, )>', 
#           '<PUNCTUATION, :>', 
#           '<IDENTIFIER, clock>', 
#           '<ASSIGNMENT_OPERATOR, =>', 
#           '<INT, 12>', 
#           '<KEYWORD, untilClockStrikes>', 
#           '<PUNCTUATION, (>',
#           '<PUNCTUATION, )>', 
#           '<PUNCTUATION, :>', 
#           '<IDENTIFIER, clock>', 
#           '<ASSIGNMENT_OPERATOR, =>', 
#           '<IDENTIFIER, clock>', 
#           '<OPERATOR, ->', 
#           '<INT, 1>', 
#           '<KEYWORD, paint>', 
#           '<PUNCTUATION, (>',  
#           '<PUNCTUATION, )>']

scan_output = ['<KEYWORD, castSpell>', 
'<IDENTIFIER, nomidnight>', 
'<PUNCTUATION, (>', 
'<PUNCTUATION, )>', 
'<PUNCTUATION, :>', 
'<KEYWORD, if>', 
'<PUNCTUATION, (>', 
'<IDENTIFIER, clock>', 
'<OPERATOR, >>', '<INT, 12>', 
'<PUNCTUATION, )>', 
'<PUNCTUATION, :>', 
'<KEYWORD, happilyEverAfter>', 
'<IDENTIFIER, clock>', 
'<KEYWORD, paint>', 
'<PUNCTUATION, (>', 
"<STRING, 'bye bye cinderella'>", 
'<PUNCTUATION, )>']


main(scan_output)