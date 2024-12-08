class Solution:
    def simplifyPath(self, path: str) -> str:
        result = list()
        directories = path.split("/")

        for p in directories:
            if p == "." or p == '': continue
            if p == "..": 
                if result: result.pop()
            else: result.append(p)
        
        return '/' + '/'.join(result)

        