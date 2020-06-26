def spiralOrder(nums):
    if not nums:
        return []
    # nums: m*n matrix
    m, n = len(nums), len(nums[0])
    tt = m*n
    flagx = 1
    flagy = 1

    sol = []
    x,y,count=0,0,0
    while 1:
        for i in range(n):
            sol.append(nums[x][y])
            y+=flagy
        count+=n
        if count>=tt: break
        y-=flagy
        x+=flagx
        flagy *= -1
        m-=1
        for i in range(m):
            sol.append(nums[x][y])
            x+=flagx
        count+=m
        if count>=tt: break
        x-=flagx
        y+=flagy
        flagx *= -1
        n-=1
    return sol

if __name__ == "__main__":
    nums = [[1]]
    print (spiralOrder(nums))

    