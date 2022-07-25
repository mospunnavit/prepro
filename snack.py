'''snack'''
def main():
    ''''''
    money = int(input())
    watercost = int(input())
    snack1 = int(input())
    snack2 = int(input())
    snack3 = int(input())
    money1 = money - watercost
    if money1 % 3 == 0:
        money1 -= 10 * snack1
        cast1 = 10
    elif money1 % 3 == 1:
        money1 -= 15 * snack1
    elif money1 % 3 == 2:
        money1 -= 20 * snack1

    if money1 % 3 == 0:
        money1 -= 12 * snack2
    elif money1 % 3 == 1:
        money1 -= 15 * snack2
    elif money1 % 3 == 2:
        money1 -= 18 * snack2

    if money1 % 3 == 0:
        money1 -= 5 * snack3
    elif money1 % 3 == 1:
        money1 -= 7 * snack3
    elif money1 % 3 == 2:
        money1 -= 9 * snack3

    if money1 < 0:
        print("Now you have %d left." %money1)
        print("You don't have enough money!")

    else:
        print("Now you have %d left." %money1)
        print("Here's your order!")   
        print("Water: %d baht")        
        print("Snack number 1: %d baht")
        print("Snack number 2: %d baht")
        print("Snack number 3: %d baht")


