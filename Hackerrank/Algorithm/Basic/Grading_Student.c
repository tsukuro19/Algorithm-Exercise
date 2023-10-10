#include<stdio.h>
#include<stdlib.h>

void input(int *n,int a[100]){
    scanf("%d",&*n);
    for(int i=0;i<*n;i++)
        scanf("%d",&a[i]);
}

void Grading_Student(int n,int a[100]){
    int i,j,sum;
    for(i=0;i<n;i++){
        sum=a[i];
        for(j=0;j<=5;j++){
            sum+=1;
            if(sum%5==0)
                break;
        }
        if(sum<40){
            printf("%d\n",a[i]);
        }else{
            if(sum-a[i]>=3)
                printf("%d\n",a[i]);
            else{
                printf("%d\n",sum);
            }
        }
    }
}

int main(void){
    int n,a[100];
    input(&n,a);
    Grading_Student(n,a);
    return 0;
}