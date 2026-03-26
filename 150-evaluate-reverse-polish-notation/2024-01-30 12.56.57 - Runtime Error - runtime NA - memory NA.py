class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def post_to_in(expression):
            stack = []
            operators = set(['+', '-', '*', '/'])

            for token in expression:
                if token not in operators:
                    stack.append(token)
                else:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    if token == '/':
                        # Perform floor division and handle truncation toward zero
                        result = str(int(eval(f'{operand1} / {operand2}')))
                    else:
                        result = f'({operand1} {token} {operand2})'
                    stack.append(result)

            return stack[0] if stack else None

        return eval(post_to_in(tokens))