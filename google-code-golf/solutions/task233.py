# TODO  # TO BE DONE BY Suhrid Sadman Abrar
def p(input_grid):
    rows,cols=len(input_grid),len(input_grid[0])
    r1=r2=c1=c2=-1
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c]==2:
                if r1<0:r1=r
                r2=r
                if c1<0 or c<c1:c1=c
                if c2<0 or c>c2:c2=c
    return [row[c1:c2+1] for row in input_grid[r1:r2+1]]
#FLAGGED