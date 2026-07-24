class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs={')':'(',']':'[','}':'{'}
        Stack=[]
        opening = {'(','[','{'}
        closing = {')',']','}'}
        for i in s:
            if i in opening:
                Stack.append(i)
            else:
                if not Stack:
                    return False
                if Stack[-1]==pairs[i]:
                    Stack.pop()
                else:
                    return False
        return len(Stack)==0