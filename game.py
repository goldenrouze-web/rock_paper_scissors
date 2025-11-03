import random


class ScoreBoard:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0

    def update(self, winner):
        if winner == "Победа игрока!":
            self.player_score += 1
        elif winner == "Победа компьютера!":
            self.computer_score += 1

    def show(self):
        print(
            f"Счет: Игрок {self.player_score} "
            f"- Компьютер {self.computer_score}"
        )


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def get_user_choice():
    choice = input(
        "Выберите rock, paper или scissors "
        "(или 'exit' для выхода): "
    ).lower()
    if choice == "exit":
        return None
    if choice not in ["rock", "paper", "scissors"]:
        print("Неверный ввод!")
        return get_user_choice()
    return choice


def determine_winner(user, computer):
    if user == computer:
        return "Ничья"
    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        return "Победа игрока!"
    else:
        return "Победа компьютера!"


def main():
    print("=== Игра Камень-Ножницы-Бумага ===")
    scoreboard = ScoreBoard()
    while True:
        user_choice = get_user_choice()
        if user_choice is None:
            print("Выход из игры")
            break
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        print(f"Компьютер выбрал: {computer_choice}")
        print(winner)
        scoreboard.update(winner)
        scoreboard.show()
        print()


if __name__ == "__main__":
    main()
