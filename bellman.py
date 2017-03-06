class Graph:
	def __init__(self,vertices):
		self.V=vertices
		self.graph=[]

	def addEdge(self,u,v,w):
		self.graph.append([u,v,w])
	
	def bellman(self,s):
		#V=len(Graph)
		dist=[float("Inf")]*self.V
		dist[s]=0
		pred=[-1]*self.V
		for i in range(self.V):
			for (u,v,w) in self.graph:
				#relax edges
				if dist[v]>dist[u]+w:
					dist[v]=dist[u]+w
					pred[v]=u
		#check for negative cycles
		for (u,v,w) in self.graph:
			if dist[v]>dist[u]+w:
				return		
		return dist,pred
	def path(self,t):
		if self.bellman(0)!=None:
			dis,pat=self.bellman(0)
			path=[]
			while t!=-1:
				path.append(t)
				t=pat[t]
			return path	
		else:
			print "no path exists"

			
g=Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(2,0,-4)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

print g.bellman(0)
print g.path(3)
