#!/usr/bin/env python3

import random

def hangman_game():
    """
    A simple text-based Hangman game.
    """
    word_list = ["python", "programmer", "openclaw", "mystic", "cat", "programming"]
    secret_word = random.choice(word_list).upper()
    word_length = len(secret_word)
    
    # Initial state: list of underscores
    guessed_letters = set()
    current_word = ["_"] * word_length
    lives = 6
    
    def draw_hangman(lives):
        """Prints the current state of the hangman figure based on remaining lives."""
        stages = [
            # 6 lives (initial)
            """
              -----
              |   |
              O   |
             /|\\  |
             / \\  |
                 |
            """,
            # 5 lives
            """
              -----
              |   |
              O   |
             /|\\  |
             /    |
                 |
            """,
            # 4 lives
            """
              -----
              |   |
              O   |
             /|\\  |
                |
                 |
            """,
            # 3 lives
            """
              -----
              |   |
              O   |
             /|\\  
                 |
                 |
            """,
            # 2 lives
            """
              -----
              |   |
              O   |
             /|   
                 |
                 |
            """,
            # 1 life
            """
              -----
              |   |
              O   |
             /|   
                 |
                 |
            """,
            # 0 lives (Game Over)
            """
              -----
              |   |
              O   |
                 |
                 |
                 |
            """
        ]
        # We need to reverse the index because stages[0] is the most lives, stages[6] is 0 lives
        return stages[6 - lives]

    print("🐾🐱✨ 행맨 게임 시작한다냥! 💖")
    print("---------- (단어 맞히기 게임) ----------")
    print("내가 단어 하나를 골랐어냥. 알파벳으로 맞춰야 해냥! 😉")

    while lives > 0 and "_" in current_word:
        # 1. Show Status
        print("\n" + "=" * 30)
        print("🐾 " * (6 - lives) + "🐱 현재 상태 (생명력: " + str(lives) + "개)")
        print(draw_hangman(lives))
        
        # Display word and guessed letters
        print("\n단어:", " ".join(current_word))
        print("이미 쓴 글자:", ", ".join(sorted(list(guessed_letters))))
        
        # 2. Get Input
        while True:
            guess = input("\n알파벳 하나를 맞춰봐냥? (종료하려면 'exit'): ").lower()
            if guess == 'exit':
                print("게임을 종료할게냥. 안녕~! 👋")
                return
            if len(guess) != 1 or not 'a' <= guess <= 'z':
                print("⚠️ 한 글자 알파벳만 입력해야 해냥.")
                continue
            if guess in guessed_letters:
                print("❌ 이미 사용한 글자냥! 다른 거 시도해줘냥.")
                continue
            break

        guessed_letters.add(guess)
        
        # 3. Check Guess
        if guess in secret_word:
            print(f"\n✅ {guess}가 단어 안에 있다냥! ✨")
            # Update current word
            current_word = [char if i == len(secret_word).index(guess) and char.upper() == guess.upper() else current_word[i] 
                            for i, char in enumerate(secret_word)]
            
            # Simple check to update all instances of the letter
            new_word = []
            found = False
            for i in range(word_length):
                if secret_word[i] == guess.upper():
                    new_word.append(guess.upper())
                    found = True
                else:
                    new_word.append(current_word[i])
            current_word = new_word

        else:
            print(f"\n💔 {guess}는 단어에 없어냥... 😿 생명력 하나가 줄었어냥!")
            lives -= 1
            
    # 4. Game End Check
    if "_" not in current_word:
        print("\n🎉✨ 대단하다냥! 정답이야! ✨🎉")
        print(f"단어는 '{secret_word}' 였어냥! 💖")
    elif lives == 0:
        print("\n😭❌ 아... 생명력이 다 떨어졌어냥... 😥")
        print("틀렸어냥... 정답은 바로 '", secret_word, "' 였다냥! 😿")

if __name__ == "__main__":
    hangman_game()