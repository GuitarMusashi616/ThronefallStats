import yaml

from enemy import Enemy, EnemyTrait, EnemyTraits
from difflib import get_close_matches

def print_all_traits():
    data = load_data()
    all_traits = set()
    for monster in data:
        for trait in monster['traits']:
            all_traits.add(trait)

    for trait in all_traits:
        print(trait)

def load_data():
    content = open('data/enemies.yaml').read()
    data = yaml.safe_load(content)
    return data

def load_enemies():
    data = load_data()
    return {enemy['name']:enemy for enemy in data}

class EnemyFactoryMelon:
    def __init__(self):
        self.enemies = load_enemies()

    def create(self, name: str, quantity: int = 1) -> Enemy:
        # assert name in self.enemies, f"{name} is not a recognized enemy"
        matches = get_close_matches(name, self.enemies.keys(), 1)
        assert matches, f"{name} is not a recognized enemy"

        enemy = self.enemies[matches[0]]
        return Enemy(
            name = enemy['name'],
            traits = EnemyTraits([EnemyTrait[x] for x in enemy['traits']]),
            quantity = quantity,
            hp = enemy['hp'],
        )