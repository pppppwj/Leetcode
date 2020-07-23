def kmp_next(s):
    nxt = [0] * len(s)
    nxt[0] = -1
    i,j=0,-1
    while i < len(s)-1:
        if j==-1 or s[i]==s[j]:
            i+=1
            j+=1
            nxt[i] = j
        else:
            j = nxt[j]
    return nxt

def kmp(s1,s2):
    nxt = kmp_next(s2)
    i,j=0,0
    while i<len(s1) and j<len(s2):
        if j==-1 or s1[i] == s2[j]:
            i+=1
            j+=1
        else:
            j = nxt[j]
    return i-j

if __name__ == "__main__":
    s = "aacecaaa"
    ss = s + "#" + s[::-1]
    print(kmp_next(ss))