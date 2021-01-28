def repeatedString(s, n):
    count=s.count('a')
    if count==0:
        return count
    elif count==1 and len(s)==1:
        return n
    else:
        ans=0
        rem = n%len(s)
        k=n-rem
        repeated = k//len(s)
        ans=(repeated*count)+(s[:rem].count('a'))
        return ans
    
