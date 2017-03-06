import java.util.*;
import java.io.*;
class node
{
	int data;
	node left;
	node right;
	public node(int data)
	{
		this.data=data;
		left=null;
		right=null;

	}
}
public class bst{
	public static node root;
	public bst(){
		this.root=null;
	}
	public boolean find(int data){
		node current=root;
		while (current!=null)
		{
			if (current.data=data)
			{
				return true;
			}
			else if(current.data<data)
			{
				current=current.right;
			}
			else if(current.data>data)
			{
				current=current.left;
			}
			
		}
		return false;
	}
	public insert(int data)
	{
		node newnode=new node(data);
		if (root==null)
		{
			root=newnode;
		}
		node parent=null;
		node current=newnode;
		while (true)
		{
			parent=current;
			if (current.data<data)
			{
				current=current.right;
				if (current==null)
				{
					parent.right=newnode;
				}
			}
			else
			{
				current=current.left;
				if (current=null)
				{
					parent.left=newnode;
				}
			}
		}
	}

	public boolean delete(int data)
	{
	//find the node
	node parent=root;
	node current=root;
	boolean isLeftChild=false;//find if the current is left child or right
	while (current.data!=data)
	{
		parent=current;
		if (current.data<data)
		{
			isLeftChild=false;
			current=current.right;
		}
		else{
			isLeftChild=true;
			current=current.left;
		}
		if (current=null){return false;}
	
	}
	//we have searched the node and it's parent
	//there will be 3 cases if the node has no child, node has 1 child and node has both 2 childs		
	}

}
