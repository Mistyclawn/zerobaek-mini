# 051 - Gnome Gardener
# 이 파일은 051 게임의 핵심 로직을 담는다냥.
# 플레이어는 요정들이 사는 마법의 정원을 관리하며 희귀 식물과 마법의 순환을 조율한다냥.

class GnomeGame:
    def __init__(self):
        self.garden_state = {}
        self.magic_level = 1

    def harvest(self, plant):
        # 식물 수확 로직
        return f"'{plant}'에서 빛나는 마나를 모았다냥!"

    def deal_with_sprite(self, sprite):
        # 요정 처리 로직
        return f"장난꾸러기 '{sprite}'를 달래서 평화가 찾아왔다냥."

# 더 많은 로직과 GUI 부분이 추가될 예정이라냥.
