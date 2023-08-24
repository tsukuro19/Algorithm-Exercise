#include<stdio.h>

void input(long long int *n,long long int a[100000]){
    scanf("%lld",&*n);
    for(long long int i=0;i<*n;i++){
        scanf("%lld",&a[i]);
    }
}

int Max_Of_Array(long long int n,long long int a[100000]){
    long long int max=a[0],i;
    for(i=0;i<n;i++){
        if(max<a[i])
            max=a[i];
    }
    return max;
}

void Birthday_Cake_Candle(long long int n,long long int a[100000]){
    long long int cout=0,i;
    long long int max=Max_Of_Array(n,a);
    for(i=0;i<n;i++){
        if(max==a[i])
            cout++;
    }
    printf("%lld",cout);
}

int main(void){
    long long int n,a[100000];
    input(&n,a);
    Max_Of_Array(n,a);
    Birthday_Cake_Candle(n,a);
    return 0;
}