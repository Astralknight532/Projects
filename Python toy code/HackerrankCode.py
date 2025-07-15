# Hackerrank code

def sockPairCounter(n, ar):
    x = n
    occ = {item: ar.count(item) for item in ar}
    paircount = 0

    for k, v in occ.items():
        if v >= 2:
            paircount += v // 2

    return paircount

def minAbsDiff(arr):
    diffs = []
    temp = 0
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            temp = arr[i] - arr[j]
            diffs.append(abs(temp))
    
    print(diffs, min(diffs))


# main driver
if __name__ == '__main__':
    #ar1 = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    #ar2 = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
    #sockPairs1 = sockPairCounter(len(ar1), ar1)
    #sockPairs2 = sockPairCounter(len(ar2), ar2)

    a1 = [3, -7, 0]
    a2 = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]
    a3 = [1, -3, 71, 68, 17]

    minAbsDiff(a1)
    minAbsDiff(a2)
    minAbsDiff(a3)