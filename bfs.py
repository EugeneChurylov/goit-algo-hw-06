from collections import deque


def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    print(start_node)

    while queue:
        current_node = queue.popleft()

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                print(neighbor)