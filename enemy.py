# pyright: strict

from __future__ import annotations
from collections import defaultdict
from enum import Enum, auto
from functools import reduce
from typing import Iterator, List, Set, Tuple

class EnemyTrait(Enum):
    HUMAN = auto()
    MONSTER = auto()
    SIEGE = auto()
    MELEE = auto()
    RANGED = auto()
    FLYING = auto()
    FAST = auto()

    VULNERABLE_TO_SPLASH = auto()
    VULNERABLE_TO_BUILDINGS = auto()

    ARMORED_AGAINST_RANGED = auto()
    ARMORED_AGAINST_PLAYER = auto()

    # WIKI types
    TOWER_VULNERABLE = auto()
    RANGED_RESISTANT = auto()
    RANGED_VULNERABLE = auto()
    HIGH_HEALTH = auto()
    HERO_RESISTANT = auto()

    # Moonloader types
    ArmoredAgainstRanged = auto()
    NaturallyVulnerableToSplash = auto()
    FastMoving = auto()
    MeeleFighter = auto()
    NaturallyHighHealthTarget = auto()
    Monster = auto()
    Exploding = auto()
    FireAndExplosionResistant = auto()
    EnemyOwned = auto()
    Player = auto()
    TakesReducedDamageFromPlayerAttacks = auto()
    Humanoid = auto()
    TakesIncreasedDamageFromTowers = auto()
    AUTO_Alive = auto()
    SiegeWeapon = auto()
    LargeUnit = auto()
    RangedFighter = auto()
    PlayerOwned = auto()
    Flying = auto()
    Boss = auto()
    VulnerableVsRanged = auto()

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


class EnemyTraits:
    def __init__(self, traits: List[EnemyTrait]):
        self.traits = traits
    
    def has(self, trait: EnemyTrait) -> bool:
        return trait in self.traits
    
    def as_tuple(self):
        return tuple(self.traits)
    
    def __iter__(self) -> Iterator[EnemyTrait]:
        return iter(self.traits)

    def __repr__(self) -> str:
        return repr(self.traits)
    
class Enemy:
    def __init__(self, name: str, traits: EnemyTraits, quantity: int, hp: float):
        self.name = name
        self.traits = traits
        self.quantity = quantity
        self.hp = hp

    def __repr__(self) -> str:
        return f"{self.quantity}x {self.name}"

class Wave:
    def __init__(self, enemies: List[Enemy]):
        self.enemies = enemies

    def __add__(self, other: Wave) -> Wave:
        """
        Combine two waves by merging their enemies.
        If the same enemy type appears in both waves, their quantities are added.
        """
        # Create a dictionary to track enemy quantities by name
        enemy_dict: dict[str, Enemy] = {}
        
        # Add enemies from the first wave
        for enemy in self.enemies:
            if enemy.name in enemy_dict:
                # If enemy already exists, add quantities
                existing = enemy_dict[enemy.name]
                enemy_dict[enemy.name] = Enemy(
                    enemy.name, 
                    enemy.traits, 
                    existing.quantity + enemy.quantity,
                    enemy.hp
                )
            else:
                # Create a new enemy entry
                enemy_dict[enemy.name] = Enemy(
                    enemy.name, 
                    enemy.traits, 
                    enemy.quantity,
                    enemy.hp
                )
        
        # Add enemies from the second wave
        for enemy in other.enemies:
            if enemy.name in enemy_dict:
                # If enemy already exists, add quantities
                existing = enemy_dict[enemy.name]
                enemy_dict[enemy.name] = Enemy(
                    enemy.name, 
                    enemy.traits, 
                    existing.quantity + enemy.quantity,
                    enemy.hp
                )
            else:
                # Create a new enemy entry
                enemy_dict[enemy.name] = Enemy(
                    enemy.name, 
                    enemy.traits, 
                    enemy.quantity,
                    enemy.hp
                )
        
        # Convert back to list and create new Wave
        combined_enemies = list(enemy_dict.values())
        return Wave(combined_enemies)
    
    @property
    def traits(self) -> Set[EnemyTrait]:
        traits: Set[EnemyTrait] = set()
        for enemy in self.enemies:
            for trait in enemy.traits:
                traits.add(trait)
        return traits
    
    # what percent of enemies have this trait?
    def trait_percent(self, trait: EnemyTrait):
        total = 0
        total_with_trait = 0
        for enemy in self.enemies:
            total += enemy.quantity
            if enemy.traits.has(trait):
                total_with_trait += enemy.quantity

        return total_with_trait / total

    def trait_percent_hp_weighted(self, trait: EnemyTrait):
        total = 0
        total_with_trait = 0
        for enemy in self.enemies:
            total += enemy.quantity * enemy.hp
            if enemy.traits.has(trait):
                total_with_trait += enemy.quantity * enemy.hp

        return total_with_trait / total
    
    def all_traits(self, is_hp_weighted: bool=False):
        print(self)
        weighted_traits: List[Tuple[float, EnemyTrait]] = []
        for trait in self.traits:
            perc = self.trait_percent(trait) if not is_hp_weighted else self.trait_percent_hp_weighted(trait)
            weighted_traits.append((perc, trait))

        weighted_traits.sort(key=lambda x: x[0], reverse=True)

        for perc, trait in weighted_traits:
            print(f"{perc:.2%}\t{trait}")
        print()

    def all_trait_groups(self, is_hp_weighted: bool=False):
        print(self)
        counter = defaultdict(int) # type: ignore
        for enemy in self.enemies:
            tup = enemy.traits.as_tuple()
            counter[tup] += 1 if not is_hp_weighted else enemy.hp # type: ignore

        total = sum(counter.values()) # type: ignore

        counter_sorted = list(counter.items()) # type: ignore
        counter_sorted.sort(key = lambda x: x[1], reverse=True) # type: ignore

        for trait_group, count in counter_sorted: # type: ignore
            perc = count / total
            print(f"{perc:.2%}\t{trait_group}")
        print()
    
    def __repr__(self) -> str:
        return repr(self.enemies)

class Level:
    def __init__(self, waves: List[Wave]):
        self.waves = waves
    
    def check_trait(self, traits: List[EnemyTrait]):
        for i, wave in enumerate(self.waves):
            add_string = ""
            for trait in traits:
                perc = wave.trait_percent(trait)
                add_string += f"\t{trait}%: {perc:.2%}"
            print(f"Wave {i+1}: {wave}{add_string}")

    def all_traits_by_wave(self, is_hp_weighted: bool = False):
        for i, wave in enumerate(self.waves):
            print(f"Wave {i+1}")
            wave.all_traits(is_hp_weighted)

    def all_traits(self, is_hp_weighted: bool = False):
        print("Whole Level")
        wave = self.combined()
        wave.all_traits(is_hp_weighted)
        print()

    def all_trait_groups(self, is_hp_weighted: bool=False):
        print("Whole Level Groups")
        wave = self.combined()
        wave.all_trait_groups(is_hp_weighted)
        print()

    def combined(self) -> Wave:
        if not self.waves:
            return Wave([])
        return reduce(lambda w1, w2: w1 + w2, self.waves)
    

    def __repr__(self) -> str:
        return repr(self.waves)
