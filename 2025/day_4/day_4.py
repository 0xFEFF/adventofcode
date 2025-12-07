def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        data = file.read().strip().split('\n')
    return data

def solution_part_one(data: list[str]):
    sum = 0
    rows = len(data)

    for i in range(rows):
        # edge case is the first and the last row and also the first and the last element in the row since there is one missing
        if i == 0:
            exclude_previous_row = True
            exclude_following_row = False
        elif i == (rows - 1):
            exclude_previous_row = False
            exclude_following_row = True
        else:
            exclude_previous_row = False
            exclude_following_row = False
            
        columns = len(data[i])
        for j in range(columns):
            if data[i][j] == ".":
                continue
            if j == 0:
                exclude_previous_column = True
                exclude_following_column = False
            elif j == rows - 1:
                exclude_previous_column = False
                exclude_following_column = True
            else:
                exclude_previous_column = False
                exclude_following_column = False
                

            rolls_adj = ''
            #print(i, j, data[i])
            #print(f"epr {exclude_previous_row}, efr {exclude_following_row}, epc {exclude_previous_column}, efc {exclude_following_column}")
            if exclude_previous_row and exclude_previous_column:
                
                rolls_adj += data[i][j+1]
                rolls_adj += data[i+1][j]
                rolls_adj += data[i+1][j+1]

            elif exclude_previous_row and exclude_following_column:
                
                rolls_adj += data[i][j-1]
                rolls_adj += data[i+1][j]
                rolls_adj += data[i+1][j-1]

            elif exclude_previous_row:
                rolls_adj += data[i][j-1]
                rolls_adj += data[i][j+1]
                rolls_adj += data[i+1][j-1]
                rolls_adj += data[i+1][j]
                rolls_adj += data[i+1][j+1]

            elif exclude_following_row and exclude_previous_column:
                rolls_adj += data[i-1][j]
                rolls_adj += data[i-1][j+1]
                rolls_adj += data[i][j+1]

            elif exclude_following_row and exclude_following_column:
                rolls_adj += data[i-1][j]
                rolls_adj += data[i-1][j-1]
                rolls_adj += data[i][j-1]

            elif exclude_previous_column:
                rolls_adj += data[i][j+1]
                rolls_adj += data[i+1][j+1]
                rolls_adj += data[i+1][j]
                rolls_adj += data[i-1][j+1]
                rolls_adj += data[i-1][j]

            elif exclude_following_column:
                rolls_adj += data[i][j-1]
                rolls_adj += data[i+1][j-1]
                rolls_adj += data[i+1][j]
                rolls_adj += data[i-1][j-1]
                rolls_adj += data[i-1][j]

            elif exclude_following_row:
                rolls_adj += data[i][j-1]
                rolls_adj += data[i][j+1]
                rolls_adj += data[i-1][j-1]
                rolls_adj += data[i-1][j]
                rolls_adj += data[i-1][j+1]
            else:
                rolls_adj += data[i][j-1]
                rolls_adj += data[i][j+1]
                rolls_adj += data[i-1][j-1]
                rolls_adj += data[i-1][j]
                rolls_adj += data[i-1][j+1]
                rolls_adj += data[i+1][j-1]
                rolls_adj += data[i+1][j]
                rolls_adj += data[i+1][j+1]

            #print(rolls_adj)
            if rolls_adj.count('@') < 4:
                sum += 1

    print(f"amount of roles {sum}")


