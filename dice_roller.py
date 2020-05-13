import random

def main():
    dicerolls = 2
    dicesum = 0
    for i in range(0, dicerolls):
        roll = random.randint(1,6)
        dicesum += roll
        print(f'You rolled a {roll}')
    print(f'You rolled a total of {dicesum}')

if __name__== "__main__":
  main()
