class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        md = {'}':'{',')':'(',']':'['}
        l = []
        for i in s:
            if i in md.values():
                l.append(i)
            else:
                if not l:
                    return False
                elif l.pop() !=md[i]:
                    return False
        return not l