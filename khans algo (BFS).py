from collections import deque
def bfs():
    adj = {0:[], 1:[], 2:[3], 3:[1], 5:[0,2], 4:[1,0]}
    q = deque()
    res = []
    inDegree = [0 for _ in adj]
    for nodes in adj.values():
        for j in nodes:
            inDegree[j] += 1
    for i in range(len(inDegree)):
        if inDegree[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()
        for neighbours in adj[node]:
            inDegree[neighbours] -= 1
            if inDegree[neighbours] == 0:
                q.append(neighbours)
        res.append(node)

    return res

print(bfs())
