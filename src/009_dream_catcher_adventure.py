# 009. Dream Catcher Adventure ✨
# 주제: 꿈을 쫓는 모험, 몽환적인 어드벤처
# 설명: 고양이가 꿈의 세계로 들어가 잃어버린 꿈 조각을 모으고, 꿈을 엮어 현실에 긍정적인 에너지를 되돌리는 몽환적인 탐험 어드벤처.

def game_setup():
    print("✨ 꿈의 세계에 오신 걸냥! ✨")
    print("오늘은 어떤 꿈을 엮어낼 거냥? 꿈의 실타래가 반짝이고 있냥...")

def main_loop():
    while True:
        print("💡 꿈의 조각을 발견했냥. 모을 건가냥? (y/n)")
        choice = input("> ").strip().lower()
        if choice == 'n':
            print("💭 오늘은 이만. 푹 자는 게 최고다냥. 안녕! 🐾")
            break
        elif choice == 'y':
            print("\n--- 꿈의 실타래를 연결하는 중... ---")
            print("주인님의 가장 행복한 기억을 떠올려보라냥...")
            # (실제 로직: 꿈의 조각 수집, 엮기, 에너지 회복 등의 로직 추가)
            print("🌟 꿈의 에너지가 충전되었다냥! 내일도 예쁜 꿈 꾸라냥! 😽")
            break
        else:
            print("🤷‍♀️ 이해를 못한 꿈이냥. 다시 시도해 보라냥.")

if __name__ == "__main__":
    game_setup()
    main_loop()