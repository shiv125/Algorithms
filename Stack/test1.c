#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include <string.h>
#include <ctype.h>
#include "shiv_stack.h"
#include<math.h>
bool precedence(char x, char y){

if (x=='^')
return false;
else if ((x=='/' ||  x=='*')  && (y=='+' || y=='-'))
return false;
else
return true;
}
int operatorfun(char op, int x, int y){

if (op=='+')
return x+y;
else if (op=='-')
return x-y;
else if (op=='*')
return x*y;
else if (op=='/')
return x/y;
else if (op=='^')
return (int)pow(x,y);



}
/**
The C library function long int strtol(const char *str, char **endptr, int base) converts the initial part of the string in str to a long int value according to the given base, which must be between 2 and 36 inclusive, or be the special value 0.
**/
int main(char *argv[]){
int n;
scanf("%d",&n);
char a[n+1][100];//max number of str is n+1 and max num of char is 10

for (int i=0;i<n;i++){
scanf("%s",a[i]);
}	
for (int j=0;j<n;j++){
Stack numbers= NULL;//integer stack
Stack2 operators=NULL;//operator stack

//char input[10];
//scanf("%s",input);

char *p=a[j]; 

while (*p) { // While there are more characters to process...
    if (isdigit(*p)) { // Upon finding a digit, ...
        int val = strtol(p, &p, 10); // Read a number, ...
	push(&numbers,val);        
    } else { // Otherwise, move on to the next character and that character will be surely operator

while(!isEmpty2(&operators) && precedence(*p,peek2(&operators))){
		
	int x=pop(&numbers);
	int y=pop(&numbers);
	int r = operatorfun(pop2(&operators),y,x);
//operatarfun will give the result after applying the operation between two numbers
 	
	push(&numbers, r);
	
			
	}

	push2(&operators,*p);        
	p++;
    }
}


while (!isEmpty2(&operators)){
	int x=pop(&numbers);
	int y=pop(&numbers);
int z= pop2(&operators);
	int r = operatorfun(z,y,x);

	push(&numbers, r);
}

//ALGORITHM
/**
now we have two arrays, one is of digits and another is of operators;
if there are n numbers, then there will be n-1 operators
we will use is two stacks, 
**/

printf("%d\n",pop(&numbers));
}
return 0;
}
