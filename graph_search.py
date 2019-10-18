def dfs(graph, start_vertex, target_value, visited=None):
	if not visited:
		visited = []

	visited.append(start_vertex)

	if start_vertex == target_value:
		return visited

	for neighbor in graph[start_vertex]:
		if neighbor not in visited:
			path = dfs(graph, neighbor, target_value, visited=visited)
			if path:
				return path

def bfs(graph, start_vertex, target_value):
	path = [start_vertex]
	bfs_queue = [[start_vertex, path]]
	visited = set()

	while bfs_queue:
		current_vertex, path = bfs_queue.pop(0)
		visited.add(current_vertex)
		
		for neighbor in graph[current_vertex]:
			if neighbor not in visited:
				if neighbor == target_value:
					return path + [neighbor]
				else:
					bfs_queue.append([neighbor, path + [neighbor]])