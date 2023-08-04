import heapq

def prims(edges):
    adj = {}
    for src, dst, weight in edges:
        if src not in adj:
            adj[src] = []
        if dst not in adj:
            adj[dst] = []
        adj[src].append([dst, weight])
        adj[dst].append([src, weight])

    mst = []
    minheap = []
    visit = set()

    for neighbours, weight in adj[0]:
        heapq.heappush(minheap, [weight, 0, neighbours])
    
    visit.add(0)
    finwieght = 0
    while minheap:
        weight, src, neighbours = heapq.heappop(minheap)
        if neighbours in visit:
            continue
        finwieght += weight
        mst.append([src, neighbours])
        visit.add(neighbours)
        for neigh,w in adj[neighbours]:
            if neigh not in visit:
                heapq.heappush(minheap, [w, neighbours, neigh])
    print(finwieght)
    return mst

print(prims([[0, 1, 2], [0, 3, 6], [1, 2, 3], [1, 3, 8], [1, 4, 5], [4, 2, 7]]))
