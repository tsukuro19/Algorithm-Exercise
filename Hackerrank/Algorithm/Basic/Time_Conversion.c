#include<stdio.h>
#include<string.h>

void input(int *h,int *m,int *s,char TM[100],char *c){
    scanf("%02d%c%02d%c%02d%s",&*h,&*c,&*m,&*c,&*s,TM);
}

void Time_Conversion(int h,int m,int s,char TM[100]){
    char temp2[]="AM";
    if(strcmp(temp2,TM)==0){
        if(h==12){
            printf("00:%02d:%02d",m,s);
        }else{
            printf("%02d:%02d:%02d",h,m,s);
        }
    }else{
        if(h==12){
            printf("%02d:%02d:%02d",h,m,s);
        }else{
            printf("%02d:%02d:%02d",12+h,m,s);
        }
    }
    
}

int main(void){
    int h,m,s;
    char TM[100],c;
    input(&h,&m,&s,TM,&c);
    Time_Conversion(h,m,s,TM);
    return 0;
}