def dynamicFib(n):
    fibVals = [1,1]

    for i in range(2,n+1):
        fibVals.append(fibVals[i-1]+fibVals[i-2])

    return fibVals[n]


print dynamicFib(10)