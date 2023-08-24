alphabet="abcdefghijklmnopqrstuvwxyz"
heights=list(map(int,input().split()))
word=input()
set_word="".join(set(word))
result=[]
for i in set_word:
    result.append(heights[alphabet.index(i)])
print(max(result)*min(result)*len(word))