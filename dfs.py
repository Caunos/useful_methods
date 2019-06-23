adj = [[(1, 2, 8)]]  # from, to, edge weight
n = 0  # no of nodes
visited = [False]

def dfs(v):
    stack = [[0, i[0], i[1]]for i in adj[v]]
    while stack:
        a = stack.pop()
        visited[a[1]] = True
        for i in adj[a[1]]:
            if not visited[i[0]]:
                stack.append([dist[a[1]], i[0], i[1]])
    return [max(dist), dist.index(max(dist))]