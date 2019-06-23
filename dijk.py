import heapq

adj = [[(2, 8)]] # edge destination, edge weight
n = 0 #no of nodes
visited = [False]
dist = [float('Inf')]


def dijkstra(b, e):
    dist[b] = 0
    pq = [(0, b)]
    heapq.heapify(pq)
    while pq:
        cost, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        for to, km in adj[node]:
            if dist[node] + km < dist[to]:
                dist[to] = dist[node] + km
                heapq.heappush(pq, (dist[to], to))
    if dist[e] == float('Inf'):
        return "NO PATH EXISTS"
    return dist[e]