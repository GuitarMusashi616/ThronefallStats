from typing import List
from enemy import Level, Wave
from enemy_factory_melon import EnemyFactoryMelon


class LevelParser:
    @classmethod
    def from_filename(cls, filename: str):
        with open(filename) as file:
            content = file.read()
            return LevelParser(content, EnemyFactoryMelon())
        
    def __init__(self, content: str, factory: EnemyFactoryMelon):
        self.line_words = self.break_into_words(content)
        self.factory = factory
    
    def break_into_words(self, content: str) -> List[List[str]]:
        lines = content.strip().splitlines()
        return [[word.strip().split() for word in line.split(',')] for line in lines]
    
    def parse(self) -> Level:
        waves = []
        for wave in self.line_words:
            enemies = []
            for monster_type in wave:
                assert monster_type[0].isnumeric(), "Must start with a number"
                quantity = int(monster_type[0])
                name = " ".join(monster_type[1:])
                enemy = self.factory.create(name, quantity)
                enemies.append(enemy)
            waves.append(Wave(enemies))
        return Level(waves)
            
                


