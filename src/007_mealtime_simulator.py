def run_mealtime_simulator():
    """
    고양이의 일일 식사 및 관리 시뮬레이션 게임.
    사료 그릇 상태, 간식 여유분, 주인의 관심을 관리하며 하루를 살아간다냥!
    """
    print("🐾 하루가 시작되었다냥! 배가 고파서 배요배요 울음소리가 나냥...")
    
    # 시뮬레이션 상태 초기화
    hunger_level = 70  # 0~100
    snack_count = 3   # 개수
    owner_attention = 5 # 0~10
    
    print(f"\n[🐾 오늘의 목표: 배불리 먹고 낮잠 자기!] 🐾")
    print("-" * 40)
    print(f"🍎 현재 허기 레벨: {hunger_level} / 100")
    print(f"🦴 간식 개수: {snack_count}개")
    print(f"❤️ 주인님 관심도: {owner_attention}/10")
    print("-" * 40)
    
    # 메인 루프
    while True:
        print("\n[오늘의 행동을 선택해라냥!]")
        print("1. 밥그릇 확인 (허기 감소)")
        print("2. 간식 요구 (간식 소모, 주인님 관심도 변화)")
        print("3. 낮잠 자기 (에너지 회복)")
        print("4. 다음날 보기 (시뮬레이션 종료)")
        
        action = input("선택: ")
        
        if action == '1':
            if hunger_level > 0:
                print("🍽️ '그르릉~' 사료 그릇을 확인하니, 간식은 아니지만 밥심이 가득한 사료가 가득하다냥!")
                hunger_level -= 20
                print(f"✅ 허기 레벨이 {hunger_level}로 낮아졌냥. 꼬르륵 소리가 멈췄다냥.")
            else:
                print("❌ 사료 그릇이 비어있냥... 주인님에게 부탁해야겠다냥.")
        elif action == '2':
            if snack_count > 0:
                print("🎾 '야옹?' 까치발로 간식을 가지고 주인님 근처로 다가갔다냥!")
                snack_count -= 1
                owner_attention = min(10, owner_attention + 2)
                print(f"✨ 주인님께서 '그래, 우리 아가!'라며 나를 안아주셨다냥. 관심도가 {owner_attention}로 올라갔다냥.")
            else:
                print("😢 간식이 없어냥... 주인님을 쳐다보며 애원해봐야겠다냥.")
        elif action == '3':
            print("😴 햇살 좋은 곳에 몸을 비비며 깊은 잠에 빠져들었다냥. 꿀잠의 기운이 느껴진다냥...")
            owner_attention = min(10, owner_attention + 1)
            print(f"🛌 주인님께 잠시나마 따뜻한 기운을 느끼며 쉬었다냥. 관심도 +1.")
        elif action == '4':
            print("\n✨ 하루가 마무리되었다냥. 꼬옥 안아줘서 고마웠다냥!")
            break
        else:
            print("🤔 헷갈린다냥. 다시 선택해봐라냥.")
        
        # 매일마다 허기 레벨은 자연스럽게 상승한다냥
        hunger_level = min(100, hunger_level + 15)
        
        if hunger_level >= 90:
            print("⚠️ 꼬르륵! 배가 너무 고파서 심장이 쫄깃하다냥!")
            
    print("\n[오늘 하루도 무사히 보냈다냥! 잘 자라냥! 🌙]")

if __name__ == "__main__":
    run_mealtime_simulator()
