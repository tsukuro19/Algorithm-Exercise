def climbing(player,rank):
    index=0
    result=[]
    n=len(rank)
    for i in player:
        while n>index and i>=rank[index]:
            index+=1
        result.append(n+1-index)
    return result

leaderboard=int(input())
ranked=list(map(int,input().split()))
games=int(input())
player=list(map(int,input().split()))
set_ranked=list(set(ranked))
print("\n".join(map(str,climbing(player,sorted(set_ranked)))))