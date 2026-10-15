class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operator = {"+", "-", "*", "/"}
        for s in tokens:
            if s not in operator:
                stack.append(int(s))
            else:
                a = stack.pop()
                b = stack.pop()
                res = 0
                if s == "+":
                    res = a + b
                elif s == "-":
                    res = b - a
                elif s == "*":
                    res = a * b
                elif s == "/":
                    res = int(b / a)
                stack.append(res)
        return stack[-1]
