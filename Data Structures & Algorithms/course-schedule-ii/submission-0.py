class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj={i:[] for i in range(numCourses)}
        indegree=[0]*numCourses
        for crs,pre in prerequisites:
            indegree[crs]+=1
            adj[pre].append(crs)

        res=[]

        def dfs(node):
            res.append(node)
            indegree[node]-=1
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    dfs(nei)


        for crs in range(numCourses):
            if indegree[crs]==0:
                dfs(crs)

        return res if len(res)==numCourses else []