def input_generator(filepath):
    with open(filepath) as list_file:
        while line := list_file.readline():
            yield line
            
def calculate_part1(filestream):
    for line in filestream:
        print(line)

def calculate_part2(filestream):
    for line in filestream:
        print(line)


if __name__ == "__main__":
    filepath = "./2024/dayX/input.txt"
    calculate_part1(input_generator(filepath))
    calculate_part2(input_generator(filepath))