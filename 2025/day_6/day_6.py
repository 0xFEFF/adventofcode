import re
import math

def read_input(file_path: str) -> tuple[list[str], list[str]]:
    fixed = []
    with open(file_path, 'r') as file:
        data = file.read().split('\n')

    for line in data:
        line = line.strip()
        fixed.append(re.sub(r'\s+', ' ', line).split(' '))
    return fixed, data
    

def solution_part_one(data: list[str]):
    h = len(data)
    w = len(data[0])
    sum = 0
    for i in range(w):
        part = 0
        if data[h-1][i] == '*':
            part = 1
            for j in range(h-1):
                #print(int(data[j][i]))
                part *= int(data[j][i])
        else:
            part = 0
            for j in range(h-1):
                part += int(data[j][i])
        
        #print(part)
        sum += part
    print(sum)


def solution_part_two(data: list[str]):
    h = len(data)
    w = len(data[0])
    #print(h, w)
    res = 0
    numbers = []
    for i in range(w-1,-1,-1):
        #print("".join([data[0][i], data[1][i], data[2][i]]))
        number = ''
        for j in range(h-1):
            number += data[j][i]

        #print(i, j, len(number))
        if len(number) == number.count(' '):
            continue

        if data[h-1][i] == '*':
            numbers.append(int(number.strip()))
            res += math.prod(numbers)
            numbers = []
        elif data[h-1][i] == '+':
            numbers.append(int(number.strip()))
            res += sum(numbers)
            numbers = []
        else:
            numbers.append(int(number.strip()))
        #print(numbers, res)
    print(res)

if __name__ == "__main__":
    print("Day X: ")

    example_data, raw_example_data = read_input('example.txt')
    print(raw_example_data)
    #solution_part_one(example_data) 
    solution_part_two(raw_example_data)

    fixed_input_data, raw_input_data = read_input('input.txt')
    #solution_part_one(fixed_input_data)
    solution_part_two(raw_input_data)