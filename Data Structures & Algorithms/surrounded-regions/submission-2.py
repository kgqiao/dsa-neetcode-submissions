class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #matrix
        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visit = set() #Initialize visited set for record, no duplicates
        not_surrounded = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r == 0 or c == 0 or r == rows-1 or c == cols-1): #if cell is a O and an edge
                    q.append((r,c))
                    not_surrounded.add((r,c))
    
        #view all "O" edge cells to review which of their O neighbors are also not surrounded
        while q:
            r, c = q.popleft()
            for dr, dc in directions: #review to see what neighbors can be reached by the edge cells
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # FIX 2: Only process unvisited 'O' cells
                    if board[nr][nc] == "O" and (nr, nc) not in not_surrounded:
                        not_surrounded.add((nr, nc))
                        q.append((nr, nc)) # FIX 3: Append neighbor (nr, nc), not (r, c)
        
        # Step 3: Flip all cells not connected to the border
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in not_surrounded:
                    board[r][c] = "X"