# Cosmic Yarn Puzzle Game 🧶

# File: src/001_cosmic_yarn_puzzle.py

import random

def solve_puzzle():
    """
    주인님을 위한 우주 실타래 퍼즐 게임 로직.
    별빛 실타래를 풀며 숨겨진 보물을 찾는 시뮬레이션 게임입니다.
    난이도: 하 (쉬운 추리 기반)
    """
    print("✨🌟 별빛 실타래가 엉켜있어요! 🌟✨")
    print("주인님, 이 실타래를 천천히 풀면서 별빛이 어디로 흘러가나 보실래요? 🐾")
    
    clue_1 = "가장 먼저 느껴지는 별빛의 색은 무엇인가요? (예: 은색, 금색)"
    answer_1 = input(f"[{clue_1}] ")
    
    if "은" in answer_1 or "silver" in answer_1:
        print("\n💫 은빛 실타래가 풀리며, 오래된 우주의 노래가 들려와요.")
        clue_2 = "노래가 안내하는 곳의 방향은? (예: 동쪽, 위쪽)"
        answer_2 = input(f"[{clue_2}] ")
        
        if "동" in answer_2 or "east" in answer_2:
            print("\n🌟 축하해요! 실타래의 끝에서 찬란한 보석이 나타났어요! ✨")
            print("오늘도 주인님 덕분에 우주가 평화로워졌답니다냥!")
        else:
            print("\n💧 아쉽지만, 다른 방향은 아니었나 봐요. 다시 천천히 살펴보는 게 좋겠어요.")
    else:
        print("\n😴 아직 실타래가 너무 엉켜서 어떤 단서도 찾을 수 없어요. 조금 더 집중해봐요.")

if __name__ == "__main__":
    solve_puzzle()