import java.util.*;
//fenwick tree
public class fenwicktree{

	//private static int[] bit;
	//bit=new int[1000];
	static void update(int i, int upd,int n,int[] bit){
		for (;i<n;i+=i&(-i)){
			bit[i]+=upd;
		}
	}
	static int query(int i,int[] bit)
	{
		int sum=0;
		for (;i>0;i-=i&(-i))
		{
			sum+=bit[i];
		}
		return sum;

	}
	public static void main(String[] args)
	{
		int a[]={2,3,4,5};
		int n=a.length;
		int bit[]=new int[100];
		for (int j=1;j<n+1;j++)
			update(j,a[j-1],n,bit);
		System.out.println(query(2,bit));
	
	
	}
}
