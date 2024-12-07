def input_generator(filepath):
    with open(filepath) as list_file:
        while line := list_file.readline():
            yield line
            
def calculate_part1(filestream):
    s=0
    for line in filestream:
        report = [int(x) for x in line.split()]
        diff = [report[i]-report[i+1] for i in range(len(report)-1)]
        if set(diff).issubset({1,2,3}) or set(diff).issubset({-1,-2,-3}):
            s += 1
    print(s)

def calculate_part2(filestream):
    c=0
    for line in filestream:
        c+= 1
        report = [int(x) for x in line.split()]
        diff = [report[i]-report[i+1] for i in range(len(report)-1)]
        print(report, diff)

        if c == 20:
            break



if __name__ == "__main__":
    filepath = "./2024/day2/input.txt"
    #calculate_part1(input_generator(filepath))
    calculate_part2(input_generator(filepath))
