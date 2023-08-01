from collections import deque
adj = {1:[2],2:[3],3:[4],4:[]}
q = deque()
visit = set()
visit.add(1)
q.append((1,-1))
def bfs():
    while q:
        cur, parent  = q.popleft()
        for n in adj[cur]:
            if n not in visit:
                q.append((n,cur))
                visit.add(n)
            elif parent != n:
                return True

    return False

print(bfs())
