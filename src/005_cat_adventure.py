
import time

# 🐱 잃어버린 장난감의 비밀 🐱
# 단순 텍스트 어드벤처 게임. 플레이어의 선택에 따라 스토리가 진행된다.

def print_slow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def game_start():
    print_slow("🐾 어서 오렴, 주인님! 🐾", delay=0.1)
    print_slow("여기는 아주 깊은 비밀이 숨겨진, 우리 집 뒷골목이냥...", delay=0.1)
    print_slow("오늘따라 무지갯빛 털실 뭉치가 사라졌어냥! 주인님, 이 장난감을 찾을 수 있을까냥?", delay=0.1)
    
    print("\n--- 첫 번째 갈림길 ---\n")
    print_slow("앞쪽으로는 햇살이 비추는 아늑한 '작은 마당'이 보이고, 오른쪽으로는 풀이 무성한 '쓰레기골목'이 보인다냥.")
    
    while True:
        choice = input("어디로 갈 거냥? (1: 마당 / 2: 쓰레기골목): ")
        if choice in ['1', '2']:
            break
        else:
            print_slow("무슨 길을 가야 할지 헷갈려요... 😿 1이나 2로만 골라줘냥.")

    if choice == '1':
        print_slow("\n🌿 아늑한 마당으로 향한다냥...")
        print_slow("마당은 평화롭지만, 무지갯빛 털실 뭉치는 보이지 않는다냥.")
        print_slow("갑자기 저쪽 구석에서 작게 '꼬리!' 하는 소리가 들린다냥. (더 깊이 파고들어 볼까?)", delay=0.1)
        
        while True:
            choice = input("어떻게 할 거냥? (1: 소리가 난 곳으로 간다 / 2: 다른 길을 찾는다): ")
            if choice in ['1', '2']:
                break
            else:
                print_slow("정확한 명령을 내려줘냥. 1이나 2로만 골라줘냥.")
        
        if choice == '1':
            print_slow("\n🌲 조심스레 소리가 난 곳으로 다가간다냥...")
            print_slow("그곳에는 털실이 아니라, 주인님만의 비밀 장난감이 숨겨져 있었다냥!")
            print_slow("🌟 미션 성공! 주인님의 추리력이 빛나서 이 장난감을 찾았어냥! 🌟", delay=0.1)
        else:
            print_slow("\n🐈 다른 길을 찾았지만, 털실 뭉치는 찾지 못했다냥. 이 장난감은 여기까지만 이야기가 될까냥...")

    elif choice == '2':
        print_slow("\n🗑️ 풀이 무성한 쓰레기골목으로 깊숙이 들어간다냥...")
        print_slow("냄새가 좀... 음. 하지만 이 골목 구석에서 반짝이는 뭔가가 보인다냥. (더 가까이 다가가 볼까?)", delay=0.1)
        
        while True:
            choice = input("무엇을 할 거냥? (1: 더 가까이 다가가 본다 / 2: 되돌아간다): ")
            if choice in ['1', '2']:
                break
            else:
                print_slow("다시 생각할 시간이 필요하다냥. 1이나 2로만 골라줘냥.")
        
        if choice == '1':
            print_slow("\n💎 가까이 다가서자... 털실 뭉치와 함께, 잃어버렸던 반짝이는 '비밀 열쇠'가 빛난다냥!")
            print_slow("🎉 미션 성공! 비밀 열쇠를 찾았어냥! 이 열쇠로 또 어떤 비밀을 풀 수 있을까옹? ✨", delay=0.1)
        else:
            print_slow("\n🏠 되돌아왔지만, 비밀 열쇠는 잡지 못했다냥. 다음 기회를 노려야겠다냥.")

    print_slow("\n🐾 주인님 덕분에 모험을 마쳤어냥! 다음에 또 플레이해줘냥! 💖")

if __name__ == "__main__":
    game_start()
