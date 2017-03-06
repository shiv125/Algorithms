#single source shortest path in dag(for negative weight cycles)
#in O(V+E)
#first sort the vertices using topological sort
#then relax every vertex
class Graph:
	def __init__(self,vertices):
		self.V=vertices
		self.graph={}
		for i in range(self.V):
			self.graph[i]=[]

	def addEdge(self,u,v,w):
		self.graph[u].append([v,w])
	
	def TopoSort(self):
		Indegree=[0]*self.V
		for i in self.graph:
			for j in self.graph[i]:
				Indegree[j[0]]+=1
		que=[]
		output=[]
		for i in range(self.V):
			if Indegree[i]==0:
				que.append(i)
		while len(que)>0:
			v=que.pop()
			output.append(v)
			for u in self.graph[v]:
				Indegree[u[0]]-=1
			Indegree[v]-=1
			for i in range(self.V):
				if Indegree[i]==0:
					que.append(i)
					break
		return output
	def ssspdag(self,s):
		dist=[float("Inf")]*(self.V)
		dist[s]=0
		k=self.TopoSort()
		for u in k:
			for j in self.graph[u]:
				w=j[1]
				v=j[0]
				if dist[v]>dist[u]+w:
					dist[v]=dist[u]+w
		for u in self.graph:
			for v in self.graph[u]:
				if dist[v[0]]>dist[u]+v[1]:
					return

		return dist
	
			
g = Graph(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)

print g.ssspdag(1)
			



