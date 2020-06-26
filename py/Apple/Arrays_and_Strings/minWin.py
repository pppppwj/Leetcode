# S = "ADOBECODEBANC", T = "ABC"
from collections import Counter
def minWin(s: str,t: str):
    # using counter and missing 
    # to check whether t already inside s[start:end]
    t_counter = Counter(t)
    missing = len(t)
    i,j=0,0
    start,end = 0,0
    while (end < len(s)):
        if t_counter[s[end]]>0:
            missing-=1
        t_counter[s[end]]-=1
        
        end+=1

        if missing == 0:
            # find start
            while t_counter[s[start]]<0:
                t_counter[s[start]]+=1
                start +=1
            t_counter[s[start]]+=1
            missing+=1
            if j==0 or end - start < j - i:
                j,i=end,start
            start +=1
    return s[i:j]

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print (minWin(s,t))
            

    
