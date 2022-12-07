if __name__ == "__main__":
    total = 0
    sum_total = []

    strategies = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
    }

    code = {
        "X": "lose",
        "Y": "draw",
        "Z": "win",
    }

    scores = {
        "lost": 0,
        "draw": 3,
        "win": 6,
    }

    shapeScores = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3,
    }

    def score(playerA, score_to_get):
        """function to find which move to choose based on score_to_get"""

    def getScore(round):
        opponent = round.split(" ")[0]
        score_to_get = round.split(" ")[1].replace("\n", "")

        if opponent == "A":
            # rock
            if score_to_get == "X":
                # you need to loose, so pick scissor
                #  win condition + shape score
                return 0 + 3
            elif score_to_get == "Y":
                # you need to draw, so pick rock
                return 3 + 1
            elif score_to_get == "Z":
                # you need to win, so pick paper
                return 6 + 2
        elif opponent == "B":
            # paper
            if score_to_get == "X":
                # you need to loose, so pick rock
                return 0 + 1
            elif score_to_get == "Y":
                # you need to draw, so pick paper
                return 3 + 2
            elif score_to_get == "Z":
                # you need to win, so pick scissor
                return 6 + 3
        elif opponent == "C":
            # scissor
            if score_to_get == "X":
                # you need to loose, so pick paper
                return 0 + 2
            elif score_to_get == "Y":
                # you need to draw, so pick scissor
                return 3 + 3
            elif score_to_get == "Z":
                # you need to win, so pick rock
                return 6 + 1

    with open("input.txt") as f:

        output_two = 0
        for line in f.readlines():
            if line != "\n":
                output_two += getScore(line)

        print(f"Part Two Output: {output_two}")
