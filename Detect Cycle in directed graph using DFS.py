adj = {1:[2],2:[3], 3:[4], 4:[]}
visit = set()
pathVisit = set()

def dfs(node,parent):
    visit.add(node)
    for neighbour in adj[node]:
        if neighbour not in visit:
            if dfs(neighbour, node):
                return True
        elif parent != neighbour:
            return True
    return False

print("No Cycle") if not dfs(1,-1) else print("Cycle")
