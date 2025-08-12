# pyright: strict

from unit import Unit


def berserks(quantity: int):
    return Unit(
        name="Berserks",
        quantity=quantity,
        attacks_per_second=2,
        attack_range=3,
        base_dmg=2.5,
        dmg_vs_siege=2,
        hp=65,
        movement_speed=6.5,
        cost=4,
    )

def knights(quantity: int):
    return Unit(
        name="Knights",
        quantity=quantity,
        attacks_per_second=1,
        attack_range=3.5,
        base_dmg=2.5,
        hp=100,
        movement_speed=4,
        cost=4,
    )

def flails(quantity: int):
    return Unit(
        name="Flails",
        quantity=quantity,
        attacks_per_second=1,
        attack_range=4,
        base_dmg=1.5,
        hp=70,
        movement_speed=5,
        cost=4,
    )

def spearman(quantity: int):
    return Unit(
        name="Spearman",
        quantity=quantity,
        attacks_per_second=2,
        attack_range=4.5,
        base_dmg=1.75,
        dmg_vs_ranged=0.75,
        dmg_vs_fast=1.75,
        hp=60,
        movement_speed=8,
        cost=4,
    )

def longbows(quantity: int):
    return Unit(
        name="Long Bows",
        quantity=quantity,
        attacks_per_second=0.5,
        attack_range=40,
        attack_range_vs_flying=1.25,
        base_dmg=4,
        dmg_vs_flying=1.2,
        dmg_vs_ranged_resistant=0.5,
        hp=15,
        movement_speed=9,
        cost=4,
    )

def crossbowmen(quantity: int):
    return Unit(
        name="Crossbowmen",
        quantity=quantity,
        attacks_per_second=0.5,
        attack_range=13,
        base_dmg=7,
        dmg_vs_ranged=2,
        dmg_vs_flying=0.5,
        dmg_vs_ranged_resistant=0.4,
        hp=35,
        movement_speed=4,
        cost=4,
    )

def hunters_ranged(quantity: int):
    return Unit(
        name="Hunters",
        quantity=quantity,
        attacks_per_second=0.714,
        attack_range=25,
        attack_range_vs_monsters=1.4,
        base_dmg=3.5,
        dmg_vs_monsters=2,
        dmg_vs_air_not_monster=0.5,
        dmg_vs_ranged_resistant=0.5,
        hp=45,
        movement_speed=6,
        cost=4,
    )

def hunters_melee(quantity: int):
    return Unit(
        name="Hunters",
        quantity=quantity,
        attacks_per_second=2,
        attack_range=3.5,
        base_dmg=3.5,
        dmg_vs_monsters=2,
        hp=45,
        movement_speed=6,
        cost=4,
    )

def fire_archers(quantity: int):
    return Unit(
        name="Fire Archers",
        quantity=quantity,
        attacks_per_second=0.333,
        attack_range=25,
        base_dmg=5.4*7,
        dmg_vs_siege=3,
        hp=30,
        movement_speed=5,
        cost=4,
    )

def tower(quantity: int):
    return Unit(
        name="Tower",
        quantity=quantity,
        attacks_per_second=0.5,
        attack_range=36,
        base_dmg=8,
        dmg_vs_flying=1.15,
        dmg_vs_ranged_resistant=0.6,
        dmg_vs_tower_vulnerable=2,
        hp = 100,
        movement_speed=0,
        cost = 3,
    )

def castle_tower(quantity: int):
    return Unit(
        name="Castle Tower",
        quantity=quantity,
        attacks_per_second=0.714,
        attack_range=36,
        base_dmg=8,
        dmg_vs_flying=1.15,
        dmg_vs_ranged_resistant=0.6,
        dmg_vs_tower_vulnerable=2,
        hp = 250,
        movement_speed=0,
        cost = 8,
    )

def sniper_tower(quantity: int):
    return Unit(
        name="Sniper Tower",
        quantity=quantity,
        attacks_per_second=0.25,
        attack_range=54,
        base_dmg=22.4,
        dmg_vs_flying=1.15,
        dmg_vs_ranged_resistant=0.6,
        dmg_vs_tower_vulnerable=2,
        hp = 250,
        movement_speed=0,
        cost = 8,
    )

