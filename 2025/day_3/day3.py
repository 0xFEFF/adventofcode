def read_input(file_path: str) -> list[str]:
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
    jolt_max = 0
    for bank in data:
        joltage = ''
        current_index = 0
        while len(joltage) < 12:
            highest_value = 0
            # it is necessary to find the next 11 values that are the highest
            for j in range(current_index,len(bank)):
                if int(bank[j]) > highest_value and len(bank[j:]) + len(joltage) > 11:
                    highest_value = int(bank[j])
                    current_index = j + 1
                    #print(bank[j], j)
            
            joltage += str(highest_value)
            
        print(f"jolt {joltage}")
        jolt_max += int(joltage)

    print(f"jolt max {jolt_max}")


if __name__ == "__main__":
    print("Day 3: Lobby")

    example_data = read_input('example.txt')
    #solution_part_one(['818181911112111']) 
    #print(example_data)
    #solution_part_one(example_data) 

    solution_part_two(['987654321111111'])
    solution_part_two(example_data)

    input_data = read_input('input.txt')
    #solution_part_one(input_data)
    solution_part_two(input_data)