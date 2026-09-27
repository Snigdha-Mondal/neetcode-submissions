class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        fresh,secs=0,0
        q=collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append([r,c])

        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    nr,nc=dr+r,dc+c
                    if nc<0 or nc>=cols or nr<0 or nr>=rows or grid[nr][nc]!=1:
                        continue
                    q.append([nr,nc])
                    grid[nr][nc]=2
                    fresh-=1
            secs+=1

        return secs if fresh==0 else -1