def solution_part_two(data: list[str]):
    check_row_index = 0 
    amount_rows = len(data)
    moved_rolls = 0

    while check_row_index < amount_rows:
        #print(f"current row index {check_row_index}")
        rolls_moved = False

        if check_row_index == 0:
            exclude_previous_row = True
            exclude_following_row = False
        elif check_row_index == (amount_rows - 1):
            exclude_previous_row = False
            exclude_following_row = True
        else:
            exclude_previous_row = False
            exclude_following_row = False

        columns = len(data[check_row_index])
        for j in range(columns):
            if data[check_row_index][j] == ".":
                continue
            if j == 0:
                exclude_previous_column = True
                exclude_following_column = False
            elif j == amount_rows - 1:
                exclude_previous_column = False
                exclude_following_column = True
            else:
                exclude_previous_column = False
                exclude_following_column = False
                

            rolls_adj = ''
            #print(i, j, data[i])
            #print(f"epr {exclude_previous_row}, efr {exclude_following_row}, epc {exclude_previous_column}, efc {exclude_following_column}")
            if exclude_previous_row and exclude_previous_column:
                
                rolls_adj += data[check_row_index][j+1]
                rolls_adj += data[check_row_index+1][j]
                rolls_adj += data[check_row_index+1][j+1]

            elif exclude_previous_row and exclude_following_column:
                
                rolls_adj += data[check_row_index][j-1]
                rolls_adj += data[check_row_index+1][j]
                rolls_adj += data[check_row_index+1][j-1]

            elif exclude_previous_row:
                rolls_adj += data[check_row_index][j-1]
                rolls_adj += data[check_row_index][j+1]
                rolls_adj += data[check_row_index+1][j-1]
                rolls_adj += data[check_row_index+1][j]
                rolls_adj += data[check_row_index+1][j+1]

            elif exclude_following_row and exclude_previous_column:
                rolls_adj += data[check_row_index-1][j]
                rolls_adj += data[check_row_index-1][j+1]
                rolls_adj += data[check_row_index][j+1]

            elif exclude_following_row and exclude_following_column:
                rolls_adj += data[check_row_index-1][j]
                rolls_adj += data[check_row_index-1][j-1]
                rolls_adj += data[check_row_index][j-1]

            elif exclude_previous_column:
                rolls_adj += data[check_row_index][j+1]
                rolls_adj += data[check_row_index+1][j+1]
                rolls_adj += data[check_row_index+1][j]
                rolls_adj += data[check_row_index-1][j+1]
                rolls_adj += data[check_row_index-1][j]

            elif exclude_following_column:
                rolls_adj += data[check_row_index][j-1]
                rolls_adj += data[check_row_index+1][j-1]
                rolls_adj += data[check_row_index+1][j]
                rolls_adj += data[check_row_index-1][j-1]
                rolls_adj += data[check_row_index-1][j]

            elif exclude_following_row:
                rolls_adj += data[check_row_index][j-1]
                rolls_adj += data[check_row_index][j+1]
                rolls_adj += data[check_row_index-1][j-1]
                rolls_adj += data[check_row_index-1][j]
                rolls_adj += data[check_row_index-1][j+1]
            else:
                rolls_adj += data[check_row_index][j-1]
                rolls_adj += data[check_row_index][j+1]
                rolls_adj += data[check_row_index-1][j-1]
                rolls_adj += data[check_row_index-1][j]
                rolls_adj += data[check_row_index-1][j+1]
                rolls_adj += data[check_row_index+1][j-1]
                rolls_adj += data[check_row_index+1][j]
                rolls_adj += data[check_row_index+1][j+1]

            #print(rolls_adj)
            if rolls_adj.count('@') < 4:
                moved_rolls += 1
                # replace all found rolls with #
                char_seq = [char for char in data[check_row_index]]
                char_seq.pop(j)
                char_seq.insert(j, ".")
                data[check_row_index] = "".join(char_seq)
                rolls_moved = True
               
        if rolls_moved:
            if check_row_index != 0:
                check_row_index -= 1
            else:
                continue
        else:
            check_row_index += 1     

    print(f"moved rolls {moved_rolls}")



if __name__ == "__main__":
    print("Day 4: Printing Department")

    #example_data = read_input('example.txt')
    #solution_part_one(example_data) 
    #solution_part_two(example_data)

    #part two 
    # if there is a change in the row there need to be a recheck
    # if there is a previous row this needs to be prechecked before 
    # if not then the move goes on

 
    input_data = read_input('input.txt')
    solution_part_one(input_data)
    solution_part_two(input_data)
    