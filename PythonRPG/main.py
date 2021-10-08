import random
import storyLine


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

encounter_message_list = ["You traveled over Mountain tops, through dangerous valleys, and fought the cannon foughter, but now you must fight ", "After a long and treacherous journey, you found ",]

def heal_player():
    if Hercules['Level'] == 1:
        Hercules['Health'] = 100
    elif Hercules['Level'] == 5:
        Hercules['Health'] = 200
    elif Hercules['Level'] == 10:
        Hercules['Health'] = 300
    elif Hercules['Level'] == 15:
        Hercules['Health'] = 350


def level_up():
    new_health = Hercules['Health'] + 100
    new_attack_power = Hercules['Attack_Power'] + 10
    new_dodge = Hercules['Dodge'] + 5
    Hercules['Health'] = new_health
    Hercules['Attack_Power'] = new_attack_power
    Hercules['Dodge'] = new_dodge
    if Hercules['Level'] == 1:
        Hercules['Level'] = 5
    elif Hercules['Level'] == 5:
        Hercules['Level'] = 10
    elif Hercules['Level'] == 10:
        Hercules['Level'] = 15
    print(f'Congrats hero! You leved up!!')
    print(f'Your new lever is: ' + Hercules['Level'])
    print(f'Your new Health max is ' + Hercules['Health'])
    print(f'Your new Attack Power is ' + Hercules['Attack_Power'])


def the_adventure_begins():
    print('You have reached a 3 way fork in the road? How unexpected! Would you like to go left, straight, or right?')
    print()
    user_input = input('Please enter: Left, Straight, or Right').lower()
    if user_input == 'left':
        print()
        print("As you walk along the path you see mutilated bodies, and gaint prints in the ground that look like lion prints, wonder what it could be?")
        print()
        fight(Lion)
    elif user_input == 'straight':
        print()
        print(f'You went straight, in the distance you see a massive lake!')
        print()
        fight(Hydra)
    elif user_input == 'right':
        print()
        print(f'This path seems oddly gloomy and you sense an evil presence... ')
        print()
        fight(Cerberus)
    else:
        print('Please Try again!')
        the_adventure_begins()
    
def continue_():
    if Cerberus['Health'] <= 0 and Lion['Health'] <= 0 and Hydra['Health'] <= 0:
        storyLine.story_ends()
    elif Lion['Health'] > 0 and Hydra['Health'] > 0 and Cerberus['Health'] > 0:
        the_adventure_begins()
    elif Lion['Health'] <= 0 and Hydra['Health'] <= 0:
        print()
        print('Now there is only one more foe to battle, The Cerberus!! ONWARD!!')
        print()
        fight(Cerberus)
    elif Lion['Health'] <= 0 and Cerberus['Health'] <= 0:
        print()
        print('There be only one foe to battle left! The god of the Sea! Hydra!!!')
        print()
        fight(Hydra)
    elif Cerberus['Health'] <= 0 and Hydra['Health'] <= 0:
        print()
        print('Against all odds, you tackled the strongest foes alive First, now all that is left is the Lion!')
        print()
        fight(Lion)
    elif Lion['Health'] <= 0 and Hydra['Health'] > 0 and Cerberus['Health'] > 0:
        print()
        print(f'Amazing the great Hercules has slain the Lion!!')
        user_input = input('Where would you like to go next? Straight or Right?: ').lower()
        if user_input == 'straight':
            fight(Hydra)
        elif user_input == 'right':
            fight(Cerberus)
        else:
            print('That was not a valid input, please try again')
            print()
            continue_()
    elif Hydra['Health'] <= 0 and Lion['Health'] > 0 and Cerberus['Health'] > 0:
        print()
        print('The mighty Hercules has amazed the people with his risky Victory!')
        user_input = input('After slaying the Hydra, where would you like to go on the path of Destiny?: Left, or Right? ').lower()
        if user_input == 'left':
            fight(Lion)
        elif user_input == 'right':
            fight(Cerberus)
        else:
            print("That doesn't appear to be a valid answer. Here, try again!")
            print()
            continue_()
    elif Cerberus['Health'] <= 0 and Lion['Health'] > 0 and Hydra['Health'] > 0:
        print()
        print('OH MY GOODNESS! The people cheer Hercules all around the land!!! Who would have guessed he would first defeat the Cerberus!')
        user_input = input(f'Where would this great hero like to go next on the Path of Destiny!: Left or Straight? ').lower()
        if user_input == 'left':
            fight(Lion)
        elif user_input == 'straight':
            fight(Hydra)
        

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

def fight(monster):
    monster = monster['Name']
    print()
    print(encounter_message_list[random.randrange(0, 1)] + f"{monster}")
    print()
    while int(Hercules['Health']) > 0 and int(monster["Health"]) > 0:
        user_input = input("Choose your Attack!" + Hercules['Attacks']).lower()
        attack(user_input, monster)
        if monster["Health"] <= 0:
            print()
            print(f'{monster} has been defeated carry on with your quest!')
            level_up()
            print()
            heal_player()
            continue_()
        print(f'{monster} is preparing to attack')
        monster_attack(monster)
        if Hercules['Health'] <= 0:
            print()
            print(f'THE MIGHTY HERCULES WAS DEFEATED BY {monster}')
            print()
            print(f'You recover at your camp. Prepare for the next battle')
            heal_player()
            continue_()


def story_begins():
    print()
    print('Once Long ago, there was a great Hero by the Name of Hercules!')
    print('The god Zeus approached Hercules at a young age and told him:')
    print('"Young Child, inside you is a great strength! One day, you will')
    print(' come to the path of Destiny. There you will find the beginning')
    print(' to becoming a Legend of the People!" After that Zeus did not')
    print('again call on Hercules. At the age of 28, Hercules was on a walk')
    print('and he was already a Hero to the People. So he thought nothing of')
    print('the sign he found with "Destiny" scratched into it.')
    print('This is where you come into place, you will take control')
    print(' of our hero. Make the choices, and slay the enemies!')
    print()
    print('What will you do?')
    the_adventure_begins()

def story_ends():
    print()
    print('Congrats Great Hero Hercules!')
    print('Your name is all over the land!')
    print('You defeated all foes who challenged you!')
    print('Along with some of the greatest threats to the land')
    print('such as Cerberus, Hydra and the Lion Chimera!!')
    print('Where will your story take you next?')
    print('')
    print('Thank you for playing My development of the story of Hercules!')
    print()

story_begins()