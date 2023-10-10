#include<stdio.h>
#include<stdlib.h>

void input(long long int *s,long long int *t,long long int *m,long long int *n,long long int d1[100000],long long int d2[100000],long long int *a,long long int *b){
    long long int i,j;
    scanf("%lld %lld",&*s,&*t);
    scanf("%lld %lld",&*a,&*b);
    scanf("%lld %lld",&*m,&*n);
    for(i=0;i<*m;i++){
        scanf("%lld",&d1[i]);
    }
    for(j=0;j<*n;j++){
        scanf("%lld",&d2[j]);
    }
}

void Apple_And_Orange(long long int s,long long int t,long long int m,long long int n,long long int a,long long int b,long long int d1[100000],long long int d2[100000]){
    long long int i,j;
    long long int cout1=0,cout2=0;
    for(i=0;i<m;i++){
        if(d1[i]+a>=s && d1[i]+a<=t)
            cout1++;
    }
    for(j=0;j<n;j++){
        if(d2[j]+b>=s && d2[j]+b<=t)
            cout2++;
    }
    printf("%lld\n%lld",cout1,cout2);
}

int main(void){
    long long int s,t,m,n,a,b;
    long long int d1[100000],d2[100000];
    input(&s,&t,&m,&n,d1,d2,&a,&b);
    Apple_And_Orange(s,t,m,n,a,b,d1,d2);
    return 0;
}