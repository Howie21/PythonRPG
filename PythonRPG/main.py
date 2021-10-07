import random


Hercules = {
    'Level': 1,
    'Name': 'Hercules',
    'Health': 100,
    'Attack_Power': 5,
    'Attacks': ['punch', 'stab', 'club'],
    'Dodge': 5
}

Lion = {
    'Name': 'The Nemean Lion',
    'Health': 100,
    'Attack_Power': 5,
    'Attacks': ['bite', 'claw', 'pounce'],
    'Dodge': 5
}

Hydra = {
    'Name': 'The Nine Headed Lernaean Hydra',
    'Health': 250,
    'Attack_Power': 10,
    'Attacks': ['bite', 'claw', 'multi attack'],
    'Dodge': 10
}

Cerberus = {
    'Name': 'Cerberus',
    'Health': 350,
    'Attack_Power': 15,
    'Attacks': ['Bite', 'Swipe', 'Chew'],
    'Dodge': 10
}
def heal_player():
    if Hercules['Level'] == 1:
        Hercules['Health'] = 100
    elif Hercules['Level'] == 5:
        Hercules['Health'] = 200
    elif Hercules['Level'] == 10:
        Hercules['Health'] = 300

def level_up():
    new_health = Hercules['Health'] + 100
    new_attack_power = Hercules['Attack_Power'] + 10
    new_dodge = Hercules['Dodge'] + 5
    Hercules['Health'] = new_health
    Hercules['Attack_Power'] = new_attack_power
    Hercules['Dodge'] = new_dodge
    if Hercules['Level'] == 1:


def attack(string, monster):
    user_attack = string
    monster_name = monster['Name']
    monster_dodge_chance = random.randrange(0, monster['Dodge'])
    user_hit_damage = random.randrange(0, Hercules['Attack_Power'])
    if user_hit_damage >= monster_dodge_chance:
        if user_attack in Hercules['Attacks']:
            print(f"You try to {user_attack} {monster_name} ")
            print()
            print()
            if user_attack == 'punch':
                damage_to_monster = Hercules['Attack_Power'] * user_hit_damage + 10
            elif user_attack == 'club':
                damage_to_monster = Hercules['Attack_Power'] * user_hit_damage + 15
            elif user_attack == 'stab':
                damage_to_monster = Hercules['Attack_Power'] * 2 
            print()
            print(f"Amazing, you did {damage_to_monster} damage to {monster_name} with {user_attack}")
            print()
            new_monster_hp = int(monster['Health']) - int(damage_to_monster)
            monster['Health'] = new_monster_hp
            print(f'{monster_name} has {new_monster_hp} Health left! Keep fighting loyal Hercules!')
            print()
        elif user_attack not in Hercules['Attacks']:
            print()
            print(f'{user_attack} does not appear to be in Hercules arsenal. You miss this round!! Sorry!')
            print()
    else:
        print(f'You tried {user_attack} against {monster_name}')
        print()
        print(f'{monster_name} dodged your attack')
        print()


def monster_attack(monster):
    name = monster['Name']
    monster_hit = random.randrange(0, monster['Attack_Power'])
    user_dodge = random.randrange(0, Hercules['Dodge'])
    if monster_hit > user_dodge:
        monster_attacks_player = monster['Attacks'][random.randrange(0, len(monster['Attacks']))]
        damage_to_player = monster['Attack_Power'] * 2
        print()
        print(f'{name} hit you for {damage_to_player} using {monster_attacks_player}')
        print()
        new_player_hp = int(Hercules['Health']) - int(damage_to_player)
        if Hercules['Health'] > 0:
            print()
            print(f'Be careful! You have {new_player_hp} Health left')
            print()
        elif Hercules['Health'] <= 0:
            print()
            print(f'The {name} knocked you out. You have {new_player_hp} health left!')
    else:
        print()
        print(f"You successfully doged the {name}'s attack")

