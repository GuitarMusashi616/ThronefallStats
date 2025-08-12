# pyright: strict

from enemy import Enemy, EnemyTrait, EnemyTraits

def swordsman(quantity: int = 1) -> Enemy:
    return Enemy(
        'Swordsman',
        EnemyTraits([
            EnemyTrait.MELEE,
        ]),
        quantity,
        hp=25
    )

def archer(quantity: int = 1) -> Enemy:
    return Enemy(
        'Archer',
        EnemyTraits([
            EnemyTrait.RANGED,
            EnemyTrait.TOWER_VULNERABLE,
        ]),
        quantity,
        hp=20
    )

def catapult(quantity: int = 1) -> Enemy:
    return Enemy(
        'Catapult',
        EnemyTraits([
            EnemyTrait.RANGED,
            EnemyTrait.SIEGE,
        ]),
        quantity,
        hp=45
    )

def monster_rider(quantity: int = 1) -> Enemy:
    return Enemy(
        'Monster Rider',
        EnemyTraits([
            EnemyTrait.MELEE,
            EnemyTrait.FAST,
            EnemyTrait.MONSTER,
        ]),
        quantity,
        hp=40
    )

def exploder(quantity: int = 1) -> Enemy:
    return Enemy(
        'Exploder',
        EnemyTraits([
            EnemyTrait.MELEE,
            EnemyTrait.MONSTER,
            EnemyTrait.FAST,
            EnemyTrait.HERO_RESISTANT,
        ]),
        quantity,
        hp=60
    )

def peasant(quantity: int = 1) -> Enemy:
    return Enemy(
        'Peasant',
        EnemyTraits([
            EnemyTrait.MELEE,
        ]),
        quantity,
        hp=8.7,
    )

def pikes(quantity: int = 1) -> Enemy:
    return Enemy(
        'Pikes',
        EnemyTraits([
            EnemyTrait.MELEE,
            EnemyTrait.RANGED_VULNERABLE,
        ]),
        quantity,
        hp=25
    )


def flying_mage(quantity: int = 1) -> Enemy:
    return Enemy(
        'Flying Mage',
        EnemyTraits([
            EnemyTrait.RANGED,
            EnemyTrait.FLYING,
        ]),
        quantity,
        hp=45
    )

def fury(quantity: int = 1) -> Enemy:
    return Enemy(
        'Fury',
        EnemyTraits([
            EnemyTrait.RANGED,
            EnemyTrait.RANGED_VULNERABLE,
        ]),
        quantity,
        hp=75,
    )

def barrel_knight(quantity: int = 1) -> Enemy:
    return Enemy(
        'Barrel Knight',
        EnemyTraits([
            EnemyTrait.MELEE,
            EnemyTrait.SIEGE,
        ]),
        quantity,
        hp=100,
    )

def slime(quantity: int = 1) -> Enemy:
    return Enemy(
        'Slime',
        EnemyTraits([
            EnemyTrait.MONSTER,
            EnemyTrait.MELEE,
        ]),
        quantity,
        hp=12.5
    )

def master_crossbowman(quantity: int = 1) -> Enemy:
    return Enemy(
        'Master Crossbowman',
        EnemyTraits([
            EnemyTrait.RANGED,
            EnemyTrait.TOWER_VULNERABLE,
        ]),
        quantity,
        hp=40
    )

def ram(quantity: int = 1) -> Enemy:
    return Enemy(
        'Ram',
        EnemyTraits([
            EnemyTrait.MELEE,
            EnemyTrait.SIEGE,
            EnemyTrait.RANGED_RESISTANT,
            EnemyTrait.HIGH_HEALTH
        ]),
        quantity,
        hp=250,
    )

def wasp(quantity: int = 1) -> Enemy:
    return Enemy(
        'Wasp',
        EnemyTraits([
            EnemyTrait.RANGED,
            EnemyTrait.FLYING,
            EnemyTrait.MONSTER,
        ]),
        quantity,
        hp=25
    )

def spiky_slime(quantity: int = 1) -> Enemy:
    return Enemy(
        'Spiky Slime',
        EnemyTraits([
            EnemyTrait.MELEE,
            EnemyTrait.MONSTER,
        ]),
        quantity,
        hp=50
    )

def racer(quantity: int = 1) -> Enemy:
    return Enemy(
        'Racer',
        EnemyTraits([
            EnemyTrait.MELEE,
            EnemyTrait.FAST,
            EnemyTrait.MONSTER,
            EnemyTrait.HERO_RESISTANT,
        ]),
        quantity,
        hp=35
    )

def ogre(quantity: int = 1) -> Enemy:
    return Enemy(
        'Ogre',
        EnemyTraits([
            EnemyTrait.MELEE,
            EnemyTrait.HIGH_HEALTH,
        ]),
        quantity,
        hp=200
    )

def hunterling(quantity: int = 1) -> Enemy:
    return Enemy(
        'Hunterling',
        EnemyTraits([
            EnemyTrait.MELEE,
            EnemyTrait.FAST,
            EnemyTrait.MONSTER,
        ]),
        quantity,
        hp=30
    )
