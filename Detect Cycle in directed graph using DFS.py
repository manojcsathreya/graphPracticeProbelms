adj = {1:[2],2:[3,4], 3:[5], 4:[5], 5:[]}
visit = set()
pathVisit = set()

def dfs(node,parent):
    visit.add(node)
    pathVisit.add(node)
    for neighbour in adj[node]:
        if neighbour not in visit:
            if dfs(neighbour, node):
                return True
        elif neighbour in pathVisit:
            return True
    pathVisit.remove(node)
    return False

print("No Cycle") if not dfs(1,-1) else print("Cycle")
