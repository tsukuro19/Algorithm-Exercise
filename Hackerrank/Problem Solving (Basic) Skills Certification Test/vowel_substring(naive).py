def Check_vowel(string,sub_length):
    vowel=['a','e','i','o','u']
    max_count_vowel,result_string=0,""
    step=0
    while step+sub_length<=len(string):
        count_vowel=0
        for i in range(step,step+sub_length):
            if string[i] in vowel:
                count_vowel+=1
        if count_vowel>max_count_vowel:
            result_string=string[step:step+sub_length]
            max_count_vowel=count_vowel
        step+=1
    if result_string=="":
        return "Not found!"
    return result_string

if __name__=="__main__":
    string_check=input()
    sub_length=int(input())
    print(Check_vowel(string_check,sub_length))