inp=[[0,1],[1,2],[0,3],[3,4],[2,3],[2,4]]
V=5
Graph={}
for i in range(V):
	Graph[i]=[]
for i in inp:
	Graph[i[0]].append(i[1])
V=len(Graph)
#store indegree array
Indegree=[0]*V
for i in Graph:
	for j in Graph[i]:
		Indegree[j]+=1
#Indegree=sorted(Indeg)
#store each vertex's indegree in a queue
que=[]
output=[]
for i in range(V):
	if Indegree[i]==0:
		que.append(i)
j=1
while len(que)>0:
	v=que.pop()
	output.append(v)
	for i in Graph[v]:
		Indegree[i]-=1
	Indegree[v]-=1
	for i in range(V):
		if Indegree[i]==0:
			que.append(i)
			break
	j+=1
print output




			
		

