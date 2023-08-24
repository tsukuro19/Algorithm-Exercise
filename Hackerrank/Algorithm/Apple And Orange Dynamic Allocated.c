#include<stdio.h>
#include<stdlib.h>

/*void input(int *s,int *t,int *m,int *n,int *d1,int *d2,int *a,int *b){
    int i,j;
    scanf("%d %d",&*s,&*t);
    scanf("%d %d",&*a,&*b);
    scanf("%d %d",&*m,&*n);
    /*if(*a<*s<*t<*b)
        system("cls");
    for(i=0;i<*m;i++){
        scanf("%d ",&*(d1+i));
    }
    for(j=0;j<*n;j++){
        scanf("%d ",&*(d2+j));
    }
}*/

void Apple_And_Orange(int s,int t,int m,int n,int a,int b,int *d1,int *d2){
    int i,j;
    printf("%d",s);
    int cout1=0,cout2=0;
    for(i=0;i<m;i++){
        if((*(d1+i)+a)>=s && (*(d1+i)+a)<=t)
            cout1++;
    }
    for(j=0;j<n;j++){
        if((*(d2+j)+b)>=s && (*(d2+j)+b)<=t)
            cout2++;
    }
    printf("%d\n%d",cout1,cout2);
}

int main(void){
    int s,t,m,n,a,b;
    //input(&s,&t,&m,&n,&*d1,&*d2,&a,&b);
    int i,j;
    scanf("%d %d",&s,&t);
    scanf("%d %d",&a,&b);
    scanf("%d %d",&m,&n);
    int *d1=(int *) malloc(m*sizeof(int));
    int *d2=(int *) malloc(n*(sizeof(int)));
    /*if(*a<*s<*t<*b)
        system("cls");*/
    for(i=0;i<m;i++){
        scanf("%d ",(d1+i));
    }
    for(j=0;j<n;j++){
        scanf("%d ",(d2+j));
    }
    Apple_And_Orange(s,t,m,n,a,b,d1,d2);
    free(d1);
    free(d2);
    return 0;
}