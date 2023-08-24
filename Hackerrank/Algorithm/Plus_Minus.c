#include<stdio.h>

int input(int *n,int a[100]){
    scanf("%d",&*n);
    for(int i=0;i<*n;i++){
        scanf("%d",&a[i]);
    }
}

void Plus_Minus(int n,int a[100]){
    int i;
    int cout1=0,cout2=0,cout3=0;
    for(i=0;i<n;i++){
        if(a[i]>0){
            cout1++;
        }else if(a[i]<0){
            cout2++;
        }else{
            cout3++;
        }
    }
    printf("%f\n",(float) cout1/n);
    printf("%f\n",(float) cout2/n);
    printf("%f",(float) cout3/n);
}

int main(void){
    int n,a[100];
    input(&n,a);
    Plus_Minus(n,a);
    return 0;
}