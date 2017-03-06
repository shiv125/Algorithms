#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include "shiv_stack.h"
typedef struct node *Stack;
int peek(Stack *st){
if (!isEmpty(st)){
struct node *first;
first=*st;
return first->data;
}
}
void push(Stack *st,int data){
struct node* new = (struct node*)malloc(sizeof(struct node*));
new->data = data;
new->next=*st;
*st=new;
}
bool isEmpty(Stack *st){
if (st==NULL){
return true;
}
else{
return false;
}
}
int pop(Stack *st){
if (!isEmpty(st)){
struct node *first;
first=*st;
int value=first->data;
*st=first->next;
first->next=NULL;
free(first);
return value;
}
}


//implementation of stacks for characters
typedef struct node1 *Stack2;
char peek2(Stack2 *st){
if (!isEmpty2(st)){
struct node1 *first;
first=*st;
return first->data;
}
}
void push2(Stack2 *st,char data){
struct node1* new = (struct node1*)malloc(sizeof(struct node1*));
new->data = data;
new->next=*st;
*st=new;
}
bool isEmpty2(Stack2 *st){
if (*st==NULL){
return true;
}
else{
return false;
}
}
char pop2(Stack2 *st){
if (!isEmpty2(st)){
struct node1 *first;
first=*st;
char value=first->data;

*st=first->next;
first->next=NULL;
free(first);
return value;
}
}


