class Solution:
    def calculate(self, s: str) -> int:


        def infix_to_postfix(expression):
            precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
            stack = []
            postfix = []
            for char in expression:
                if char.isalnum():  # Operand
                    postfix.append(char)
                elif char in precedence:  # Operator
                    while stack and precedence.get(stack[-1], 0) >= precedence[char]:
                        postfix.append(stack.pop())
                    stack.append(char)

            while stack:
                postfix.append(stack.pop())

            return ''.join(postfix)

        # print(infix_to_postfix(s))

        def evaluate_postfix(expression):
            if expression.isdigit(): return int(expression)
            stack = []

            # Iterate through each character in the expression
            for char in expression:
                # If the character is a digit, push it onto the stack
                if char.isdigit():
                    stack.append(int(char))
                # If the character is an operator, pop two operands from the stack,
                # perform the operation, and push the result back onto the stack
                elif char in ['+', '-', '*', '/']:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    if char == '+':
                        stack.append(operand1 + operand2)
                    elif char == '-':
                        stack.append(operand1 - operand2)
                    elif char == '*':
                        stack.append(operand1 * operand2)
                    elif char == '/':
                        stack.append(int(operand1 / operand2))

            # The final result should be the only element left on the stack
            return stack.pop() if stack else None


        return evaluate_postfix(infix_to_postfix(s))