import os

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

def calc_distance_list(l,r):
    diff = []
    for i in range(len(r)):
        diff.append(abs(l[i] - r[i]))

    return sum(diff)

def calc_similarity(l,r):
    s = 0
    for v in l:
        s += v*  r.count(v)
    
    return s

if __name__ == "__main__":
    l,r = calc_sorted_list()

    print(f"distance is: {calc_distance_list(l,r)}")
    print(f"similarity is: {calc_similarity(l,r)}")