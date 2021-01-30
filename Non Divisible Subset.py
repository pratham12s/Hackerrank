#1Solution based on sum of two numbers is divisible by K only if the remainder of first number is r then the remainder of the second number must be k-r. Hence we iterate from 1 to the half of the array and select the remainder either r or K-r whichever is maximum. 
#2 we also take the 0 remainder once so that we do not end up with numbers that have sum divisible by K (add 1 to answer only if there is a number which gives remainder 0 on dividing by K)
#3 Incase the remainder is even then the K/2 remainder needs to be add one if there is a number which leaves a remainder of exact K/2 because we ont iterate through the K/2 incase K is even and we need to add it only once because (K/2)*2=K hence that will not satisfy the condition of Non Divisible by K
def nonDivisibleSubset(k, s):
    # Write your code here
    remainder =[0]*k
    max_count=0
    for i in s:
        r_index = i%k
        remainder[r_index]+=1
    for i in range(1,(k+1)//2):
        max_count+=max(remainder[i],remainder[k-i])
    if remainder[0]>0:
        max_count+=1
    if k%2==0 and remainder[k//2]>0:
        max_count+=1
    return max_count
