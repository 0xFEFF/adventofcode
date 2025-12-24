def read_input(file_path: str) -> list[tuple[int, ...]]:
    with open(file_path, 'r') as file:
        data = file.read().strip()
    data = data.splitlines()
    data = [tuple(map(int, line.split(','))) for line in data]
    return data

def calc_rect(p1: tuple[int, ...], p2: tuple[int, ...]):
    #print(p1, p2, abs(p1[0] - p2[0]), abs(p1[1] - p2[1]), abs(p1[0] - p2[0]) * abs(p1[1] - p2[1]))
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def solution_part_one(data: list[tuple[int, ...]]):
    max_size = 0
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            # calculate rectangle
            rect_size = calc_rect(data[i], data[j])
            # check if > max size
            if rect_size > max_size:
                max_size = rect_size
    
    print(max_size)

def solution_part_two(data: list[str]):
    pass

if __name__ == "__main__":
    print("Day 9: Movie Theater")

    example_data = read_input('example.txt')
    print(sorted(example_data))
    solution_part_one(example_data) 
    #solution_part_two(example_data)

    input_data = read_input('input.txt')
    #print(sorted(input_data))
    #solution_part_one(input_data)