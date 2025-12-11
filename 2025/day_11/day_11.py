def read_input(file_path: str) -> dict[str, list[str]]:
    with open(file_path, 'r') as file:
        data = file.read().strip()
        data = data.splitlines()
        di: dict[str, list[str]] = {}
        for e in data:
            #print(e.split(":"))
            k,v = e.split(":")
            v = v.strip().split(' ')
            di[k] = v

    return di


def solution_part_one(data: dict[str, list[str]]):
    searching: bool = True
    ways: list[str] = []
    while searching:
        searching = False



def solution_part_two(data: list[str]):
    pass

if __name__ == "__main__":
    print("Day X: ")

    example_data = read_input('example.txt')
    print(example_data['you'])
    #solution_part_one(example_data) 
    #solution_part_two(example_data)

    #input_data = read_input('input.txt')
    #solution_part_one(input_data)
    #solution_part_two(input_data)