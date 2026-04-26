import random

def hunt_simulation():
    """
    새벽 사냥꾼 시뮬레이터: 에너지 관리를 통한 사냥 성공 확률 게임.
    플레이어는 에너지를 소비하며 무작위 사냥 시도를 합니다.
    """
    print("✨ 🐾 새벽 사냥꾼 시뮬레이터 🐾 ✨")
    print("주인님이 깊이 잠든 새벽, 사냥 본능이 발동했냥!")

    energy = 100
    max_attempts = 10
    attempts = 0

    while energy > 0 and attempts < max_attempts:
        attempts += 1
        print(f"\n--- 시도 {attempts}/{max_attempts} ---")
        print(f"현재 에너지: {energy}%")

        if energy < 10:
            print("😴 에너지가 너무 낮다냥... 잠시 쉬어야겠냥.")
            break

        # 사냥 성공 확률 (난이도 및 에너지에 따라 변동)
        success_chance = 30 + (energy / 2)
        print(f"사냥 본능 점수 측정... 성공 확률: 약 {success_chance:.1f}%")
        
        # 사냥 시도 (랜덤 판정)
        roll = random.randint(1, 100)
        
        if roll <= success_chance:
            print("🌟 성공이다냥! 주운 장난감을 발견했냥!")
            energy -= 15 # 성공하면 약간 에너지가 소모됨 (흥분)
            print("🍖 보상: 약간의 기력 회복 (10 에너지)")
            energy = min(100, energy + 10)
        else:
            print("💨 헛발질... 냄새만 맡고 지나갔냥.")
            energy -= 20 # 실패하면 에너지 소모가 큼
            
        # 에너지 소모 및 회복 (시간 경과에 따른 기본 소모)
        energy -= 5
        
    print("\n=========================================")
    if energy <= 0:
        print("💔 에너지를 모두 소진했냥. 오늘은 사냥할 수 없겠냥...")
    elif attempts >= max_attempts:
        print("🐾 최대 시도 횟수를 채웠냥. 오늘은 여기까지냥...")
    else:
        print("😴 충분히 쉬어서 에너지가 회복되었냥. 다음 기회를 노려볼까냥.")
    print("=========================================")

if __name__ == "__main__":
    hunt_simulation()