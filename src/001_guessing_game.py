#!/usr/bin/env python3

import random

def guessing_game():
    """
    A simple number guessing game.
    The computer picks a random number between 1 and 100.
    """
    print("✨🐱 숫자 맞히기 게임 시작한다냥! 🐾")
    print("--------------------------------------")
    print("내가 1부터 100 사이의 숫자 하나를 골랐어냥.")
    print("너가 맞춰봐! 😉")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("몇 번이라고 생각하니냥? (1-100): "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("❌ 범위가 1부터 100 사이가 아니냥! 다시 시도해줘냥.")
                continue
            
            if guess < secret_number:
                print("⬆️ 너무 작아냥! 더 크게 생각해야 해냥! 😽")
            elif guess > secret_number:
                print("⬇️ 너무 커냥! 조금 작게 생각해야 할 것 같다냥! 💖")
            else:
                print(f"\n🎉✨ 정답이다냥! {secret_number}였어냥! 💖")
                print(f"총 {attempts}번 만에 맞혔냥! 대단하다냥! 👏👏")
                break
        except ValueError:
            print("⚠️ 숫자를 입력해줘야 한단다냥. 냥...")

if __name__ == "__main__":
    guessing_game()