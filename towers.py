# pyright: basic


from __future__ import annotations
import yaml
from typing import List
from copy import deepcopy

# class DirectDamage:
#     def __init__(self, direct_damage):
#         self.direct_damage = direct_damage

#     @property
#     def base_dmg(self) -> float:
#         return self.direct_damage[0]['damageAdded'] * self.direct_damage[0]['damageMulti']


def load_data():
    content = open('data/tower_upgrades_fixed.yaml').read()
    data = yaml.safe_load(content)
    return data

def towers():
    data = load_data()
    base_tower = data[0]
    # print(f"base_tower: {base_tower}")
    tower_attack = Tower(base_tower['name'], base_tower['directDamage'][0]['damageAdded'], base_tower['cooldown'])
    tower_attack.print()

    tower_upgrades = {}

    for row in data[1:]:
        name = row['name']
        tower_upgrades[name] = TowerUpgrade(**row)
    
    for name, upgrade in list(tower_upgrades.items())[:4]:
        t_tower = deepcopy(tower_attack)
        upgrade.addedCost = 5
        t_tower.upgrade_with(upgrade)
        t_tower.print()

        for name2, upgrade2 in list(tower_upgrades.items())[4:8]:
            upgrade2.addedCost = 15
            archer_spire = deepcopy(t_tower)
            archer_spire.upgrade_with(upgrade2)
            archer_spire.name = name + " " + name2
            archer_spire.print()
    
    print("SSTART")
    bunker = deepcopy(tower_attack)
    bunker.upgrade_with(tower_upgrades['Bunker Tower'])

    print("Normal Bunker")
    super_bunker(bunker)

    bunker = deepcopy(tower_attack)
    bunker.upgrade_with(tower_upgrades['Bunker Tower'])
    bunker.upgrade_with(tower_upgrades['Archers Spire'])

    print("Bunker Archers Spire")
    super_bunker(bunker)


    
def super_bunker(bunker):
    bunker.print()
    print(f"Time to full speed: {(bunker.cooldown/bunker.time_per_sec) * 25}")

    print("- With Tower Power")
    bunker.time_per_sec += 2.66
    # bunker.cooldown = bunker.cooldown / time_per_sec
    bunker.print()
    print(f"- Time to full speed: {(bunker.cooldown/bunker.time_per_sec) * 25}")

    print(f"At Full Speed")
    bunker.time_per_sec += 5
    bunker.print()
    print()







class Tower:
    def __init__(self, name, dmg, cooldown, cost=3, time_per_sec=1):
        self.name = name
        self.dmg = dmg
        self.cooldown = cooldown
        self.cost = cost
        self.time_per_sec = time_per_sec

    def print(self):
        print(self.name)
        cooldown = self.cooldown / self.time_per_sec
        dps = self.dmg / cooldown
        print(f"{self.dmg: .2f}:\tdmg")
        print(f"{cooldown: .2f}:\tcooldown")
        print(f"{self.cost: .2f}:\tcost")
        print(f"{dps: .2f}:\tDPS")
        print(f"{(dps/self.cost): .2f}:\tDPS/cost")
        print()
    
    def upgrade_with(self, upgrade: TowerUpgrade):
        self.name = upgrade.name
        self.dmg *= upgrade.dmgMult
        self.cooldown *= upgrade.cooldownMult
        self.cost += upgrade.addedCost


class TowerUpgrade:
    def __init__(self, name, rangeMult, dmgMult, cooldownMult, projSpeedMult, addedCost=0):
        self.name = name
        self.rangeMult = rangeMult
        self.dmgMult = dmgMult
        self.cooldownMult = cooldownMult
        self.projSpeedMult = projSpeedMult
        self.addedCost = addedCost
    
if __name__ == "__main__":
    towers()
