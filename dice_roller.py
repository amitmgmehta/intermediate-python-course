import random

def main():
    dicerolls = int(input('Enter the number of dices you want to roll here: '))
    diceface = int(input('Enter the number of sides per dice: '))
    dicesum = 0
    for i in range(0, dicerolls):
        roll = random.randint(1,diceface)
        dicesum += roll
        if roll == 1:
            print(f'You rolled a {roll}! Critical failure.')
        elif roll == 6:
            print(f'You rolled a {roll}! Critical success.')
        else:
            print(f'You rolled a {roll}.')
    print(f'You rolled a total of {dicesum}')

if __name__== "__main__":
  main()
