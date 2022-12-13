

def get_marker(end) -> tuple:
  with open('puzzle_input.txt', 'r') as f:
    datastream = f.readline()

    # start of packet marker 4 symbols
    start = 0
    not_marker = True
    # analytics for loop runs
    runs = 0

    while end != len(datastream):
        not_marker = True
        sub = datastream[start:end]
        for letter in sub:
            # add a run to investigate a letter
            runs += 1

            if sub.count(letter) > 1:
                not_marker = False
                # used for minimizing the runtime
                break

        if not_marker:
            return 'marker: ' + sub, 'end of the marker: ' + str(end), 'number of runs: ' + str(runs)

        start += 1
        end += 1


if __name__ == "__main__":
    # returns tuple with marker, end of marker and amount of loop runs
    solution1 = get_marker(4)
    print(solution1)

    # returns tuple with marker, end of marker and amount of loop runs
    solution2 = get_marker(14)
    print(solution2)