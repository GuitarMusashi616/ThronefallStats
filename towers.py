import yaml
from typing import List
from copy import deepcopy

def load_data():
    content = open('data/tower_upgrades_fixed.yaml').read()
    data = yaml.safe_load(content)
    return data

def towers():
    data = load_data()
    base_tower = data[0]
    # print(f"base_tower: {base_tower}")
    t_base_tower = Tower(base_tower['name'], base_tower['directDamage'][0]['damageAdded'], base_tower['cooldown'])
    t_base_tower.print()

    for row in data[1:]:
        # print(f"{row['name']}")
        t_tower = deepcopy(t_base_tower)
        t_tower.name = row['name']
        t_tower.dmg *= row['dmgMult']
        t_tower.cooldown *= row['cooldownMult']
        t_tower.print()

class Tower:
    def __init__(self, name, dmg, cooldown):
        self.name = name
        self.dmg = dmg
        self.cooldown = cooldown

    def print(self):
        print(self.name)
        print(f"DPS: {(self.dmg / self.cooldown): .2f}")
        print(f"dmg: {self.dmg: .2f}")
        print(f"cooldown: {self.cooldown: .2f}")
        print()

if __name__ == "__main__":
    towers()
