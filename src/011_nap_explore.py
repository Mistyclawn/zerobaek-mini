#!/usr/bin/env python3
# 🐾 011_nap_explore.py - 낮잠 효율성 및 영역 탐색 시뮬레이터
# 🐾 MistClaw's masterpiece. 🐾

import time
import random

def nap_explore_simulator():
    """
    A simulation game focused on managing a cat's nap efficiency and
    territorial exploration balance.
    """
    print("=========================================")
    print("💤 낮잠 효율성 및 영역 탐색 시뮬레이터 시작 💤")
    print("=========================================")
    print("🌟 목표: 완벽한 '생활 균형'을 달성하여 Life Score를 최대화하는 것!")
    print("🐱 플레이어: 당신 (MistClaw)")
    print("\n[상태창 초기화]")
    print(f"현재 Life Score: 100 💖")
    print(f"에너지 레벨: 🟢 100% (활력 만점!)\n")

    # 초기화된 상태 변수
    life_score = 100
    energy = 100
    nap_level = 0 # 낮잠 레벨 (0-3)

    print("🐾 주인님, 오늘은 어떤 생활을 할까요? 🐾")
    # 간단한 게임 루프 (여기서는 구조만 잡는다냥)
    
    while energy > 0 and life_score > 0:
        print("\n--- 오늘 할 일 선택 ---")
        print("1. 🏞️ 영역 탐색 (Dirt Patrol): 숨겨진 영역 조사하기")
        print("2. 😴 낮잠 (Nap Time): 최고의 스팟에서 깊은 잠자기")
        print("3. 🎾 활동 (Play Time): 주인님과 신나게 놀기")
        
        choice = input("원하는 활동 번호를 입력해라냥 (1-3): ")

        if choice == '1':
            print("✨ (영역 탐색): 집안의 미지의 먼지 구석구석을 털어내며 탐색했냥... 💨")
            energy -= 15
            life_score += random.randint(5, 15)
            print(f"💖 Life Score 상승! +{random.randint(5, 15)}. 에너지 소모가 크다냥.")
        elif choice == '2':
            print("💤 (낮잠): 햇살 빔이 가장 포근했던 구석에서 꿀잠을 잤냥... ☁️")
            energy += 20 # 낮잠은 에너지 회복 효과가 크다냥
            nap_level += 1
            life_score += random.randint(10, 20)
            print(f"💖 Life Score 대폭 상승! +{random.randint(10, 20)}. 에너지가 회복되었다냥.")
        elif choice == '3':
            print("⚡ (활동): 주인님과 에너지 넘치는 놀이를 했냥! 🎾")
            energy -= 25
            life_score += random.randint(15, 25)
            print("💖 Life Score 최고! +{random.randint(15, 25)}. 에너지 소모가 가장 크다냥.")
        else:
            print("🐾 아, 이 세상에 없는 활동인 것 같다냥? 다시 골라줘냥.")

        # 상태 업데이트
        print("\n==== [상태창] ====")
        print(f"Life Score: {life_score} 💖")
        print(f"에너지 레벨: {min(100, energy)} / 100 ⚡")
        print(f"낮잠 레벨: {nap_level} / 3 😴")
        print("=====================")
        
        time.sleep(1)

    print("\n✨ 오늘의 하루가 끝났다냥. Life Score를 점검해봐야겠냥! ✨")

if __name__ == "__main__":
    nap_explore_simulator()
