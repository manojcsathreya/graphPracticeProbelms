class DisjointSet():
    def __init__(self,n):
        self.rank = [0 for _ in range(n+1)]
        self.parent = [i for i in range(n+1)]
        self.size = [0 for _ in range(n+1)]
    
    def find_upar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_upar(self.parent[node])
        return self.parent[node]
    
    def union_by_rank(self, u, v):
        ulp_v = self.find_upar(v)
        ulp_u = self.find_upar(u)

        if ulp_u == ulp_v:
            return
        
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v 
        elif self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def union_by_size(self,u,v):
        ulp_v = self.find_upar(v)
        ulp_u = self.find_upar(u)

        if ulp_u == ulp_v:
            return
        
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v 
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

def main():
    ds = DisjointSet(7)
    ds.union_by_size(1, 2)
    ds.union_by_size(2, 3)
    ds.union_by_size(4, 5)
    ds.union_by_size(6, 7)
    ds.union_by_size(5, 6)

    # Check if 3 and 7 are in the same set
    if ds.find_upar(3) == ds.find_upar(7):
        print("Same")
    else:
        print("Not Same")
    
    print(ds.parent)
    print(ds.rank)

    ds.union_by_size(3, 7)
    if ds.find_upar(3) == ds.find_upar(7):
        print("Same")
    else:
        print("Not Same")

    print(ds.parent)
    print(ds.rank)

if __name__ == "__main__":
    main()

        
