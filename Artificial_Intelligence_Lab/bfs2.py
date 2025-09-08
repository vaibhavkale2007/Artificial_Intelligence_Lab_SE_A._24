def dfs_path(maze, start, end):
    stack = [start]  # Stack for DFS
    visited = set()
    parent = {start: None}  # To reconstruct the path

    while stack:
        position = stack.pop()
        x, y = position

        if position == end:
            # Reconstruct path from end to start
            path = []
            while position is not None:
                path.append(position)
                position = parent[position]
            return path[::-1]  # Return reversed path

        if position in visited:
            continue
        visited.add(position)

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            next_pos = (new_x, new_y)

            if (0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and
                    maze[new_x][new_y] == 0 and next_pos not in visited and next_pos not in parent):
                stack.append(next_pos)
                parent[next_pos] = position

    return None  # No path found

