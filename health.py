# pyright: strict

from __future__ import annotations
from typing import Dict, Iterator, List
import yaml

from enemy import EnemyTrait

class Fighter:
    def __init__(self, name: str, hp: float, dmg: float, cooldown: float, dmg_traits: DamageTraits, traits: Traits):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.cooldown = cooldown
        self.dmg_traits = dmg_traits
        self.traits = traits
    
    @property
    def dps(self) -> float:
        return self.dmg / self.cooldown
    
    def __repr__(self) -> str:
        return (
            f"{self.name}\n"
            f"HP:\t{self.hp}\n"
            f"DMG:\t{self.dmg}\n"
            f"CD:\t{self.cooldown}\n"
            f"DPS:\t{self.dps}\n"
            f"HAS:\t{self.traits}\n"
            f"VS:\t{self.dmg_traits}\n"
        )
    
    def print(self):
        print(self)

    def dmg_vs(self, traits: Traits):
        assert self.dmg_traits is not None, "This fighter does not support against method"
        # if the damage traits req traits then add that multiplier
        dmg = 0
        for dmg_trait in self.dmg_traits:
            if traits.includes(dmg_trait.req_traits):
                dmg += dmg_trait.damage_added
                dmg *= dmg_trait.damage_mult
        return dmg
    
    def print_vs(self, traits: Traits):
        dmg = self.dmg_vs(traits)
        dps = dmg / self.cooldown

        print(self.name)
        print(f"HP:\t{self.hp}")
        print(f"DMG:\t{dmg}")
        print(f"CD:\t{self.cooldown}")
        print(f"DPS:\t{dps}")
        print(f"HAS:\t{self.traits}")
        print(f"VS:\t{self.dmg_traits}")
        print()





class Traits:
    def __init__(self, traits: List[EnemyTrait]):
        self.traits = traits
    
    def __repr__(self) -> str:
        return repr(self.traits)
    
    def __iter__(self) -> Iterator[EnemyTrait]:
        return iter(self.traits)
    
    @classmethod
    def from_list(cls, ls: List[str]):
        return cls([EnemyTrait[x] for x in ls])
    
    def has(self, trait: EnemyTrait):
        return trait in self.traits
    
    def includes(self, traits: Traits):
        return all(trait in self.traits for trait in traits)

class DamageTrait:
    def __init__(self, damage_added: float, damage_mult: float, req_traits: Traits):
        self.damage_added = damage_added
        self.damage_mult = damage_mult
        self.req_traits = req_traits
    
    def __repr__(self) -> str:
        return f"+{self.damage_added} x{self.damage_mult} {self.req_traits}"
    
    @classmethod
    def from_dic(cls, dic: Dict[str, float | List[str]]):
        return cls(
            damage_added=dic['damageAdded'], # type: ignore
            damage_mult=dic['damageMult'], # type: ignore
            req_traits = Traits.from_list(dic['requiredTags']) # type: ignore
        )

class DamageTraits:
    def __init__(self, damage_traits: List[DamageTrait]):
        self.damage_traits = damage_traits
    
    @classmethod
    def from_list(cls, ls: List[Dict[str, float | List[str]]]):
        return cls([DamageTrait.from_dic(dic) for dic in ls])
    
    def __iter__(self) -> Iterator[DamageTrait]:
        return iter(self.damage_traits)
    
    def __repr__(self):
        return repr(self.damage_traits)

def load_data():
    content = open('data/dps_small.yaml').read()
    data = yaml.safe_load(content)
    return data

def all_dps() -> List[Fighter]:
    result: List[Fighter] = []
    for row in load_data():
        if 'directDamage' not in row:
            continue
        name = row['name'] 
        hp = row['hp'] 
        traits = Traits.from_list(row['traits'])
        dmg_traits = DamageTraits.from_list(row['directDamage'])
        dmg = row['directDamage'][0]['damageAdded']
        cooldown = row['cooldown']

        fighter = Fighter(name, hp, dmg, cooldown, dmg_traits, traits)
        result.append(fighter)
    return result

def hp_sorted():
    all_units = all_dps()
    all_units.sort(key = lambda x: x.hp, reverse=True)
    for unit in all_units:
        unit.print()

def hp_against_towers_sorted():
    all_units = all_dps()
    all_units = list(filter(lambda unit: unit.name.startswith("E "), all_units))
    for unit in all_units:
        unit.tower_hp = unit.hp # type: ignore
        if unit.traits.has(EnemyTrait.ArmoredAgainstRanged):
            unit.tower_hp /= 0.6 # type: ignore

        if unit.traits.has(EnemyTrait.TakesIncreasedDamageFromTowers):
            unit.tower_hp /= 2 # type: ignore

        if unit.traits.has(EnemyTrait.Flying):
            unit.tower_hp /= 1.15 # type: ignore

    all_units.sort(key = lambda x: x.tower_hp, reverse=True) # type: ignore
    for unit in all_units:
        print(unit.name)
        print(f"THP:\t{unit.tower_hp}") # type: ignore
        print(f"HP:\t{unit.hp}")
        print(f"DMG:\t{unit.dmg}")
        print(f"CD:\t{unit.cooldown}")
        print(f"DPS:\t{unit.dps}")
        print(f"HAS:\t{unit.traits}")
        print(f"VS:\t{unit.dmg_traits}")
        print()

def dps_against_ogres_sorted():
    all_units = all_dps()
    all_units.sort(key = lambda x: x.dps, reverse=True)
    ogres = filter(lambda x: 'ogre' in x.name.lower(), all_units)
    ogre = next(ogres)
    print(ogre)
    assert ogre.traits

    for unit in filter(lambda x: x.name.startswith('P '), all_units):
        unit.print_vs(ogre.traits)
        # unit.print()



if __name__ == "__main__":
    dps_against_ogres_sorted()
    
