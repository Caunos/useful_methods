"""
written for directed and weighted edges change accordingly

"""

import heapq

adj = [[(2, 8)]]  # edge destination, edge weight
n = 0  # no of nodes
visited = [False]
dist = [float('Inf')]


def prims(node):
    finalEdges = []
    visited[node] = True
    dist[node] = True
    pq = [(0, node)]
    heapq.heapify(pq)
    while pq:
        cost, nd = heapq.heappop(pq)
        if visited[nd]:
            continue
        visited[nd] = True
        for to, km in adj[nd]:
            if dist[node] + km < dist[to]:
                finalEdges.append((nd, to, km))
                dist[to] = dist[node] + km
                heapq.heappush(pq, (dist[to], to))
    return finalEdges