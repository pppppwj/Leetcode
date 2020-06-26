def isPalindrome(s:str):
    start, end = 0, len(s)-1
    alp = set([str(i) for i in range(10)])
    # 'a' - 'z' 'A' - 'Z'
    # ord chr 
    for i in range(26):
        alp.add(chr(ord('a')+i))
        alp.add(chr(ord('A')+i))

    print(alp)

    while 1:
        while (start < len(s)-1 and not s[start] in alp):
            start+=1
        while (end>0 and not s[end] in alp):
            end-=1
        if start < end:
            if s[start].lower()!=s[end].lower():
                return False
            start+=1
            end-=1
        else:
            break

    return True


if __name__ == "__main__":
    test = "0P"
    print (isPalindrome(test))