class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        fresh=0
        q=collections.deque()

        def addGrid(r,c):
            nonlocal fresh
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!=1:
                return
            grid[r][c]=2
            q.append((r,c))
            fresh-=1
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1

        secs=0
        while q and fresh>0:
            secs+=1
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=2
                addGrid(r+1,c)
                addGrid(r-1,c)
                addGrid(r,c-1)
                addGrid(r,c+1)

        return secs if fresh==0 else -1

        

