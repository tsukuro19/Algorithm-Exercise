def Jumping_cloud(clouds,k,n):
    energy,index=100,0
    while True:
        index=(index+k)%n
        energy-=1
        if clouds[index]==1:
            energy-=2
        if index==0:
            break
   
    return energy
        


if __name__=="__main__":
    n,k=map(int,input().split())
    clouds=list(map(int,input().split()))
    print(Jumping_cloud(clouds,k,n))