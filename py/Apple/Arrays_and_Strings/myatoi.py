# convert string to integer 

def myatoi(s):
    i = 0
    numberset={"0","1","2","3","4","5","6","7","8","9"}
    # skip space 
    while (i<len(s) and s[i]==" "):
        i+=1

    # pos flag == 0 / neg flag == 1
    flag = 0
    if i<len(s): 
        if s[i]=="-":
            flag = 1
            i+=1
        elif s[i]=="+":
            i+=1
    
    res=0
    while (i<len(s) and s[i] in numberset):
        res = res*10 + ord(s[i]) - ord("0")
        i+=1

    MAX_VALUE = 2**31-1
    MIN_VALUE = -2**31
    if res:
        if flag:
            return max(MIN_VALUE,-1*res)
        else:
            return min(res,MAX_VALUE)
    else:
        return 0


s=" -3213"
print(myatoi(s))