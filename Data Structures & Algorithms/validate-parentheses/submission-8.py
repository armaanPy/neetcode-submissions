class Solution:
    def isValid(self, s: str) -> bool:
        # Add parentheses to stack
        # If parentheses are valid, pop from stack
        # Return true if stack empty
        bracketMap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = []
        for c in s:
            if c in bracketMap:
                if stack and stack[-1] == bracketMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False