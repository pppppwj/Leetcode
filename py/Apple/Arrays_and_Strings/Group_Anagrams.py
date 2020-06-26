def hashana(s):
    aux = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,
            73,79,83,89,97,101]
    res = 1
    for i in range(len(s)):
        res*=aux[ord(s[i]) - ord('a')]
    return res



def Group_Anagrams(strs):
    sol = []
    index = 0
    aux = {}
    for i in range(len(strs)):
        temp = hashana(strs[i])
        if temp in aux:
            sol[aux[temp]].append(strs[i])
        else:
            aux[temp] = index
            sol.append([strs[i]])
            index+=1
    return sol


def Str2IntArray(s):
    res = [0]*26
    for i in range(len(s)):
        res[ord(s[i]) - ord('a')]+=1
    return tuple(res)

def Group_Anagrams(strs):
    sol = []
    index = 0
    aux = {}
    for i in range(len(strs)):
        temp = Str2IntArray(strs[i])
        if temp in aux:
            sol[aux[temp]].append(strs[i])
        else:
            aux[temp] = index
            sol.append([strs[i]])
            index+=1
    return sol


if __name__ == "__main__":
    strs=["eat", "tea", "tan", "ate", "nat", "bat"]
    print (Group_Anagrams(strs))