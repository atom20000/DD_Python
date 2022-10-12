from dataclasses import dataclass
import faker
import random


PERKS = [
    'Black Widow',
    'Lady Killer',
    'Daddy\'s Boy',
    'Daddy\'s Girl',
    'Gun Nut',
    'Little Leaguer',
    'Thief',
    'Swift Learner',
    'Intense Training',
    'Child at Heart',
    'Comprehension',
    'Educated',
    'Entomologist',
    'Scoundrel',
    'Iron Fist',
    'Bloody Mess',
    'Lead Belly',
    'Toughness',
    'Fortune Finder',
    'Gunslinger',
    'Demolition Expert',
    'Commando',
    'Rad Resistance',
    'Scrounger',
    'Size Matters',
    'Strong Back',
    'Impartial Mediation',
    'Animal Friend',
    'Finesse',
    'Mister Sandman',
    'Mysterious Stranger',
    'Nerd Rage!',
    'Night Person',
    'Here and Now',
    'Pyromaniac',
    'Cannibal',
    'Life Giver',
    'Robotics Expert',
    'Sniper',
    'Silent Running',
    'Fast Metabolism',
    'Lawbringer',
    'Chemist',
    'Contract Killer',
    'Cyborg',
    'Light Step',
    'Master Trader',
    'Adamantium Skeleton',
    'Tag!',
    'Better Criticals',
    'Action Boy/Action Girl',
    'Chem Resistant',
    'Infiltrator',
    'Computer Whiz',
    'Concentrated Fire',
    'Paralyzing Palm',
    'Solar Powered',
    'Ninja',
    'Grim Reaper\'s Sprint',
    'Explorer',
    'Dream Crusher',
    'Hematophage',
    'Power Armor Training',
    'Ant Might',
    'Ant Sight',
    'Barkskin',
    'Rad Regeneration',
    'Survival Expert (Junior Survivor / Survival Guru)',
    'Wired Reflexes',
    'Deep Sleep',
    'Puppies!',
    'Quantum Chemist',
    'Devil\'s Highway',
    'Escalator to Heaven',
    'Karmic Rebalance',
    'No Weaknesses',
    'Rad Tolerance',
    'Warmonger',
    'Nerves of Steel',
    'Party Girl/Party Boy',
    'Rad Absorption',
    'Nuclear Anomaly',
    'Almost Perfect',
    'Xenotech Expert',
    'Ghoul Ecology',
    'Covert Ops',
    'Auto Axpert',
    'Booster Shot',
    'Pitt Fighter',
    'Punga Power!',
    'Superior Defender',
    'Mirelurk Ecology',
    'Gray Matters',
    'Swing for the Fences',
]

@dataclass
class STATS():
    action_points: int
    carry_weight: int
    critical_chance: int
    damage_resistance: int
    fire_resistance: int
    hit_points: int
    melee_damage: int
    poison_resistance: int
    radiation_resistance: int
    skill_rate: int
    unarmed_damage: int

@dataclass
class SPECIAL():
    strenght: int
    perception: int
    endurance: int
    charisma: int
    intelligence: int
    agility: int
    luck: int

@dataclass
class SKILLS():
    barter: int
    big_guns: int
    energy_weapons: int
    explosives: int
    lockpick: int
    medicine: int
    melee_weapons: int
    repair: int
    science: int
    small_guns: int
    sneak: int
    speech: int
    unarmed: int


