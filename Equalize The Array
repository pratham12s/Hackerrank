def equalizeArray(arr):
    k = max(arr)
    sum1=0
    count = [0]*(k+1)
    for i in arr:
        count[i]+=1
    ans = sum(count)
    arr2 = list(set(arr))
    for i in arr2:
        if i==k:
            sum1=sum(count[:i])
        else:
            sum1 = sum(count[:i])+sum(count[i+1:])
        ans = min(ans,sum1)
    return ans
