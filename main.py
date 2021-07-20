from random import randrange


def rolling_dice(sides):
    dice = 0
    while dice < 1 or dice > sides:
        if sides == 0 or sides < 0:
            break
        dice = randrange(1, sides+1)
    return 0 if sides == 0 else dice


run = True
while run:
    side = int(input('How many sides do you want? '))
    print('Dice: ', rolling_dice(side))
    chose = input('Want to rolling dice again? (y/n) ')
    if chose == 'n':
        run = False

print('\nThank you so much!')
