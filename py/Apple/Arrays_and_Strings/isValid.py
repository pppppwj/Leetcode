class Solution:
    def isValid(self, s):
        stack = ["#"]
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            else:
                if s[i]==")":
                    if stack.pop()=="(":
                        continue
                    else:
                        return False
                if s[i]=="}":
                    if stack.pop()=="{":
                        continue
                    else:
                        return False
                if s[i]=="]":
                    if stack.pop()=="[":
                        continue
                    else:
                        return False
        stack.pop()
        if not stack:
            return True
        else:
            return False