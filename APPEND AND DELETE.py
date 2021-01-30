def appendAndDelete(s, t, k):
    ls,lt = len(s),len(t)
    difindex = min(ls,lt)
    limit=0
    if k>=ls+lt:
        return'Yes'
    for i in range(min(ls,lt)):
        if s[i]!=t[i]:
            difindex=i
            break
    limit = ls+lt-2*difindex
    if limit==k or (k>limit and (k-limit)%2==0):
        return'Yes'
    else:
        return'No'
