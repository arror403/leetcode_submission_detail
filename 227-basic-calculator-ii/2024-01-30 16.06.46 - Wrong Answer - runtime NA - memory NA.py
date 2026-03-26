class Solution:
    def calculate(self, s: str) -> int:
        

        def shunting_yard(infix):
            precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
            output = []
            operator_stack = []
            operators = set(precedence.keys())

            # Helper function to check if a token is an operator
            def is_operator(token):
                return token in operators

            for token in infix:
                if token.isdigit():
                    output.append(token)
                elif is_operator(token):
                    while (operator_stack and is_operator(operator_stack[-1]) and
                        precedence[token] <= precedence[operator_stack[-1]]):
                        output.append(operator_stack.pop())
                    operator_stack.append(token)

            while operator_stack:
                output.append(operator_stack.pop())

            return ''.join(output)



        def evaluate_postfix(expression):
            stack = []
            operators = set(['+', '-', '*', '/'])

            for token in expression:
                if token not in operators:
                    stack.append(int(token))
                else:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    if token == '+':
                        stack.append(operand1 + operand2)
                    elif token == '-':
                        stack.append(operand1 - operand2)
                    elif token == '*':
                        stack.append(operand1 * operand2)
                    elif token == '/':
                        stack.append(int(operand1 / operand2))
                        # stack.append(int(eval(f'{operand1}/{operand2}')))

            return stack[0]


        return evaluate_postfix(shunting_yard(s))