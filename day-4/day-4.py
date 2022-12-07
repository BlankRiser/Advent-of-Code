def is_same_range(pairs):
    pair_one, pair_two = pairs.split(",")

    section_one = [int(i) for i in pair_one.split("-")]
    section_two = [int(i) for i in pair_two.split("-")]

    if section_one[0] <= section_two[0] and section_one[1] >= section_two[1]:
        return True
    elif section_two[0] <= section_one[0] and section_two[1] >= section_one[1]:
        return True
    else:
        return False


def has_overlapping_range(pairs):
    pair_one, pair_two = pairs.split(",")

    section_one = [int(i) for i in pair_one.split("-")]
    section_two = [int(i) for i in pair_two.split("-")]

    if section_one[0] in range(section_two[0], section_two[1] + 1) or section_one[
        1
    ] in range(section_two[0], section_two[1] + 1):
        return True
    elif section_two[0] in range(section_one[0], section_one[1] + 1) or section_two[
        1
    ] in range(section_one[0], section_one[1] + 1):
        return True
    else:
        return False


if __name__ == "__main__":
    with open("input.txt") as f:
        input = [line.split("\n")[0] for line in f.readlines()]

    output_one = 0
    output_two = 0

    for pairs in input:
        if is_same_range(pairs):
            output_one += 1
        if has_overlapping_range(pairs):
            output_two += 1

    print(f"Part One Output: {output_one}")
    print(f"Part Two Output: {output_two}")
