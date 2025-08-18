import yaml
from typing import List

def load_data():
    content = open('data/dps_fixed.yaml').read()
    data = yaml.safe_load(content)
    return data

def load_unique():
    data = load_data()
    names = set()
    result = []
    for row in data:
        name = row['name'] 
        if name not in names:
            names.add(name)
            result.append(row)
    return result

def simple_dps_hp_of_each():
    for row in load_unique():
        try:
            name = row['name'] 
            hp = row['hp'] 

            print(name)
            print(f"hp: {hp}")
            # print(f"dmg: {row['directDamage'][0]['damageAdded']}")
            # print(f"cooldown: {row['cooldown']}")
            if 'directDamage' in row:
                dmg = row['directDamage'][0]['damageAdded']
                cooldown = row['cooldown']
                print(f"dps: {dmg/cooldown}")
            print()
        except (KeyError, TypeError):
            pass

def simple_dps_hp_cost_of_each():
    for row in load_unique():
        try:
            name = row['name'] 
            hp = row['hp'] 

            if "P " not in name:
                continue

            print(name)
            print(f"hp: {hp}")
            # print(f"dmg: {row['directDamage'][0]['damageAdded']}")
            # print(f"cooldown: {row['cooldown']}")
            if 'directDamage' in row:
                quantity = 4
                cost = 4
                cooldown = row['cooldown']
                heroes = {"P Support Mage", "P Lizzard Rider", "P Golem", "P Firewing"}
                
                if name in heroes:
                    cost = 6
                    quantity = 1

                dmg = row['directDamage'][0]['damageAdded'] * quantity

                print(f"dps: {dmg/cooldown}")
                print(f"dps/cost: {(dmg/cooldown)/cost}")

            print()
        except (KeyError, TypeError):
            pass

if __name__ == "__main__":
    simple_dps_hp_cost_of_each()
