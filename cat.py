'''cat'''
def main():
    '''procat'''
    catgrade = float(input())
    secgrade = float(4.00 - catgrade)
    if catgrade < 1.00:
        print("I'm so sad.")
    elif catgrade < 2.00:
        print("%0.2f"%secgrade)
    elif catgrade >= 2.00:
        print("I'm so happy.")
main()
