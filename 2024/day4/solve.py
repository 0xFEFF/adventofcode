import numpy as np

def count_xmas_horizontal(arr):
    s = 0
    for line in arr:
        m = "".join(line)
        s += m.count("XMAS")
        s += m[::-1].count("XMAS")
    return s

def count_xmas_diagonal(arr):
    s = 0
    print(arr.shape)
    for i in range (arr.shape[0]-3):
        for j in range (arr.shape[1]-3):
            word = arr[i][j] + arr[i+1][j+1] + arr[i+2][j+2] + arr[i+3][j+3]

            if word == "XMAS":
                s += 1
            if word[::-1] == "XMAS":
                s += 1

    print("backwards")
    print(arr.shape[0]-1)
    for i in range(arr.shape[0]-3):
        for j in range(arr.shape[1]-1,2,-1):
            word = arr[i][j] + arr[i+1][j-1] + arr[i+2][j-2] + arr[i+3][j-3]
            print(word)
            if word == "XMAS":
                s += 1
            if word[::-1] == "XMAS":
                s += 1
    return s

if __name__ == "__main__":
    filepath = "./2024/day4/input.txt"
    s = 0
    with open(filepath) as read_file:
        # horizontal
        rows = np.array([list(row) for row in read_file.read().split("\n")])
        s += count_xmas_horizontal(rows)
        # vertical
        rot90_rows = np.rot90(rows,k=3)
        s += count_xmas_horizontal(rot90_rows)
        # diagonal
        s += count_xmas_diagonal(rows)
        print(s)



