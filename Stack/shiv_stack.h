#ifndef SHIV_STACK_H
#define SHIV_STACK_H
#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
//stack for integers
struct node{
int data;
struct node* next; //self-reference structures
};
typedef struct node *Stack;

//struct node* top=NULL;
void push(Stack *st,int data);
int pop(Stack *st);
//int size();
int peek(Stack *st);
bool isEmpty(Stack *st);
int peek(Stack *st);

//stack for characters
struct node1{
char data;
struct node1* next;
};
typedef struct node1 *Stack2; 
void push2(Stack2 *st,char data);
char pop2(Stack2 *st);
//int size();
char peek2(Stack2 *st);
bool isEmpty2(Stack2 *st);
char peek2(Stack2 *st);

#endif
