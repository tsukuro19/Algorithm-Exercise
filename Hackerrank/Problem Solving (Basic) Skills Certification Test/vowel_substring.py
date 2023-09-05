def Check_vowel(string,sub_length):
    vowels={"a","e","i","o","u"}
    i=0
    result=""
    sub_str=string[0:sub_length]
    vowel_count=0
    for val in sub_str:
        if val in vowels:
            vowel_count+=1
    max_vowel=vowel_count
    if vowel_count>0:
        result=sub_str
    start=1
    end=start+sub_length
    while end<=len(string):
        if string[start-1] in vowels:
            vowel_count-=1
        if string[end-1] in vowels:
            vowel_count+=1
        if vowel_count>max_vowel:
            result=string[start:end]
            max_vowel=vowel_count
        start+=1
        end+=1
    if result:
        return result
    else:
        return "Not found!"

if __name__=="__main__":
    string_check=input()
    sub_length=int(input())
    print(Check_vowel(string_check,sub_length))