def solve_part_1():
    with open('puzzle_input.txt', 'r') as f:
        datastream = f.readlines()

        cmd = []
        file = []
        directory = []

        for line in datastream:
            line = line.replace('\n', '')

            if line[0].isdigit():
                file.append(line)
            elif line[0] == '$':
                cmd.append(line)
            else:
                directory.append(line)
        
        return cmd, file, directory

def solve_part_2():
    pass
    with open('puzzle_input.txt', 'r') as f:
        datastream = f.readline()


if __name__ == "__main__":
    # returns 
    solution1 = solve_part_1()
    print(solution1)

    # returns 
    solution2 = solve_part_2()
    print(solution2)