#https://app.codesignal.com/interview-practice/task/SKZ45AF99NpbnvgTn
#passed time limit
def sudoku2(grid):
    def isNotValid(a):
        return len(a) != len(set(a))
    for i,x in enumerate(grid):
        if isNotValid([a for a in x if a != '.']):
            return False 
        if isNotValid([grid[j][i] for j in range(len(grid)) if grid[j][i] != '.']):
            return False
    for i in range(0,3):
        for j in range(0,3):
            a = []
            for k in range(0,3):
                a.extend(grid[k+3*i][j*3:j*3+3])
            if isNotValid([e for e in a if e != '.']):
                return False
    return True