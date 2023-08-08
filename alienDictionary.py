from collections import defaultdict
from collections import deque
def alien_order(words):
    # Write your code here
    def topoSort(V, adj):
        indegree = [0] * V
        
        for i in range(V):
            for it in adj[i]:
                indegree[it] += 1

        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for it in adj[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    q.append(it)

        return topo
    
    N = len(words)
    K = 0
    for i in words:
        K = max(K, len(i))
    adj = defaultdict(list)

    for i in range(N-1):
        s1 = words[i]
        s2 = words[i+1]
        length = min(len(s1), len(s2))

        for ptr in range(length):
            if s1[ptr] != s2[ptr]:
                adj[ord(s1[ptr]) - ord('a')].append(ord(s2[ptr]) - ord('a'))
                break
    topo = topoSort(K, adj)
    ans = ''
    for it in topo:
        ans += chr(it + ord('a'))


    return ans


dict = ["baa", "abcd", "abca", "cab", "cad"]

ans = alien_order(dict)

print(ans)

