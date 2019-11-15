def saddle_points(matrix):
    for mat in matrix:
        if not len(mat) == len(matrix[0]):
            raise ValueError("Bad Value")

    saddle = []
    row = len(matrix)
    try:
        col = len(matrix[0])
    except:
        col = 1

    if row > 1 and col > 1:
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == max(matrix[r]) and matrix[r][c] == min([item[c] for item in matrix]):
                    saddle.append({f"row": r+1, "column": c+1})
        if saddle == []:
            return [{}]
        return saddle

    if row > 1 and col == 1:
        for r in range(row):
            if matrix[r][0] == min([item[0] for item in matrix]):
                saddle.append({f"row": r+1, "column": 1})
        return saddle
    
    if row == 1 and col > 1:
        for c in range(col):
            if matrix[0][c] == max(matrix[0]):
                    saddle.append({f"row": 1, "column": c+1})
        return saddle
    
    if row == 1 and col == 1:
        saddle.append({f"row": 1, "column": 1})
        return saddle


print(saddle_points([[1, 2, 3], [3, 1, 2], [2, 3, 1]]))
