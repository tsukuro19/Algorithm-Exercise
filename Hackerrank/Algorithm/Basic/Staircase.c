#include<stdio.h>

void input(int *n){
    scanf("%d",&*n);
}

void Staircase(int n){
    int i,j,s=0,pattern=0;
    for(i=0;i<n;i++){
        s=n-(i+1);
        for(j=0;j<s;j++){
            printf(" ");
        }
        for(j=n-1;j>=s;j--){
            printf("#");
        }
        printf("\n");
    }
}

int main(void){
    int n;
    input(&n);
    Staircase(n);
    return 0;
}