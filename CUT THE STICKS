def cutTheSticks(arr):
    arr = sorted(arr)
    count = []
    item=0
    while(len(arr)>0):
        k=arr[0]
        count.append(len(arr))
        arr = list(map(lambda x: x - k, arr))
        arr = list(filter((item).__ne__, arr))
        arr=sorted(arr) 
    return count
