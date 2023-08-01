from collections import deque
edges = [[1,0],[2,1],[0,3],[3,7],[3,4],[7,4],[7,6],[4,5],[4,6],[6,5]]
adj = {}
for src,dst in edges:
    if src not in adj:
        adj[src] = []
    if dst not in adj:
        adj[dst] = []
    adj[src].append(dst)
    adj[dst].append(src)
q = deque()
q.append((0,0))
distance = [float("inf")] * len(adj)
distance[0] = 0
while q:
    for i in range(len(q)):
        cur, dist = q.popleft()
        for neighbours in adj[cur]:
            if 1+dist < distance[neighbours]:
                distance[neighbours] = 1+dist
                q.append((neighbours, 1+dist))

print(distance)
