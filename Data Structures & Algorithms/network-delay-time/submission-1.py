class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges=collections.defaultdict(list)
        for u,v,t in times:
            edges[u].append((v,t))

        minHeap=[(0,k)]
        visited=set()
        res=0

        while minHeap:
            w1,n1=heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            res=max(res,w1)

            for nei,neiW in edges[n1]:
                if nei not in visited:
                    heapq.heappush(minHeap,(neiW+w1,nei))

        return res if len(visited)==n else -1
