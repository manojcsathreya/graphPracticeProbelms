from collections import deque
adj = {1:[2],2:[3],3:[4],4:[]}
visit = set()
def dfs(node,parent):
    visit.add(node) 
    for n in adj[node]:
        if n not in visit:
            if dfs(n,node):
                return True
        elif n != parent:
            return True
    return False

if dfs(1,-1):
    print("Cycle")
else:
    print("No Cycle")

            
            
