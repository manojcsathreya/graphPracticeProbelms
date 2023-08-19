#Belman-Ford
edge = [[3, 2, 6], [5, 3, 1], [0, 1, 5], [1, 5, -3], [1, 2, -2], [3, 4, -2], [2, 4, 3]]

v = 6
dist = [float("inf")] * v
dist[0] = 0

for i in range(v):
    for u,v,w in edge:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
print(dist)


#Floyd Warshall
matrix = [[0, 2, -1, -1],[1, 0, 3, -1],[-1, -1, 0, -1],[3, 5, 4, 0]]

def floydWarshall(matrix):
    n = len(matrix)
    dist = [[float('inf') for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0  
            elif matrix[i][j] != -1:
                dist[i][j] = matrix[i][j]

    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
print(floydWarshall(matrix))
