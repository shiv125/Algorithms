/**
author: shivdutt sharma
min-heap
**/
#include<stdio.h>
#include<stdlib.h>
#include <string.h>
#include <ctype.h>
#include<math.h>
int count=-1;

void swap(int *x, int *y){
    int temp;
    temp=*x;
    *x=*y;
    *y=temp;
}

void shiftup(int A[],int i){
    while(A[i]<A[(i-1)/2]){
        swap(&A[i],&A[(i-1)/2]);
        shiftup(A,(i-1)/2);             
    }
}
int min(int *x,int *y,int i){
    if (*x<*y)
        return 2*i+1;
    else
        return 2*i+2;
}
void shiftdown(int A[],int i){
    //replace with smaller child
    int next=min(&A[2*i+1],&A[2*i+2],i);
    while (A[i]<A[next] && next<count+1){
        swap(&A[i],&A[next]);
        shiftdown(A,next);    
    }
}
void Insert(int A[],int value){
    count++;
    A[count]=value;
    shiftup(A,count);
}
//count is last index of the array, i.e is the last node
void Delete(int A[],int value){
    int k;
    for (int i=0;i<count;i++){
        if (A[i]==value){
            k=i;
            break;
        }
    }
    swap(&A[k],&A[count]);
    count=count-1;
    shiftdown(A,k);
}
void Deletemin(int A[]){
    //int temp = A[0];
    swap(&A[0],&A[count]);
    count--;
    shiftdown(A,0);
    //return temp;
}
int Extractmin(int A[]){
    return A[0];
}

int main(int argc, char *argv[]){
    
    int y=0;
    /**
    int heap[10];
    Insert(heap,8);
    Insert(heap,5);
    Insert(heap,7);
    int k=Extractmin(heap);
    printf("%d",k);
    **/
    int n;
    scanf("%d",&n);
    //printf("%d",n);
    int heap[n];
    int result[n];
    char input[n+1][15];
    for (int i=0;i<n;i++){
        scanf (" %[^\n]s", input[i]);
        //scanf("%s",input[i]);
    }
    for (int i=0;i<n;i++){
        char *p=input[i];
        int temp[10];
        int j=0;
        while(*p){
            if (isdigit(*p)){
                temp[j]=strtol(p,&p,10);
                //printf("%d\n",j);
                //printf("%d\n",temp[j]);
                j++;
            }
            else
                p++;
            }
    
        if (temp[0]==1){
            //add element value to heap
            int value=temp[1];
            //printf("%d",temp[0]);
            //printf("\n%d",temp[1]);
            Insert(heap,temp[1]);
            
        }
        
        else if(temp[0]==2){
            //delete element v from heap
            int value=temp[1];
            Delete(heap,temp[1]);
            //printf("%d",temp[0]);
            
        }
        else if(temp[0]==3){
            int res=Extractmin(heap);
            result[y]=res;
            y++;
            
        }
    }

    for (int i=0;i<y;i++)
        printf("%d\n",result[i]);
    
  return 0;
}

  