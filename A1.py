from collections import deque, defaultdict

def create_graph():
    graph = defaultdict(list)
    num_nodes = int(input("Enter the number of nodes: "))
    num_edges = int(input("Enter the number of edges: "))
    print("Enter the edges (format: node1 node2):")
    for _ in range(num_edges):
        node1, node2 = input().split()
        graph[node1].append(node2)
        graph[node2].append(node1)  # For undirected graph; remove this line for directed graph
    return graph

def display_graph(graph):
    for node in graph:
        print(f"{node}: {', '.join(graph[node])}")

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = create_graph()
print("Graph representation (Adjacency List):")
display_graph(graph)

start_node = input("\nEnter the starting node for BFS and DFS: ")
print("\nBFS traversal:")
bfs(graph, start_node)
print("\nDFS traversal:")
dfs(graph, start_node)
