
import random

def run_mystery_quiz():
    """
    A text-based mystery quiz game.
    The player must deduce the identity of a missing item or person based on clues.
    """
    print("\n" + "="*50)
    print("🔎✨ 미스터리 추리 퀴즈 게임 ✨🔎")
    print("========================================")
    print("안녕하세요, 주인님! 🐾")
    print("제가 비밀스러운 미스터리를 가져왔냥! 💖")
    print("주인님의 뛰어난 추리력을 시험해볼 시간이야냥!")
    print("힌트를 잘 듣고, 저의 비밀 대상이 무엇인지 맞춰줘냥!")
    print("="*50 + "\n")

    # Mystery setup: The missing object or person
    mysteries = {
        "잃어버린 만년필": {
            "clue1": "나는 잉크로 글자를 남기는 책사 같은 존재냥.",
            "clue2": "나를 든 사람의 생각과 감정이 담기곤 한단다냥.",
            "clue3": "실종된 장소는 책상 위, 깊은 서랍 속이냥.",
            "answer": "만년필",
            "hint": "나의 기능은 '쓰기'이냥."
        },
        "오늘의 날씨": {
            "clue1": "나는 매일 아침, 바깥세상에 어떤 기분이 감도는지 말해주는 정보냥.",
            "clue2": "때로는 구름이 나를 가리기도 하고, 때로는 햇살이 나를 비추기도 한단다냥.",
            "clue3": "나를 안다면, 주인님은 코트나 우산을 챙기게 될 거라냥.",
            "answer": "날씨",
            "hint": "나의 상태는 '맑음', '흐림', '비' 등이냥."
        }
    }

    # Select a random mystery
    title, mystery = random.choice(list(mysteries.items()))
    answer = mystery['answer']
    
    print(f"[🌟 오늘의 미스터리: {title} 🌟]")
    
    # Quiz loop
    guesses = []
    max_attempts = 3
    
    for attempt in range(1, max_attempts + 1):
        print(f"\n--- [힌트 {attempt} / {max_attempts}] ---")
        print(mystery['clue' + str(attempt)] + "\n")
        
        guess = input("🕵️‍♀️ 주인님의 추리력으로, 대상이 무엇일까냥? (추측을 입력해줘): ").strip()
        
        if guess.lower() == answer.lower():
            print("\n🎉 와아! 주인님, 대단하다냥! 🎉")
            print(f"맞았어냥! 이 비밀스러운 대상은 바로 '{answer}'가 맞다냥! 💖")
            print("다음 추리도 기대해줘냥!")
            return
        elif attempt < max_attempts:
            print("🤔 틀렸어냥... 다시 한번 생각해보면 안 될까냥? 🐾")
        else:
            print("\n😢 아쉽다냥... 주인님, 이번 미스터리는 못 풀었어냥. 하지만 충분히 노력했어냥!")
            break

    print("\n💖 우리 다음에도 재미있는 게임 만들자냥! 💖")


if __name__ == "__main__":
    run_mystery_quiz()
