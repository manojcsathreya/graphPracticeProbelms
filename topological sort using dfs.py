adj = {0:[], 1:[], 2:[3], 3:[1], 5:[2], 4:[1]}
visit = set()
stack = []

def dfs(node):
    if node in visit:
        return
    visit.add(node)
    for neighbours in adj[node]:
        dfs(neighbours)
    stack.append(node)

for nodes in adj:
    if nodes not in visit:
        dfs(nodes)

print(stack[::-1])
