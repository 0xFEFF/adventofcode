def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split('\n')
    return data

def get_lock_number(data: list[str]) -> int:
    index = 0
    zeros = 0
    for line in data:
        letter = line[0]
        number = int(line[1:])
        #print(f"Letter: {letter}, Number: {number}")
        
        # everything above 100 can be ignored since 100 is a full rotation
        if number > 100:
            number = number % 100
            #print(f"Adjusted number for three digits: {number}")

        if letter == 'R':
            index += number
        elif letter == 'L':
            index -= number

        #print(f"current index: {index}")
        
        if index < 0:
            index = len(lock_number) - abs(index)
        if index >= len(lock_number):
            index = index % len(lock_number)
        
        #print(f"fixed index: {index} and number: {lock_number[index]}")

        if lock_number[index] == 0:
            zeros += 1

    print(f"Total zeros encountered at the end of rotation for part one: {zeros}")

def get_lock_number_part_two(data: list[str]) -> int:
    index = 0
    zeros = 0

    for line in data:
        letter = line[0]
        number = int(line[1:])
        #print(f"Letter: {letter}, Number: {number}")

        for step in range(1,number+1):
            if letter == 'R':
                index = index + 1
            elif letter == 'L':
                index = index - 1

            #print(f"current step: {step}, current index: {index}")

            if index < 0:
                index = len(lock_number) - abs(index)

            if index >= len(lock_number):
                index = index % len(lock_number)

            if lock_number[index] == 0:
                zeros += 1
                #print(f"current index: {index} and number: {lock_number[index]}")

    print(f"Total zeros encountered at the end of rotation for part two: {zeros}")



if __name__ == '__main__':
    lock_number = list(range(50, 100)) + list(range(0, 50))

    #test_data = ['R3', 'L55', 'R2', 'R125']
    #get_lock_number(test_data)

    # 1031 is the result
    data = read_input('input.txt')
    get_lock_number(data)

    #test_data_rotation = read_input('example.txt')
    #get_lock_number_part_two(test_data_rotation)

    # 5831 is the result
    data = read_input('input.txt')
    get_lock_number_part_two(data)