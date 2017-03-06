#kruskal,in undirected graph connects all the vertices together without any cycles and with minimum possible total edge weight
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
def find(A,a,b):
	if (root(A,a)==root(A,b)):
		return True
	else:	
		return False
Graph=[[0,1,4],[0,3,2],[0,4,1],[1,2,8],[1,4,5],[1,5,6],[2,5,1],[3,4,3],[4,5,9]]
#Graph=[['A','B',4],['A','D',2],['A','E',1],['B','C',8],['B','E',5],['B','F',6],['C','F',1],['D','E',3],['E','F',9]]

graph=sorted(Graph,key=lambda x:x[2])
n=len(graph)
size=[1]*n
A=[]
for i in range(n):
	A.append(i)

X=[]
for i in graph:
	u=i[0]
	v=i[1]
	if (find(A,u,v)!=True):
		X.append(i)
		union(A,size,u,v)

print X

