from collections import Counter
def threesum(nums):
    sol = []
    neg, zero, pos = Counter(), 0, Counter()
    for i in range(len(nums)):
        if nums[i] == 0:
            zero +=1
        elif nums[i] > 0:
            pos[nums[i]]+=1
        else:
            neg[nums[i]]+=1

    # case 1: (0 ,0 ,0)
    if zero >= 3:
        sol.append((0,0,0))
    
    # case 2: (a, 0, -a) a>0
    if zero >= 1:
        for i in pos:
            if -i in neg:
                sol.append((i,0,-i))

    # case 3: (a,b,-a-b) a,b>0
    for i in neg:
        for j in pos:
            if j<=-i/2 and -i-j in pos:
                if -i-j == j:
                    if pos[j]>=2: sol.append((j,j,i))
                else: sol.append((i,j,-i-j))

    # case 4: (-a,-b,a+b) a,b>0
    for i in pos:
        for j in neg:
            if j<=-i/2 and -i-j in neg:
                if -i-j == j:
                    if neg[j]>=2: sol.append((j,j,i))
                else: sol.append((i,j,-i-j))

    return sol


if __name__ == "__main__":
    nums = [3,-2,-1]
    sol = threesum(nums)
    print (sol)

