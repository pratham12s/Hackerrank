def jumpingOnClouds(c):
    count,i=0,0
    while i<len(c)-1:
        if len(c)-i==2:
            count+=1
            i+=1 
        elif c[i+2]==0:
            count+=1
            i+=2
        else:
            count+=1
            i+=1
    return count
