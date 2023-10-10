#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void Enter_Multidimensional(long int *n,long int a[1000][1000]){
    scanf("%d",&*n);
    int i,j;
    for(i=0;i<*n;i++){
        for(j=0;j<*n;j++){
            scanf("%d",&a[i][j]);
        }
    }
}

void Sum_Multidimensional(long int n,long int a[1000][1000]){
    int i,j;
    int temp=n-1;
    int sum1=a[0][0];
    int sum2=a[0][n-1];
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(i==j)
                sum1+=a[i+1][j+1];
        }
    }
    for(i=0;i<n;i++){
        for(j=n-1;j>=0;j--){
        if(j==temp)
            sum2+=a[i+1][j-1];
        }
        temp--;
    }
    int diff=sum1-sum2;
    printf("%d",abs (diff));
}

int main(void){
    long int n,a[1000][1000];
    Enter_Multidimensional(&n,a);
    Sum_Multidimensional(n,a);
    return 0;
}