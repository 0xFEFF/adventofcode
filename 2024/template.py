def calc_sorted_list():
    l,r = [],[]
    with open("./2024/day1/input.txt") as list_file:
        while line := list_file.readline():
            #print(line)
            l.append(int(line.split()[0]))
            r.append(int(line.split()[1]))
    l.sort()
    r.sort()
    return l,r

if __name__ == "__main__":
    l,r = calc_sorted_list()

    print(f"distance is: {calc_distance_list(l,r)}")
    print(f"similarity is: {calc_similarity(l,r)}")