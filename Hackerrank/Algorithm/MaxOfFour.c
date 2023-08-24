#include<stdio.h>
#include<stdlib.h>

int Input(int *a,int *b,int *c,int *d){
    scanf("%d",&*a);
    scanf("%d",&*b);
    scanf("%d",&*c);
    scanf("%d",&*d);
}

int MaxOfFour(int a,int b,int c,int d){
    if(a>b){
        if(c>a && c>d){
            return c;
        }else{
            if(a>d){
                return a;
            }else{
                return d;
            }
        }
    }else{
        if(c>b && c>d){
            return c;
        }else{
            if(b>d){
                return b;
            }else{
                return d;
            }
        }
    }
}

int main(){
    int a,b,c,d;
    Input(&a,&b,&c,&d);
    printf("%d",MaxOfFour(a,b,c,d));
    system("pause");
    system("cls");
    return 0;
}