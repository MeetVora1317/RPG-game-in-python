from sys import exit

def gold_room():
    print("the room is full of gold, How much you will take")

    choice= input()

    if '0' in choice or '1' in choice:
        how_much = int(choice)
    else:
        dead('man, learn to enter the number')
    if how_much < 50:
        print('Nice, you are not greedy , you won')
        exit(0)
    if how_much >50:
        dead('you are greedy , you are bad')


def bear_room():
    print('the bear is in the room')
    print('the bear has a bunch of honey')
    print('the fat bear is in front of another door')
    print('how are you going to move the bear')
    bear_moved = False

    while True:
        print('your choice are take hoeny, taunt bear, open door')
        choice  = input()
        if choice == 'take honey':
            dead('the bear looks at you and slaps your face off')
        elif choice == 'taunt bear' and not bear_moved:
            print('the bear from the door')
            print('you can go through the door')
            bear_moved = True
        elif choice == 'taunt bear' and bear_moved:
            dead('the bear gets pissed off and chew legs off')
        elif choice == 'open door':
            gold_room()
        else:
            print('I got no what does it means')
def dark_room():
    print('Here you see the great evil dark')
    print('he,it,whatever stares at you and you go insane')
    print('do you flee for your life or eat your head?')
    print('your choice is flee, head')
    choice = input()
    if choice == 'flee':
        start()
    elif choice == 'head':
        dead('well that was tasty')
    else:
        dark_room()

def start():
    print('you are in a dark room')
    print('there is a door on your left and right')

    choice = input()

    if choice == 'left':
        bear_room()
    elif choice == 'right':
        dark_room()
    else:
        print('you stumble around the room until you starve')


def dead(msg):
    print(msg+ 'Good job')

start()

