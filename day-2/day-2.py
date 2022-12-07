if __name__ == "__main__":
    total = 0
    sum_total = []

    strategies = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors",
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

    def isWinner(playerA, playerB):

        player = strategies[playerA]
        opponent = strategies[playerB]

        if player == opponent:
            return "draw"
        elif player == "Rock" and opponent == "Scissors":
            return "win"
        elif player == "Paper" and opponent == "Rock":
            return "win"
        elif player == "Scissors" and opponent == "Paper":
            return "win"
        else:
            return "lost"

    def getScore(round):
        opponent = round.split(" ")[0]
        player = round.split(" ")[1].replace("\n", "")

        final_score = (
            scores[isWinner(player, opponent)] + shapeScores[strategies[player]]
        )

        return final_score

    with open("input.txt") as f:

        output_one = 0
        for line in f.readlines():
            if line != "\n":
                output_one += getScore(line)

        print(f"Part One Output: {output_one}")
