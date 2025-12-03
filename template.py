def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split(',')
    return data

def solution_part_one(data: list[str]):
    pass

def solution_part_two(data: list[str]):
    pass

if __name__ == "__main__":
    print("Day 2: Gift Shop")

    example_data = read_input('example.txt')
    solution_part_one(example_data) 
    solution_part_two(example_data)

    input_data = read_input('input.txt')
    solution_part_one(input_data)
    solution_part_two(input_data)