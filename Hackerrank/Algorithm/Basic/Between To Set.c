#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int Get_Total_X(int n,int m,int *a,int *b){
    int cout=0,x;
    for(x=1;x<=100;x++){
        int flag=1;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(x % a[i]!=0 || b[j] % x!=0) flag = 0;
            }
        }
        if(flag) cout++;
    }
    return cout;
}

int main(void){
    int n,m,i,j;
    scanf("%d %d",&n,&m);
    int *a=(int *) malloc(sizeof(int)*n);
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    int *b=(int *) malloc(sizeof(int)*m);
    for(j=0;j<m;j++){
        scanf("%d",&b[j]);
    }
    int cout=Get_Total_X(n,m,a,b);
    printf("%d",cout);
    free(a);
    free(b);
    return 0;
}