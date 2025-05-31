def input_graph():
    graph = {}
    root_node = input("Enter the root node: ") 
    graph[root_node] = [] 
    has_adjacent = input(f"Does {root_node} have adjacent nodes? (yes/no): ")
    if has_adjacent == 'yes':
        adjacent_nodes = input(f"Enter the adjacent nodes of {root_node} (comma separated): ").split(',')
        graph[root_node] = [node.strip() for node in adjacent_nodes]  
    for node in graph[root_node]:
        has_adjacent = input(f"Does {node} have adjacent nodes? (yes/no): ")
        if has_adjacent == 'yes':
            adjacent_nodes = input(f"Enter the adjacent nodes of {node} (comma separated): ").split(',')
            graph[node] = [adj_node.strip() for adj_node in adjacent_nodes]

    return graph

def Queue():
    queue = {}
    
#main function
graph = input_graph()
print(graph)
