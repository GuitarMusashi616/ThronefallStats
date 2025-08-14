from enemy import EnemyTrait, Level, Wave
from enemy_factory_melon import EnemyFactoryMelon
from level_factory import *
from level_parser import LevelParser


def main():
    level = uferwind_level_factory()
    print("# Units:\n")
    level.all_traits(False)
    print("HP Weighted:\n")
    level.all_traits(True)


def main2():
    content = totend_level_input()
    parser = LevelParser(content, EnemyFactoryMelon())
    level = parser.parse()
    level.all_traits_by_wave()

    print("# Units:\n")
    level.all_traits(False)
    print("HP Weighted:\n")
    level.all_traits(True)



if __name__ == "__main__":
    main2()
