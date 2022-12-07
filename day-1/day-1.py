if __name__ == "__main__":
    total = 0
    sum_total = []

    with open("input.txt") as f:
        for line in f.readlines():
            if line != "\n":
                line = line.replace("\n", "")
                total += int(line)
            else:
                sum_total.append(int(total))
                total = 0

    sum_total.sort(reverse=True)

    print(f"Part One Output: {sum_total[0]}")
    # Output: 69795

    print(f"Part Two Output: {sum_total[0] + sum_total[1] + sum_total[2]}")
    # Output: 208437
