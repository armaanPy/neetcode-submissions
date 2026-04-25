class Solution:
    def isValid(self, s: str) -> bool:
        # Add valid parentheses into stack
        # Pop from stack if valid
        # If stack is full then it contains invalid parenthesis -> return False
        bracket_map = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = []

        for c in s:
            if c in bracket_map:
                if stack and stack[-1] == bracket_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        return True if not stack else False
        