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
        print(f"Letter: {letter}, Number: {number}")
        
        # everything above 100 can be ignored since 100 is a full rotation
        if number > 100:
            number = number % 100
            print(f"Adjusted number for three digits: {number}")

        if letter == 'R':
            index += number
        elif letter == 'L':
            index -= number

        print(f"Current index: {index}")


        if index < 0:
            index = len(lock_number) - abs(index)
        if index >= len(lock_number):
            index = index % len(lock_number)
        
        print(f"fixed index: {index}")

        if lock_number[index] == 0:
            zeros += 1

    print(f"Total zeros encountered: {zeros}")
    return zeros

if __name__ == '__main__':
    lock_number = list(range(50, 100)) + list(range(0, 50))
    print(lock_number)

    test_data = ['R3', 'L55', 'R2', 'R125']
    zeros = get_lock_number(test_data)
    print(f"number of zeros: {zeros}")

    data = read_input('input.txt')
    zeros = get_lock_number(data)
    print(f"number of zeros: {zeros}")