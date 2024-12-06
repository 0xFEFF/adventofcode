import os  

def solve_part_1():
  with open('./puzzle-input.txt', 'r') as f:
    puzzle = f.readlines()
    
    for pair in puzzle:
      pair = pair.replace('\n', '')
      print(pair)


if __name__ == "__main__":
  solve_part_1()
