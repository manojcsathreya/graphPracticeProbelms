# Dijkstra's Algo - TC: E logV
import heapq
adj = {
    0 :[[1,4],[2,4]],
    1:[[0,4],[2,2]],
    2:[[0,4],[1,2],[3,3],[4,1],[5,6]],
    3:[[2,3],[5,2]],
    4:[[2,1],[5,3]],
    5:[[2,6],[3,2],[4,3]],
}

def dijkstras(adj):
    minheap = [] 
    dist = [float("inf") for _ in range(len(adj))]
    heapq.heappush(minheap, [0,0])
    dist[0] = 0
    while minheap:
        distance , node = heapq.heappop(minheap)
        for neighbours, d in adj[node]:
            if distance + d < dist[neighbours]:
                dist[neighbours] = distance + d
                heapq.heappush(minheap,(dist[neighbours], neighbours))
    return dist

print(dijkstras(adj))
