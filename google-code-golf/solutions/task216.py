# TODO  # TO BE DONE BY Suhrid Sadman Abrar
import json
def p(input_grid):
    rows, cols = 20, 20
    visited = [[False]*cols for _ in range(rows)]
    regions = []
    
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and input_grid[i][j] != 0:
                region = []
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    if 0<=x<rows and 0<=y<cols and not visited[x][y] and input_grid[x][y] != 0:
                        visited[x][y] = True
                        region.append((x, y, input_grid[x][y]))
                        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                            stack.append((x+dx, y+dy))
                if region:
                    regions.append(region)
    
    if not regions:
        return []
    
    largest = max(regions, key=len)
    min_i = min(x for x, y, v in largest)
    max_i = max(x for x, y, v in largest)
    min_j = min(y for x, y, v in largest)
    max_j = max(y for x, y, v in largest)
    
    result = []
    for i in range(min_i, max_i+1):
        row = []
        for j in range(min_j, max_j+1):
            row.append(input_grid[i][j])
        result.append(row)
    return result

#FLAGGED