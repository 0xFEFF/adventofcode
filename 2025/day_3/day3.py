def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split('\n')
    return data

def solution_part_one(data: list[str]):
    jolt_max = 0
    for bank in data:
        joltage = 0
        for i in range(len(bank)-1):
            if int(bank[i] + bank[i+1]) > joltage:
                joltage = int(bank[i] + bank[i+1])
            for j in range(i+1, len(bank)):
                if int(bank[i] + bank[j]) > joltage:
                    joltage = int(bank[i] + bank[j])
        
        jolt_max += joltage
    print(f"Max joltage is {jolt_max}")


def solution_part_two(data: list[str]):
    pass

if __name__ == "__main__":
    print("Day 3: Lobby")

    example_data = read_input('example.txt')
    #solution_part_one(['818181911112111']) 
    #print(example_data)
    solution_part_one(example_data) 
    solution_part_two(example_data)

    input_data = read_input('input.txt')
    solution_part_one(input_data)
    #solution_part_two(input_data)