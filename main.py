# Author: Chetan Mitra czm5805@psu.edu
# Collaborator: Nick McCuch nmm6025@psu.edu
# Collaborator: Devansh Agarwal dqa5365@psu.edu


def run():
  num = int(input("Enter an int: "))
  sum = sum_n(num)
  print(f"sum is {sum}.")
  string = input("Enter a string: ")
  print_n(string, num)


def sum_n(n):
  if n<=1:
    return 1
  else:
    return n + sum_n(n-1)


def print_n(s, n):
  if n<=1:
    print(s)
  else:
    print(s)
    print_n(s,n-1)


if __name__ == "__main__":
  run()