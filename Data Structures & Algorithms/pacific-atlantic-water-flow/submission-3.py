class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pacific_visit = set()
        atlantic_visit = set()
        pacific_q = collections.deque()
        atlantic_q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pacific_q.append((r, c))
                    pacific_visit.add((r, c))
                if r == rows - 1 or c == cols - 1:
                    atlantic_q.append((r, c))
                    atlantic_visit.add((r, c))

        def bfs(q, visit):
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr == rows or nc == cols:
                        continue
                    if (nr, nc) in visit:
                        continue
                    if heights[nr][nc] >= heights[r][c]:
                        visit.add((nr, nc))
                        q.append((nr, nc))

        bfs(pacific_q, pacific_visit)
        bfs(atlantic_q, atlantic_visit)

        both = pacific_visit.intersection(atlantic_visit)
        return [[r, c] for r, c in both]