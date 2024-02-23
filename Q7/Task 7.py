def isSafe(arr, row, col, n):
    for i in range(row):
        if arr[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if arr[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if arr[i][j] == 1:
            return False
    return True


def nQueen(arr, row, n):
    if row >= n:
        return True
    for col in range(n):
        if isSafe(arr, row, col, n):
            arr[row][col] = 1
            if nQueen(arr, row + 1, n):
                return True
            arr[row][col] = 0
    return False


n = int(input("Enter Value Of N: "))
arr = [[0] * n for _ in range(n)]
if nQueen(arr, 0, n):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()