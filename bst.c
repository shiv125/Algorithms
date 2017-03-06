//implement binary search tree
#include<stdio.h>
#include<stdlib.h>
struct node {
	struct node* leftchild;
	struct node* rightchild;
	int data;
	};

struct node*  Insert(struct node* root, int value){
	struct node *newnode = (struct node*)malloc(sizeof(struct node));
	newnode->data=value;
	newnode->leftchild=NULL;
	newnode->rightchild=NULL;
	
	if (root=NULL){
		root=newnode;
		return root;
	}
	else{
		if (value<root->data)
			newnode->leftchild=Insert(newnode->leftchild,value);
		else
			newnode->rightchild=Insert(newnode->rightchild,value);
	}
	return root;
}

		
struct node* Search(struct node* root,int value){
	struct node *curent=root;
	while (current->data!=NULL){
		if (current->data > value)
			current=current->leftchild;
		else if(current->data<value)
			current=current->rightchild;
		if (current==NULL)
			printf("number not found");
	}
	return current;
}
int main(){
	struct node* root=NULL;
	Insert(root,4);
	Insert(root,5);

}

		



