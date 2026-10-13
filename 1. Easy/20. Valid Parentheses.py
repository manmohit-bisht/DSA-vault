class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = {"(", "{", "["}
        closing_brackets = {")", "}", "]"}

        for bracket in s:
            if bracket in opening_brackets:
                stack.append(bracket)
            elif bracket in closing_brackets and len(stack) == 0:
                return False
            elif bracket in closing_brackets:
                top = stack[-1]
                if (
                    (top == "(" and bracket == ")")
                    or (top == "{" and bracket == "}")
                    or (top == "[" and bracket == "]")
                ):
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
