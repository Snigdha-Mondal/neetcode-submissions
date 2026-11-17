class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        visited=set()
        minHeap=[(0,0)]
        total=0

        while len(visited)<n:
            cost,u=heapq.heappop(minHeap)
            if u in visited:
                continue
            visited.add(u)
            total+=cost

            for v in range(n):
                if v not in visited:
                    d=abs(points[u][0]-points[v][0])+abs(points[u][1]-points[v][1])
                    heapq.heappush(minHeap,(d,v))

        return total