def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        data = file.read().strip()
    if '\n' in data:
        return data.splitlines()
    elif ',' in data:
        return data.split(',')
    else:
        raise Exception("delimiter not known, pls check the input data") 

def solution_part_one(data: list[str]):
    h = len(data)
    start = data[0].find("S")
    beam_pos = {start}
    splits = 0
    #print(start)
    for i in range(1,h):
        print(f"b {beam_pos}")
        splitter = [j for j, c in enumerate(data[i]) if c == "^"]
        print(f"s {splitter}")

        if len(splitter) != 0:
            beam_pos_temp = beam_pos.copy()
            for beam in beam_pos:
                if beam in splitter:
                    beam_pos_temp.remove(beam)
                    beam_pos_temp.add(beam + 1)
                    beam_pos_temp.add(beam - 1)
                    splits += 1
            
            beam_pos = beam_pos_temp
        
    print(splits)

        

def solution_part_two(data: list[str]):
    pass

if __name__ == "__main__":
    print("Day 7: Laboratories")

    example_data = read_input('example.txt')
    #print(example_data)
    solution_part_one(example_data) 
    #solution_part_two(example_data)

    input_data = read_input('input.txt')
    solution_part_one(input_data)
    #solution_part_two(input_data)