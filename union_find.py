input_=[0,1,2,3,4,5,6]
#A[i] is a parent of i
#we can check if two elements a and b are connected or not
#iterate through all the parents of a and if b is not found till the root
#then a and b are not connected
def root(A,i):
	while (A[i]!=i):
		A[i]=A[A[i]]
		i=A[i]
	return i
#union function
def union(A,size,a,b):
	root_a=root(A,a)
	root_b=root(A,b)
	if (size[root_a]<size[root_b]):
		size[root_b]+=size[root_a]
		A[root_a]=A[root_b]
	else:
		size[root_a]+=size[root_b]
		A[root_b]=A[root_a]
def find(a,b):
	if (root(A,a)==root(A,b)):
		return True
	else:	
		return False
n=5
size=[1]*n
A=[]
for i in range(n):
	A.append(i)
union(A,size,0,1)
union(A,size,2,4)
union(A,size,0,4)
find(1,2)
print find(1,2)
