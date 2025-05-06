def ready_input(n):
	g = [[0, 19, 5, 0, 0],
	[19, 0, 5, 9, 2],
	[5, 5, 0, 1, 6],
	[0, 9, 1, 0, 1],
	[0, 2, 6, 1, 0]]
	return g
	
def user_input(n):
	g = []
	for i in range(n):
		row = []
		for j in range(n):
			if(i==j):
				row.append(0)
				continue
			cost = int(input(f"Enter cost for edge {i} - {j}: "))
			row.append(cost)
		g.append(row)
	return g

def print_graph(n, g):
	print("Adjacency Graph: ")
	for row in g:
		print(row)
		
def prims(n, g):
	selected_node = [False]*n
	no_edge = 0
	selected_node[0] = True
	INF = 9999999
	total_cost = 0
	print("\nPrim's Minimal Spanning Tree Algorithm\n")
	print("Edges : Weight")
	while(no_edge < n-1):
		mini = INF
		a = 0
		b = 0
		for i in range(n):
			if selected_node[i]:
				for j in range(n):
					if not selected_node[j] and g[i][j]>0:
						if(g[i][j] < mini):
							mini = g[i][j]
							a = i
							b = j
		print(f"{a} - {b} : {g[a][b]}")
		selected_node[b] = True
		no_edge += 1
		total_cost += g[a][b]
	print("Total cost: ",total_cost)
	
def main():
	n = int(input("Enter no. of vertices: "))
	g = ready_input(n)
	#g = user_input(n)
	print_graph(n, g)
	prims(n, g)
	
main()

