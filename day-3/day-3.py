from string import ascii_letters


def small_case():
    # Lowercase item types a through z have priorities 1 through 26.
    return {chr(i): (ord(chr(i)) - 97 + 1) for i in range(97, 123)}


def upper_case():
    # Uppercase item types A through Z have priorities 27 through 52
    return {chr(i): (ord(chr(i)) - 65 + 27) for i in range(65, 91)}


def getPriority(rucksack):
    matches = []
    first_compartment = rucksack[0 : len(rucksack) // 2]
    second_compartment = rucksack[len(rucksack) // 2 : len(rucksack)]
    for i in first_compartment:
        if i in second_compartment:
            if i not in matches:
                matches.append(i)

    letter_priotity = {**small_case(), **upper_case()}
    return letter_priotity[matches[0]]


if __name__ == "__main__":

    total = 0
    with open("input.txt") as f:
        for line in f.readlines():
            if line != "\n":
                total += getPriority(line)

    print(f"Part One Output: {total}")
    print(ascii_letters)
