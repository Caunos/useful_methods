"""
    not very much personalized.
    adjlist is dict
    all nodes is set, etc etc

    kahn's algorithm
"""


import heapq


def topologicalSort():
    # Create a vector to store indegrees of all
    # vertices. Initialize all indegrees as 0.
    in_degree = {}
    for i in allNodes:
        in_degree[i] = 0

    # Traverse adjacency lists to fill indegrees of
    # vertices.  This step takes O(V+E) time
    for i in adjDict.keys():
        for j in adjDict[i]:
            in_degree[j] = in_degree[j] + 1

    # Create an queue and enqueue all vertices with
    # indegree 0
    queue = []
    heapq.heapify(queue)
    for i in allNodes:
        if in_degree[i] == 0:
            heapq.heappush(queue, i)

            # Initialize count of visited vertices
    cnt = 0

    # Create a vector to store result (A topological
    # ordering of the vertices)
    top_order = []

    # One by one dequeue vertices from queue and enqueue
    # adjacents if indegree of adjacent becomes 0
    while queue:

        # Extract front of queue (or perform dequeue)
        # and add it to topological order
        u = heapq.heappop(queue)
        top_order.append(str(u))

        # Iterate through all neighbouring nodes
        # of dequeued node u and decrease their in-degree
        # by 1
        for i in adjDict[u]:
            in_degree[i] = in_degree[i] - 1
            # If in-degree becomes zero, add it to queue
            if in_degree[i] == 0:
                heapq.heappush(queue, i)

        cnt += 1

    # Check if there was a cycle
    if cnt != len(allNodes):
        print("There exists a cycle in the graph")
    else:
        # Print topological order
        print(" ".join(top_order))


n = int(input())
adjDict = {}
allNodes = set([])
edges = []
for _ in range(n):
    t = int(input())
    q = list(map(int, input().split()))
    for i in range(t-1):
        edges.append((q[i], q[i+1]))
        allNodes.add(q[i])
        allNodes.add(q[i+1])
for i in allNodes:
    adjDict[i] = []
for i in edges:
    adjDict[i[0]].append(i[1])
topologicalSort()


