def Sorted_sum(size,array_sum):
    sum_result=[]
    for i in range(size):
        array_sorted = [i * array_sum[i] for i in sorted(range(len(array_sum[:i])), key=lambda k: array_sum[k])]
        sum_result.append(sum(array_sorted))
    return sum(sum_result)


if __name__=="__main__":
    number=int(input())
    array_sum=[]
    for i in range(number):
        element=int(input())
        array_sum.append(element)
    print(Sorted_sum(number,array_sum)%(pow(10,9)+7))