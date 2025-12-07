def read_input(file_path: str) -> tuple[list[str], list[str]]:
    with open(file_path, 'r') as file:
        data = file.read().strip()
    data = data.split("\n\n")
    return data[0].split('\n'), data[1].split("\n")

def check_id_in_ids(id: str, ids: list[str]) -> bool:
    #print(id)
    for i in range(len(ids)):
        start, end = map(int, ids[i].split("-"))
        #print(range(start, end+1))
        if int(id) in range(start, end+1):
            return True
    return False

def solution_part_one(ids: list[str], ingredients: list[str]):
    fresh_items = 0
    
    for ingredient in ingredients:
        if check_id_in_ids(ingredient, ids):
            fresh_items += 1

    print(f"fresh items amount {fresh_items}")


def solution_part_two(ids: list[str]):
    ranges = []
    for id_range in ids:
        start, end = map(int, id_range.split("-"))
        #print(start, end, end - start)
        ranges.append((start, end))
    
    ranges = sorted(ranges)

    sum = 0 
    cur = -1
    for s,e in ranges:
        if cur >= s:
            s = cur + 1
        if s <= e:
            sum += e-s+1
        cur = max(cur, e)


    print(f"amount valid ids {sum}")


if __name__ == "__main__":
    print("Day 5: Cafeteria")

    id_ranges, ingredients = read_input('example.txt')
    #solution_part_one(id_ranges, ingredients) 
    #solution_part_two(id_ranges)

    id_ranges, ingredients = read_input('input.txt')
    solution_part_one(id_ranges, ingredients)
    solution_part_two(id_ranges)