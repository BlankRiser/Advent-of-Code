# https://docs.python.org/3/library/string.html#string.ascii_letters
# Change first part to use this import and to remove my custom functions later for github.
from string import ascii_letters


if __name__ == "__main__":

    total = 0
    length = 3
    with open("input.txt") as f:
        input = [line.split("\n")[0] for line in f.readlines()]

    for i in range(0, len(input), 3):
        group = input[i : i + 3]

        for priority, letter in enumerate(ascii_letters):
            if letter in group[0] and letter in group[1] and letter in group[2]:
                total += priority + 1

    print(f"Part Two Output: {total}")
    # 2434
