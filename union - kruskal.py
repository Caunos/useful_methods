edgeList = [(8, 1, 2)]  # weight, from, to
n = 0  # no of nodes

parent = [i for i in range(n)]
size = [1 for i in range(n)]


def findParent(nd):
    if parent[nd] == nd:
        return n
    parent[nd] = findParent(parent[nd])
    return parent[nd]


def makeUnion(a, b):
    a = findParent(a)
    b = findParent(b)
    if size[b] > size[a]:
        parent[a] = parent[b]
    else:
        parent[b] = parent[a]


def find(a, b):
    return findParent(a) == findParent(b)


def kruskal(node):
    finalEdges = []
    edgeList.sort()
    for i in edgeList:
        if not find(i[1], i[2]):
            finalEdges.append(i)
            makeUnion(i[1], i[2])