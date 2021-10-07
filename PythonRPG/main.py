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



