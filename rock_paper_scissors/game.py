#!/usr/bin/env python3
import random

ICONS = {"камень": "🪨", "бумага": "📄", "ножницы": "✂️"}
CHOICES = ["камень", "бумага", "ножницы"]


class ScoreBoard:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.history = []

    def update(self, winner, user, computer):
        if winner == "Победа игрока!":
            self.player_score += 1
        elif winner == "Победа компьютера!":
            self.computer_score += 1
        # сохраняем историю
        self.history.append((user, computer, winner))

    def show(self):
        print(
            f"Счет: Игрок {self.player_score}"
            f"- Компьютер {self.computer_score}"
            )

    def show_history(self):
        if not self.history:
            print("История пустая.")
            return
        print("\nИстория ходов:")
        for i, (user, comp, winner) in enumerate(self.history, 1):
            print(
                f"{i}: Игрок {ICONS[user]} ({user}) vs "
                f"Компьютер {ICONS[comp]} ({comp}) -> {winner}"
            )
        print()


def get_computer_choice():
    return random.choice(CHOICES)


def get_user_choice():
    while True:
        choice = input(
            "Выберите камень, бумага или ножницы "
            "(или 'выход' для выхода): "
        ).strip().lower()
        if choice in ("выход", "exit"):
            return None
        if choice in CHOICES:
            return choice
        print("Неверный ввод! Попробуйте снова.\n")


def determine_winner(user, computer):
    if user == computer:
        return "Ничья"
    if (
        (user == "камень" and computer == "ножницы")
        or (user == "бумага" and computer == "камень")
        or (user == "ножницы" and computer == "бумага")
    ):
        return "Победа игрока!"
    return "Победа компьютера!"


def main_menu():
    scoreboard = ScoreBoard()
    while True:
        print("\n=== Главное меню ===")
        print("1 — Начать игру")
        print("2 — Показать историю ходов")
        print("3 — Сбросить счет")
        print("0 — Выход")
        choice = input("Выберите пункт меню: ").strip()

        if choice == "0":
            print("Выход из игры. Спасибо за игру!")
            break
        elif choice == "1":
            play_rounds(scoreboard)
        elif choice == "2":
            scoreboard.show_history()
        elif choice == "3":
            scoreboard = ScoreBoard()
            print("Счет и история сброшены.")
        else:
            print("Неверный ввод! Попробуйте снова.")


def play_rounds(scoreboard):
    print("\n=== Игра Камень-Ножницы-Бумага ===")
    while True:
        user_choice = get_user_choice()
        if user_choice is None:
            print("Возврат в главное меню.")
            break

        computer_choice = get_computer_choice()
        print(
            f"Компьютер выбрал: {ICONS[computer_choice]} ({computer_choice})"
        )

        winner = determine_winner(user_choice, computer_choice)
        print(winner)

        scoreboard.update(winner, user_choice, computer_choice)
        scoreboard.show()
        print()


if __name__ == "__main__":
    main_menu()
