class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj=collections.defaultdict(list)
        for src,dst in sorted(tickets,reverse=True):
            adj[src].append(dst)

        stack=["JFK"]
        route=[]

        while stack:
            while adj[stack[-1]]:
                stack.append(adj[stack[-1]].pop())
            route.append(stack.pop())

        return route[::-1]