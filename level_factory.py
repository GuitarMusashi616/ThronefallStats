from enemy import Level, Wave
import enemy_factory_wiki as enemy_factory
from enemy_factory_wiki import swordsman as swordsmen, hunterling as hunterlings, racer as racers, wasp as wasps, ogre as ogres, archer as archers, catapult as catapults, fury as furies, monster_rider as monster_riders, barrel_knight as barrel_knights, peasant as peasants, exploder as exploders, pikes, flying_mage as flying_mages, ram as rams, master_crossbowman as elite_crossbow_men

def nordfels_level_factory() -> Level:
    return Level([
        Wave([swordsmen(3)]),
        Wave([swordsmen(8)]),
        Wave([swordsmen(8), hunterlings(2)]),
        Wave([archers(24)]),
        Wave([racers(15)]),
        Wave([swordsmen(20), archers(20)]),
        Wave([wasps(15)]),
        Wave([swordsmen(30), hunterlings(10), racers(10)]),
        Wave([wasps(25), ogres(5)]),
        Wave([swordsmen(90), ogres(3)]),
        Wave([archers(50), racers(30)]),
        Wave([hunterlings(5)]),
        Wave([swordsmen(80), racers(35), wasps(30), archers(30), catapults(16), ogres(7), hunterlings(5)]),
    ])

def durstein_level_factory() -> Level:
    return Level([
        Wave([monster_riders(10), racers(9)]),
        Wave([peasants(18), racers(9)]),
        Wave([archers(14), monster_riders(8), swordsmen(2)]),
        Wave([swordsmen(30), archers(10), hunterlings(7)]),
        Wave([swordsmen(20), exploders(5)]),
        Wave([archers(30), hunterlings(12), monster_riders(10)]),
        Wave([archers(12), monster_riders(12), ogres(3), exploders(3)]),
        Wave([swordsmen(36), ogres(7), exploders(3)]),
        Wave([monster_riders(90)]),
        Wave([hunterlings(25), swordsmen(15), archers(15), racers(15), ogres(2), catapults(2), exploders(2)]),
        Wave([racers(35), ogres(14)]),
        Wave([monster_riders(150), swordsmen(50), archers(35), hunterlings(35), ogres(25), racers(20), exploders(20), catapults(3)]),
    ])


def frostsee_level_factory() -> Level:
    return Level([
        Wave([
            enemy_factory.swordsman(14),
        ]),
        Wave([
            enemy_factory.slime(34),
        ]),
        Wave([
            enemy_factory.master_crossbowman(8),
        ]),
        Wave([
            enemy_factory.slime(45),
        ]),
        Wave([
            enemy_factory.swordsman(10),
            enemy_factory.ram(),
        ]),
        Wave([
            enemy_factory.wasp(9),
        ]),
        Wave([
            enemy_factory.ram(2),
            enemy_factory.master_crossbowman(14),
        ]),
        Wave([
            enemy_factory.spiky_slime(30),
            enemy_factory.racer(8),
        ]),
        Wave([
            enemy_factory.wasp(33),
        ]),
        Wave([
            enemy_factory.ram(4),
            enemy_factory.master_crossbowman(10),
            enemy_factory.ogre(5),
            enemy_factory.swordsman(40),
        ]),
        Wave([
            enemy_factory.racer(30),
            enemy_factory.wasp(20),
            enemy_factory.spiky_slime(20),
        ]),
        Wave([
            enemy_factory.spiky_slime(34),
            enemy_factory.racer(20),
            enemy_factory.swordsman(45),
            enemy_factory.master_crossbowman(8),
            enemy_factory.spiky_slime(17),
            enemy_factory.hunterling(10),
            enemy_factory.ram(3),
            enemy_factory.ogre(6),
        ]),
    ])

def uferwind_level_factory() -> Level:
    return Level([
        Wave([peasants(47)]),
        Wave([archers(10), pikes(8)]),
        Wave([furies(7)]),
        Wave([archers(25), pikes(16)]),
        Wave([monster_riders(12), wasps(12), furies(8)]),
        Wave([barrel_knights(38)]),
        Wave([flying_mages(25)]),
        Wave([archers(25), pikes(25), wasps(16), furies(12)]),
        Wave([barrel_knights(45), flying_mages(35)]),
        Wave([furies(30), racers(25), wasps(20)]),
        Wave([flying_mages(40), pikes(40), ogres(12), rams(4)]),
        Wave([flying_mages(46), barrel_knights(42), furies(30), rams(7)]),
    ])

# def sturmklamm_level_factory() -> Level:
#     Wave([archers(3), pikes(3)]),
#     Wave([mole_knights(5)]),
#     Wave([archers(12), pikes(9)]),
#     Wave([wasps(8), furies(6)]),
#     Wave([mole_archers(8), mole_knights(8)]),
#     Wave([archers(30), ogres(6), catapults(3)]),
#     Wave([monster_riders(30), racers(30), mole_knights(20), flying_mages(20)]),
#     Wave([pikes(36), quickslings(9)]),
#     Wave([mole_archers(60), mole_knights(40), exploders(6)]),
#     Wave([racers(90), elite_crossbow_men(30), exploders(6)]),
#     Wave([wasps(30), flying_mages(30), furies(14)]),
#     Wave([mole_archers(85), mole_knights(70), swordsmen(45), racers(30), pikes(30), quickslings(16), exploders(10)]),
#     Wave([strange_statues(4)]),
def totend_level_factory():
    """
    20 Fire Snail
    6 Darf Warrior, 1 Iron Tower
    20 Flying Mage, 50 Small Spider, 10 Racer, 45 Slime, 25 Giraffe Slime
    15 Mole Warrior, 25 Spider, 15 Mole Archer
    1 Thing, 15 Fury, 2 Big Spider
    100 Fire Snail
    3 Ram, 3 Catapult, 6 Wheel, 3 Quicksling, 3 Iron Tower, 35 Ghost
    20 Wasp, 20 Bloodwing, 9 Exploder, 20 Fury, 120 Racer
    60 Fire Snail, 10 Catapult, 10 Flogre, 3 Thing, 20 Darf Warrior, 20 Master Crossbowmen, 20 Flail
    8 Exploder, 80 Archer, 15 Pikes, 15 Iron Tower, 25 Fire Snail, 20 Wind Boat
    7 Thing, 30 Fire Snail, 15 Big Spider, 30 Giraffe Slime
    75 Mole Archer, 25 Wheel, 75 Mole Warrior
    30 Fire Snail, 20 Quicksling, 100 Darf Warrior, 20 Ram
    9 Thing, 24 Iron Tower, 9 Catapult, 18 Big Spider, 20 Wind Boat, 40 Darf Warrior
    1 The Corrupt King
    """
