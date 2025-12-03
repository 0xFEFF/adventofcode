def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split(',')
    return data

def solution_part_one(data : list[str]):
    sum = 0

    for item in data:
        x,y = item.split('-')
        for i in range(int(x), int(y)+1):
            num = str(i)
            if num[:len(num)//2] == num[len(num)//2:]:
                #print(num)
                sum += int(num)

    print(f"Result is {sum}")

if __name__ == "__main__":
    print("Day 2: Gift Shop")

    #example_data = read_input('example.txt')
    #solution_part_one(example_data)
    
    input_data = read_input('input.txt')
    solution_part_one(input_data)

