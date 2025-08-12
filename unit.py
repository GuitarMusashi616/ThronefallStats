# pyright: strict

from enum import Enum, auto


class UnitType(Enum):
    MELEE = auto()


class Unit:
    def __init__(self, name: str, quantity: int, attacks_per_second: float, attack_range: float, base_dmg: float, hp: float, movement_speed: float, dmg_vs_siege: float=1, dmg_vs_ranged_resistant: float=1, dmg_vs_tower_vulnerable: float=1, dmg_vs_flying: float=1, dmg_vs_monsters: float=1, dmg_vs_air_not_monster: float=1, dmg_vs_ranged: float=1, dmg_vs_fast: float=1, attack_range_vs_flying: float=1, attack_range_vs_monsters: float=1, cost: int = -1):
        self.name = name
        self.quantity = quantity
        self.attacks_per_second = attacks_per_second
        self.attack_range = attack_range
        self.attack_range_vs_flying = attack_range_vs_flying
        self.attack_range_vs_monsters = attack_range_vs_monsters
        self.base_dmg = base_dmg
        self.hp = hp
        self.movement_speed = movement_speed
        self.dmg_vs_flying = dmg_vs_flying
        self.dmg_vs_siege = dmg_vs_siege
        self.dmg_vs_monsters = dmg_vs_monsters
        self.dmg_vs_ranged_resistant = dmg_vs_ranged_resistant
        self.dmg_vs_air_not_monster = dmg_vs_air_not_monster
        self.dmg_vs_tower_vulnerable = dmg_vs_tower_vulnerable
        self.dmg_vs_ranged = dmg_vs_ranged
        self.dmg_vs_fast = dmg_vs_fast
        self.cost = cost
    
    @property
    def dps(self) -> float:
        return self.attacks_per_second * self.base_dmg * self.quantity
    
    @property
    def dps_flying(self) -> float:
        return self.attacks_per_second * self.base_dmg * self.dmg_vs_flying * self.quantity
    
    def print(self):
        print(self.name)
        print(f"HP: {self.hp: .2f}")
        print(f"DPS: {self.dps: .2f}")
        # print(f"DPS flying: {self.dps_flying: .2f}")
        print(f"Range: {self.attack_range: .2f}")
        if self.cost > 0:
            print(f"DPS/cost: {self.dps / self.cost: .2f}")
        print()

