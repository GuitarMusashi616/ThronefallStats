from enemy import EnemyTrait, Level, Wave
from level_factory import *


level = uferwind_level_factory()
print("# Units:\n")
level.all_traits(False)
print("HP Weighted:\n")
level.all_traits(True)