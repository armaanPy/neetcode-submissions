class Solution:
    def isValid(self, s: str) -> bool:
        # Stack
        # If brackets are valid pop from stack
        # If brackers invalid add to stack
        # True if stack empty else false
        
        stack = []
        bracketMap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        
        for c in s:
            # [ ]
            if c in bracketMap:
                # ]                                  [
                if stack and stack[-1] == bracketMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
