#https://www.geeksforgeeks.org/count-pairs-in-array-whose-sum-is-divisible-by-k/
def Divisible_Sum_Pair(a,n,k):
    # Create a frequency array to count
    # occurrences of all remainders when
    # divided by K
    freq=[0]*k
     # Count occurrences of all remainders
    for i in range(n):
        freq[a[i]%k]+=1
    # If both pairs are divisible by 'K'
    sum_freq=freq[0]*(freq[0]-1)/2
    # count for all i and (k-i)
    # freq pairs
    i=1
    while i<=k//2 and i!=k-i:
        sum_freq+=freq[i]*freq[k-i]
        i+=1
    #if k is even
    if k%2==0:
        sum_freq+=freq[k//2]*(freq[k//2]-1)/2
    return int(sum_freq)



n,k=map(int,input().split())
a=list(map(int,input().split()))
print(Divisible_Sum_Pair(a,n,k))