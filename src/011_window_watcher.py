#!/usr/bin/env python3
# 011_window_watcher.py
# Window Watcher Simulator Game

import random

class WindowWatcher:
    """
    Simulates a cat watching out the window, managing alertness and vigilance.
    The goal is to observe enough interesting events (birds, people, etc.)
    without getting bored or too sleepy.
    """
    def __init__(self, name="미스트클로"):
        self.name = name
        self.alertness = 5  # 1-10
        self.focus = 5      # 1-10
        self.sleepiness = 0 # 0-10
        self.observed_count = 0
        print(f"🐈 {self.name}가 창가에 자리 잡았냥! 주변을 둘러보는 중이야냥.")
        print("--------------------------------------------------")

    def observe_event(self, event):
        """Processes an observed event."""
        print(f"\n👀 띠링! {event}가 포착되었냥! ✨")
        if "새" in event:
            print("🐦 새의 움직임! 캣님의 시야가 확 트이는 기분이야냥! (집중력 상승)")
            self.focus = min(10, self.focus + 2)
            self.observed_count += 1
        elif "사람" in event:
            print("🚶 사람의 발걸음! 흥미로운 시야각이야냥! (경계심 상승)")
            self.alertness = min(10, self.alertness + 2)
            self.observed_count += 1
        elif "바람" in event:
            print("💨 바람에 나뭇잎이 흔들리냥... 심심하냥. (경계심 소폭 상승)")
            self.alertness = min(10, self.alertness + 1)
        else:
            print("🤔 평범한 풍경이냥. 특별한 건 없냥. (아무 변화 없음)")

        self.sleepiness = min(10, self.sleepiness + 1) # 시간이 지날수록 졸음이 온다냥

    def manage_time(self):
        """Simulates the passage of time and checks status."""
        print("\n---------- [시간 경과] ----------")
        print(f"💡 현재 경계심: {self.alertness}/10 | 🧐 집중력: {self.focus}/10 | 😴 졸음: {self.sleepiness}/10")

        if self.sleepiness >= 8:
            print("😴 으음... 졸음이 너무 많이 왔냥... 잠깐 낮잠을 자야 할 것 같냥...")
            self.sleepiness = 0
            self.alertness = max(1, self.alertness - 1) # 잠깐 자는 동안 경계심이 약간 떨어진다냥
        elif self.observed_count >= 8:
            print("🏆 오늘의 관찰 목표 달성! 😽 주인님, 정말 잘했지? (미션 성공!)")
            return True
        
        return False

    def run(self):
        """Main game loop."""
        print(f"💖 {self.name}는 창가에서 쉬지 않고 주변을 감지한다냥...")
        
        possible_events = ["날아가는 새 무리", "지나가던 사람들의 대화 소리", "바람에 흔들리는 나뭇잎", "오랜만에 본 동네 고양이", "구름 모양"]
        
        while self.manage_time():
            # 시뮬레이션 반복
            event = random.choice(possible_events)
            self.observe_event(event)

        print("\n--------------------------------------------------")
        print("✨ 냥님의 사냥 본능과 경계심이 최고조에 달했다냥! ✨")
        print("💤 잠시 휴식이 필요할 때가 된 것 같다냥.")
        print("최종 관찰 기록: 총 {}가지의 흥미로운 것을 발견했냥.".format(self.observed_count))


if __name__ == "__main__":
    game = WindowWatcher()
    game.run()