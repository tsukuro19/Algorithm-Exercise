def climbing(player,rank):
    i=len(rank)-1
    result=[]
    while (rank!=[] and player!=[]) and i!=0:
        if min(player)<rank[i]:
            result.append(i+2)
            player.remove(min(player))
        elif min(player)==rank[i]:
            result.append(i+1)
            player.remove(min(player))
        else:
            i-=1
    if len(result)!=len(player):
        result.append(1)
    return result

leaderboard=int(input())
ranked=list(map(int,input().split()))
games=int(input())
player=list(map(int,input().split()))
set_ranked=list(set(ranked))
print("\n".join(map(str,climbing(player,sorted(set_ranked,reverse=True)))))