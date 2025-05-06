from queue import PriorityQueue

#movement directions (up, down, left, right)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#heuristic d = |x1 - x2| + |y1 - y2|
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    open_list = PriorityQueue()
    open_list.put((0 + manhattan_distance(start, goal), 0, start)) #(f-score, g-score, node)
    g_cost = {start: 0}
    came_from = {}
    
    while not open_list.empty():
        # Get the node with the lowest f = g + h
        _, current_g_cost, current = open_list.get()
        if current == goal:
        	path = []
        	while current in came_from:
        		path.append(current)
        		current = came_from[current]
        	path.append(start)
        	path.reverse()
        	print("Total cost: ",current_g_cost)
        	return path
        for move in MOVES:
            neighbor = (current[0] + move[0], current[1] + move[1])
            # Check if neighbor is within bounds and not a wall
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] != 1:
                tentative_g_cost = current_g_cost + 1
                # If we found a better way to the neighbor, update it
                #g_cost to check if neighbor has not been visited before
                #tentative_g_cost < g_cost[neighbor] to check even If the neighbor has already been visited, 
                #the newly calculated tentative cost to reach the neighbor is better (lower) than the previously 
                #recorded cost in g_cost[neighbor].
                if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                    g_cost[neighbor] = tentative_g_cost
                    f_cost = tentative_g_cost + manhattan_distance(neighbor, goal)
                    open_list.put((f_cost, tentative_g_cost, neighbor))
                    came_from[neighbor] = current

    # If no path is found
    return None
    
    
def main():
	n = int(input("Enter the number of rows in the maze: "))
	m = int(input("Enter the number of columns in the maze: "))
	maze = []
	print("Enter the maze row by row (use 0 for open path and 1 for blocked path):")
	for i in range(n):
		row = []
		for j in range(m):
			a = int(input(f"Enter {i},{j}: "))
			row.append(a)
		maze.append(row)
		
	s1 = int(input("Enter x for start position (x,y): "))
	s2 = int(input("Enter y for start position (x,y): "))
	g1 = int(input("Enter x for goal position (x,y): "))
	g2 = int(input("Enter y for goal position (x,y): "))
	start = (s1,s2)
	goal = (g1,g2)
	print(maze)
	for e in maze:
		print(e)
	
	path = astar(maze, start, goal)

	if path:
	    print("Path found:", path)
	else:
	    print("No path found.")
	    
main()
