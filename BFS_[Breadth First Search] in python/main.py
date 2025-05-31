from collections import deque

def input_graph():
    graph = {}
    root_node = input("Enter the root node: ")
    graph[root_node] = []
    nodes_to_process = [root_node]

    while nodes_to_process:
        current_node = nodes_to_process.pop(0)
        has_adj = input(f"Does {current_node} have adjacent nodes?\n").strip().lower()
        if has_adj == 'yes':
            adj_nodes = input(f"Enter the adjacent nodes of {current_node}").split(',')
            graph[current_node] = [node.strip() for node in adj_nodes]
            for node in graph[current_node]:
                if node not in graph:
                    graph[node] = []
                    nodes_to_process.append(node)
    return graph

def bfs(graph, start_node):
    if start_node not in graph:
        print(f"Error: Starting node '{start_node}' not found in the graph.")
        return

    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    print("BFS Traversal starting from node:", start_node)

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    print()

graph = input_graph()
start_node = input("Enter the starting node for BFS: ")
bfs(graph, start_node)