class Character():

    def __init__(self, name, age, level, special=None, perks=None):
        self.name = name
        self.age = age
        self.level = level
        self.special : SPECIAL = special if special else SPECIAL(
            strenght = random.randrange(1, 11),
            perception = random.randrange(1, 11),
            endurance = random.randrange(1, 11),
            charisma = random.randrange(1, 11),
            intelligence = random.randrange(1, 11),
            agility = random.randrange(1, 11),
            luck = random.randrange(1, 11)
        )
        
        self.skills : SKILLS = SKILLS(
            barter = int((self.special.charisma * 2) +2 + (self.special.luck / 2)),
            big_guns = int((self.special.endurance * 2) +2 + (self.special.luck / 2)),
            energy_weapons = int((self.special.perception * 2) +2 + (self.special.luck / 2)),
            explosives = int((self.special.perception * 2) +2 + (self.special.luck / 2)),
            lockpick = int((self.special.perception * 2) +2 + (self.special.luck / 2)),
            medicine = int((self.special.intelligence * 2) +2 + (self.special.luck / 2)),
            melee_weapons = int((self.special.strenght * 2) +2 + (self.special.luck / 2)),
            repair = int((self.special.intelligence * 2) +2 + (self.special.luck / 2)),
            science = int((self.special.intelligence * 2) +2 + (self.special.luck / 2)),
            small_guns = int((self.special.agility * 2) +2 + (self.special.luck / 2)),
            sneak = int((self.special.charisma * 2) +2 + (self.special.luck / 2)),
            speech = int((self.special.charisma * 2) +2 + (self.special.luck / 2)),
            unarmed = int((self.special.endurance * 2) +2 + (self.special.luck / 2))
        )

        self.stats : STATS= STATS(
            action_points = self.special.agility * 2 + 65,
            carry_weight = self.special.strenght * 10 + 150,
            critical_chance = self.special.luck,
            damage_resistance = 0,
            fire_resistance = 0,
            hit_points = self.special.endurance * 20 + 100,
            melee_damage = int(self.special.strenght * 0.5),
            poison_resistance = (self.special.endurance - 1) * 5,
            radiation_resistance = (self.special.endurance - 1) * 2,
            skill_rate = self.special.intelligence + 10,
            unarmed_damage = int(self.skills.unarmed / 20 + 0.5),
        )

        self.perks = perks if perks else random.sample(PERKS, k = 4)

    def __repr__(self) -> str:
        return f"""
        NAME: {self.name}
        Age: {self.age}
        Level: {self.level}
        SPECIAL:
            Strength: {self.special.strenght}
            Perception: {self.special.perception}
            Endurance: {self.special.endurance}
            Charisma: {self.special.charisma}
            Intelligence: {self.special.intelligence}
            Agility: {self.special.agility}
            Luck: {self.special.luck}
        Stats:
            Action Points: {self.stats.action_points}
            Carry Weight: {self.stats.carry_weight} lbs
            Critical Chance: {self.stats.critical_chance} %
            Damage Resistance: {self.stats.damage_resistance}
            Fire Resistance: {self.stats.fire_resistance}
            Hit Points: {self.stats.hit_points}
            Melee Damage: {self.stats.melee_damage}
            Poison Resistance: {self.stats.poison_resistance} %
            Radiation Resistance: {self.stats.radiation_resistance} %
            Skill Rate: {self.stats.skill_rate}
            Radiation Resistance: {self.stats.radiation_resistance}
            Unarmed Damage: {self.stats.unarmed_damage}
        Skills:
            Barter: {self.skills.barter}
            Big Guns: {self.skills.big_guns}
            Energy Weapons: {self.skills.energy_weapons}
            Explosives: {self.skills.explosives}
            Lockpick: {self.skills.lockpick}
            Medicine: {self.skills.medicine}
            Melee Weapons: {self.skills.melee_weapons}
            Repair: {self.skills.repair}
            Science: {self.skills.science}
            Small Guns: {self.skills.small_guns}
            Sneak: {self.skills.sneak}
            Speech: {self.skills.speech}
            Unarmed: {self.skills.unarmed}
        Perks:
        {', '.join(list(map(lambda x: '    ' + x, self.perks)))}
        """


if __name__ == '__main__':
    fake = faker.Faker()
    print(Character(
        name = fake.name(),
        age = random.randrange(1,150),
        level = random.randrange(1, 51),
    ))