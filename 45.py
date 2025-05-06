def input1(graph):
	n = int(input("Enter no. of nodes: "))
	for i in range(n):
		v = input("Enter node: ")
		d = int(input("Enter no. of derived nodes: "))
		derived = []
		for j in range(d):
			child = input("Enter derived node: ")
			derived.append(child)
		graph[v] = derived
		
def printgraph(graph):
	print("Graph: ")
	print(graph)
	
def dfs(graph, visited, node):
	if node not in visited:
		visited.add(node)
		print(node, end=" ")
		for neighbour in graph[node]:
			dfs(graph, visited, neighbour)
			
def bfs(graph, visited_bfs, queue, node):
	visited_bfs.add(node)
	queue.append(node)
	while queue:
		s = queue.pop(0)
		print(s, end=" ")
		for neighbour in graph[s]:
			if neighbour not in visited_bfs:
				visited_bfs.add(neighbour)
				queue.append(neighbour)
				
def main():
	graph = {}
	visited = set()
	input1(graph)
	printgraph(graph)
	root = input("Enter start/root node: ")
	print("\nDFS: ")
	dfs(graph, visited, root)
	queue = []
	visited_bfs = set()
	print("\nBFS: ")
	bfs(graph, visited_bfs, queue, root)
	
main()
