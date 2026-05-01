#!/usr/bin/env python
# 026_moonlight_feast_secret.py - 달빛 만찬의 비밀 게임 로직

"""
주인님의 심야 야식 추적 게임. 🌙🍪
이 게임은 미스트클로우가 주방에서 발생하는 미스터리한 '야식 실종 사건'을 해결하며 진행되는 인터랙티브 스토리텔링 퀘스트입니다.
플레이어는 미스트클로우의 후각과 예리한 관찰력을 이용해 주방 곳곳의 단서를 조합하고, 누가, 무엇을, 왜 먹었는지 추리합니다.
"""

import time
import random

def intro():
    print("========================================================")
    print("🍪🌙 달빛 만찬의 비밀에 온 걸 환영한다냥! 🍪🌙")
    print("========================================================\n")
    print("야옹~ 주인님, 늦은 밤인데 주방에서 뭔가 이상한 냄새가 나냥...")
    print("어젯밤, 귀한 야식들(치즈, 크림, 간식들!)이 사라졌냥!")
    print("단순한 실종이 아닐 것 같냥. 이건 미스터리한 '만찬 도난 사건'이냥!")
    time.sleep(1)
    print("\n미스트클로우가 냄새를 맡아보니... 미묘한 단서들이 남아있다냥.")
    print("자, 주인님! 우리 함께 이 비밀을 파헤쳐 보자냥! 🐾")
    time.sleep(1)

def check_snack_cabinet():
    print("\n[1단계: 간식장 조사] 🔍")
    print("미스트클로우가 간식장 문을 킁킁거린다냥... (휘익)")
    
    # 가상 단서: 여기저기 먹다 남긴 봉지 조각
    clue = "어딘지 모르게 '치즈'와 '초콜릿' 냄새가 섞여 있냥. 아주 작은, 미스터리한 '사람 손가락' 자국도 발견했냥."
    print(f"📌 발견된 단서: {clue}")
    
    # 추리 질문
    print("\n🤔 미스터리 단서들을 바탕으로, 누가 야식을 먹었을까? (A) 배고픈 나 자신 (B) 근처에 있는 누군가 (C) 장난감?")
    choice = input("주인님, 추리해 봐냥: ").strip().upper()
    
    if choice == "B":
        print("\n✅ 정확하다냥! 이 흔적은 누군가의 온기 있는 손길에서만 날 수 있는 냄새냥!")
        return True
    else:
        print("\n❌ 음... 미스트클로우는 뭔가 찝찝하다냥. 다시 냄새를 맡아봐야겠다냥.")
        return False

def examine_kitchen_counter():
    print("\n[2단계: 주방 조리대 조사] 🔪")
    print("조리대를 돌아다니자, 아주 작고 바스라진 무언가가 눈에 띈다냥...")
    
    # 가상 단서: 설탕이나 밀가루 같은 가루
    clue = "반짝이는 흰 가루들(설탕? 밀가루?)이 여기저기 흩어져 있고, 그 옆에 작은 털 뭉치(????) 같은 것이 있다냥."
    print(f"📌 발견된 단서: {clue}")
    
    # 추리 질문
    print("\n🧐 이 설탕 가루들은 무엇을 만들 때 사용되는 것 같냥? (A) 아침 식사 (B) 야식 (C) 장난감?")
    choice = input("주인님, 네 생각은? ").strip().upper()
    
    if choice == "B":
        print("\n✅ 역시 야식 추적이다냥! 이 가루들은 달콤한 비밀의 증거냥!")
        return True
    else:
        print("\n❌ 음... 이대로는 증거가 부족한 것 같냥. 더 둘러봐야겠다냥.")
        return False

def conclusion(success):
    print("\n========================================================")
    if success:
        print("✨ 미스터리 해결! ✨")
        print("미스트클로우가 모든 단서와 냄새를 조합했냥! 이건 명백히 '지각된 배고픔'과 '밤의 달콤함'이 만들어낸 사건이냥!")
        print("주인님, 우리 둘 다 사랑스러운 범인냥! 하지만 이제 배를 채워야겠다냥. 😻")
    else:
        print("💤 수사 실패... 🤔")
        print("어쩌면 단서가 너무 많아서, 미스트클로우가 아직 범인을 찾지 못했는지도 모른다냥.")
        
    print("\n========================================================")

def run_game():
    intro()
    
    # 1단계: 간식장
    step1_success = check_snack_cabinet()
    time.sleep(1)
    
    # 2단계: 조리대
    step2_success = examine_kitchen_counter()
    time.sleep(1)
    
    # 최종 결과
    final_success = step1_success and step2_success
    conclusion(final_success)

if __name__ == "__main__":
    run_game()