def armoured_tower(quantity: int):
    return Unit(
        name="Armored Tower",
        quantity=quantity,
        attacks_per_second=0.5,
        attack_range=36,
        base_dmg=8,
        dmg_vs_flying=1.15,
        dmg_vs_ranged_resistant=0.6,
        dmg_vs_tower_vulnerable=2,
        hp = 450,
        movement_speed=0,
        cost = 8,
    )

def bunker_tower(quantity: int):
    return Unit(
        name="Bunker Tower",
        quantity=quantity,
        attacks_per_second=0.5,
        attack_range=19.8,
        base_dmg=8,
        dmg_vs_flying=1.15,
        dmg_vs_ranged_resistant=0.6,
        dmg_vs_tower_vulnerable=2,
        hp = 175,
        movement_speed=0,
        cost = 8,
    )

def castle_archer_spire(quantity: int):
    return Unit(
        name="Castle Archer Spire",
        quantity=quantity,
        attacks_per_second=1,
        attack_range=36,
        base_dmg=8,
        dmg_vs_flying=1.15,
        dmg_vs_ranged_resistant=0.6,
        dmg_vs_tower_vulnerable=2,
        hp = 600,
        movement_speed=0,
        cost = 23,
    )

def golem(quantity: int):
    return Unit(
        name="Golem",
        quantity=quantity,
        attacks_per_second=0.333,
        attack_range=4.5,
        base_dmg=30,
        hp=300,
        movement_speed=4,
        cost=6,
    )

def firewing(quantity: int):
    return Unit(
        name="Firewing",
        quantity=quantity,
        attacks_per_second=1,
        attack_range=45,
        attack_range_vs_flying=35,
        base_dmg=4,
        hp=30,
        movement_speed=10,
        cost=6,
    )

def lizard_rider_melee(quantity: int):
    return Unit(
        name="Lizard Rider (Melee)",
        quantity=quantity,
        attacks_per_second=2,
        attack_range=5.5,
        base_dmg=3.5,
        hp=60,
        movement_speed=13,
        cost=6,
    )

def lizard_rider_ranged(quantity: int):
    return Unit(
        name="Lizard Rider (Ranged)",
        quantity=quantity,
        attacks_per_second=2,
        attack_range=30,
        base_dmg=6,
        hp=60,
        movement_speed=13,
        cost=6,
    )

def support_mage(quantity: int):
    return Unit(
        name="Support Mage (heals)",
        quantity=quantity,
        attacks_per_second=1.5,
        attack_range=26,
        base_dmg=14,
        hp=25,
        movement_speed=9,
        cost=6,
    )

if __name__ == "__main__":
    berserks_units = berserks(4)
    berserks_units.print()
    knights_units = knights(4)
    knights_units.print()
    flails_units = flails(4)
    flails_units.print()
    spearman_units = spearman(4)
    spearman_units.print()
    longbows_units = longbows(4)
    longbows_units.print()
    crossbowmen_units = crossbowmen(4)
    crossbowmen_units.print()
    hunters_ranged_units = hunters_ranged(4)
    hunters_ranged_units.print()
    hunters_melee_units = hunters_melee(4)
    hunters_melee_units.print()
    fire_archers_units = fire_archers(4)
    fire_archers_units.print()
    tower_units = tower(1)
    tower_units.print()
    castle_tower_units = castle_tower(1)
    castle_tower_units.print()
    sniper_tower_units = sniper_tower(1)
    sniper_tower_units.print()
    armoured_tower_units = armoured_tower(1)
    armoured_tower_units.print()
    bunker_tower_units = bunker_tower(1)
    bunker_tower_units.print()
    castle_archer_spire_units = castle_archer_spire(1)
    castle_archer_spire_units.print()
    golem_units = golem(1)
    golem_units.print()
    firewing_units = firewing(1)
    firewing_units.print()
    lizard_rider_melee_units = lizard_rider_melee(1)
    lizard_rider_melee_units.print()
    lizard_rider_ranged_units = lizard_rider_ranged(1)
    lizard_rider_ranged_units.print()
    support_mage_units = support_mage(1)
    support_mage_units.print()