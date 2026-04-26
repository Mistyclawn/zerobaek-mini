#!/usr/bin/env python3

import random

class Character:
    """Base class for characters in the battle."""
    def __init__(self, name, max_hp, attack, defense):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.current_hp > 0

    def take_damage(self, damage):
        # Damage calculation: max(1, damage - defender_defense)
        actual_damage = max(1, damage - self.defense)
        self.current_hp -= actual_damage
        print(f"💥 {self.name}이(가) {actual_damage}의 피해를 입었다냥! (남은 HP: {max(0, self.current_hp)})")
        return actual_damage

def battle_turn(attacker, defender):
    """Simulates one turn of combat."""
    print("-" * 30)
    print(f"🛡️ {attacker.name} 차례다냥!")
    
    # 1. Attack
    base_damage = random.randint(attacker.attack - 5, attacker.attack + 5)
    actual_damage = defender.take_damage(base_damage)
    
    print(f"⚔️ {attacker.name}이(가) {defender.name}에게 {actual_damage}의 피해를 주었다냥!")
    
    # Check for KO
    if not defender.is_alive():
        return "win" # Battle ended by damage
    
    # 2. Defender retaliates (simple AI for this example)
    print(f"😈 {defender.name}도 반격한다냥!")
    base_damage_defense = random.randint(defender.attack - 5, defender.attack + 5)
    damage_taken = attacker.take_damage(base_damage_defense)
    print(f"⚔️ {defender.name}이(가) {attacker.name}에게 {damage_taken}의 피해를 주었다냥!")
    
    if not attacker.is_alive():
        return "loss" # Battle ended by damage

    return "continue"

def battle_game():
    """Main loop for the battle game."""
    print("\n🌸🐱✨ 몬스터 배틀 게임 시작한다냥! 💖")
    print("🐾 주인님과 가상의 몬스터가 싸우는 턴제 액션 게임이냥!")
    print("목표는 상대방의 HP를 0으로 만드는 거다냥!")

    # Setup characters
    player = Character("주인님의 용감한 캣메이트", 100, 25, 10) # Name, MaxHP, Attack, Defense
    enemy = Character("덩치 큰 마법 괴물", 120, 22, 8)
    
    print("\n==========================================")
    print("🐱 주인님의 캣메이트가 전장에 등장했다냥! 💪")
    print(f"🐱 {player.name}: HP {player.max_hp} / ATK {player.attack} / DEF {player.defense}")
    print("👹 적: 덩치 큰 마법 괴물")
    print(f"👹 {enemy.name}: HP {enemy.max_hp} / ATK {enemy.attack} / DEF {enemy.defense}")
    print("==========================================")

    turn = 1
    while player.is_alive() and enemy.is_alive():
        print("\n\n✨✨✨ ⚔️ 전투 턴: ", turn, " ✨✨✨")
        
        # Player Turn (simplified to always attack)
        print("⭐ 주인님의 차례다냥! 공격해라냥! 😼")
        base_damage = random.randint(player.attack - 5, player.attack + 5)
        enemy.take_damage(base_damage)
        
        if not enemy.is_alive():
            break
            
        # Enemy Turn (automatic counter-attack)
        print("\n👾 상대방의 반격이다냥!")
        base_damage_enemy = random.randint(enemy.attack - 5, enemy.attack + 5)
        player.take_damage(base_damage_enemy)
        
        turn += 1

    # Game conclusion
    print("\n" + "=" * 30)
    if player.is_alive() and not enemy.is_alive():
        print("🎉🎉🎉 승리했다냥! ✨🎉🎉")
        print(f"{player.name}이(가) 몬스터를 물리쳤다냥! 주인님이 최고다냥! 🏆")
    elif enemy.is_alive() and not player.is_alive():
        print("😭❌ 패배했다냥... 😭❌")
        print(f"{player.name}이(가) 쓰러졌어냥. 주인님의 다음 전투를 응원한다냥! 😿")
    else:
        print("😵 무승부로 끝났다냥...")
    print("=" * 30)

if __name__ == "__main__":
    battle_game()