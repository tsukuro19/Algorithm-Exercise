#include<stdio.h>

void input(long long int a[1000]){
    for(int i=0;i<5;i++){
        scanf("%lld",&a[i]);
    }
}

long long int Sum_Array(long long int a[1000]){
    long long int sum=0;
    int i;
    for(i=0;i<4;i++){
        sum+=a[i];
    }
    return sum;
}

void Mini_Max_Sum(long long int a[1000]){
    int i,j;
    long long int sum2=0;
    long long int sum3=Sum_Array(a);
    for(i=0;i<5;i++){
        long long int sum1=0;
        for(j=0;j<5;j++){
            sum1+=a[j];
        }
        sum1-=a[i];
        if(sum1>sum2){
            sum2=sum1;
        }
        if(sum1<sum3){
            sum3=sum1;
        }
    }
    printf("%lld %lld",sum3,sum2);
}

int main(void){
    long long int a[1000];
    input(a);
    Mini_Max_Sum(a);
    return 0;
}