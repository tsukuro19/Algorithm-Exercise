def Merge(numbers,left,right,n1,n2):
    i=j=k=0
    while i<n1 and j<n2:
        if left[i]>=right[j]:
            numbers[k]=left[i]
            i+=1
        else:
            numbers[k]=right[j]
            j+=1
        k+=1
    while i<n1:
        numbers[k]=left[i]
        i+=1
        k+=1
    while j<n2:
        numbers[k]=right[j]
        j+=1
        k+=1
    


def Merge_sort(numbers,n):
    if n>1:
        n1=n//2
        n2=n-n1
        left=numbers[:n1]
        right=numbers[n1:]
        Merge_sort(left,n1)
        Merge_sort(right,n2)
        Merge(numbers,left,right,n1,n2)
        return numbers



def Minimum_number(numbers,n):
    set_list=set(numbers)
    count_element=[]
    for element in set_list:
        count_element.append(numbers.count(element))
    if len(count_element)==1:
        return 0
    else:
        if sum(count_element)==0:
            return len(count_element)-1
        else:
            count_sorted=Merge_sort(count_element,len(count_element))
            count_sorted.pop(0)
            return sum(count_sorted)
    


if __name__=="__main__":
    n=int(input())
    numbers=list(map(int,input().split()))
    print(Minimum_number(numbers,n))