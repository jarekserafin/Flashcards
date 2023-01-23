import random


def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key
    return "key doesn't exist"


def add_card(my_dict):
    while True:
        print('The card:')
        term = input()
        if term in my_dict.keys():
            print('The card "' + term + '" already exists. Try again:')
            continue
        else:
            break
    print('The definition of the card:')
    while True:
        definition = input()
        if definition in my_dict.values():
            print('The definition "' + definition + '" already exists. Try again:')
            continue
        else:
            break
    cards[term] = definition
    print('The pair ("' + term + '":"' + definition + '") has been added.')


def remove_card(my_dict):
    print('Which card?')
    card = input()
    if card in my_dict.keys():
        my_dict.pop(card)
        print('The card has been removed.')
    else:
        print('Can\'t remove "' + card + '": there is no such card.')


def import_cards(my_dict):
    print('File name:')
    file_path = input()
    try:
        with open(file_path, 'r') as file:
            i = 1
            temp = file.readlines()
            counter = 0
            for line in temp:
                val = line.split(" ")
                my_dict[val[0]] = val[1].strip()
                counter += 1
        print(str(counter) + " cards have been loaded.")
    except FileNotFoundError:
        print('File not found.')


def export(my_dict):
    print('File name:')
    file_path = input()
    with open(file_path, 'w') as file:
        for i in my_dict:
            file.write(i + " " + my_dict[i] + "\n")
    print(str(len(my_dict)) + ' cards have been saved.')


def ask(my_dict):
    print('How many times to ask?')
    n = int(input())
    keys = [x for x in my_dict.keys()]
    for i in range(n):
        key = random.choice(keys)
        print('Print the definition of "' + key + '":')
        definition = input()
        if definition == cards[key]:
            print('Correct!')
        elif definition in cards.values():
            right_term = get_key(definition, cards)
            print('Wrong. The right answer is "' + cards[key] + '", but your definition is correct for "' + right_term + '":')
        else:
            print('Wrong. The right answer is "' + cards[key] + '".')


message_0 = 'Input the action (add, remove, import, export, ask, exit):'
actions = ['add', 'remove', 'import', 'export', 'ask', 'exit']
cards = dict()

while True:
    print(message_0)
    action = input()
    if action == 'add':
        add_card(cards)
    elif action == 'exit':
        print('Bye bye!')
        break
    elif action == 'remove':
        remove_card(cards)
    elif action == 'export':
        export(cards)
    elif action == 'import':
        import_cards(cards)
    elif action == 'ask':
        ask(cards)
