import re

def read_input():
    with open("./2024/day3/input.txt") as list_file:
        while line := list_file.readline():
            yield line

if __name__ == "__main__":
    s = 0
    for line in read_input():
        mul = re.findall("mul\(\d{1,3},\d{1,3}\)", line)

        for entry in mul:
            pattern = r"mul\((\d+),(\d+)\)"

            match = re.search(pattern, entry)
            if match:
                s += int(match.group(1)) * int(match.group(2))  
            
    print(s)
