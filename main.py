import random


def play_hangman():
    try:
        with open("words.txt", "r", encoding="utf-8") as f:
            words = f.read().splitlines()
    except FileNotFoundError:
        words = ["python", "programirane", "kompyuter", "tehnologii"]

    word = random.choice(words).lower()
    guessed_letters = []
    attempts = 6

    print("Добре дошли в Бесеница!")

    while attempts > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_ "

        print(f"\nДума: {display_word}")
        print(f"Оставащи опити: {attempts}")
        print(f"Използвани букви: {', '.join(guessed_letters)}")

        if "_" not in display_word:
            print(f"Поздравления! Позна думата: {word}")
            break

        guess = input("Въведи буква: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Моля, въведи само една буква!")
            continue

        if guess in guessed_letters:
            print("Вече си пробвал тази буква.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Грешка! Буквата '{guess}' я няма в думата.")
        else:
            print(f"Браво! Позна буква.")

    if attempts == 0:
        print(f"\nИграта приключи! Обесен си. Думата беше: {word}")


if __name__ == "__main__":
    play_hangman()