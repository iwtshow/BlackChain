
def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    r = 1
    l = 0
    falg =False
    for i in range(n-1):

        if falg:
            r = r+l
            falg = False
        else:
            falg = True
            l += r
      return  l+r


climbStairs(10)

