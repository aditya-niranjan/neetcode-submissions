class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i].lstrip("-").isdigit():
                stack.append(int(tokens[i]))
            if tokens[i] == '+':
                op1 = stack.pop()
                op2 = stack.pop()
                result = op1+op2
                stack.append(result)
            elif tokens[i] == '-':
                op1 = stack.pop()
                op2 = stack.pop()
                result = op2 - op1
                stack.append(result)
            elif tokens[i] == '*':
                op1 = stack.pop()
                op2 = stack.pop()
                result = op2 * op1
                stack.append(result)
            elif tokens[i] == '/':
                op1 = stack.pop()
                op2 = stack.pop()
                result = int(op2 / op1)
                stack.append(result)
        return stack[0]