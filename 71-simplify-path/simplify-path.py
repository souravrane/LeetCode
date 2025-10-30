class Solution:
    def simplifyPath(self, path: str) -> str:
        unslash = path.split("/")
        stack = list()

        for symbol in unslash:
            if symbol in ".": continue
            elif symbol == "..": 
                if stack: stack.pop()
            else: stack.append(symbol)
        
        return f"/{'/'.join(stack)}"
        
        