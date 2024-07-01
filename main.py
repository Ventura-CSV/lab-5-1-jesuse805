def getinput():
    # input prompt for number
    num = int(input('Enter a number: '))
    # returns the number in the prompt
    return num

def getsum(v1, v2):
    # adds v1 & v2 
    total = v1 + v2
    # returns total
    return total

def printval(v1, v2, total):
    # prints v1, v2, total
    print (v1, v2, total)


def main():
    # calls for input 1
    userval1 = getinput()
    # calls for input 2
    userval2 = getinput()
    # calls getsum with val1 & val2
    total = getsum(userval1, userval2)
    # calls printval with userval1, userval2, total
    printval(userval1, userval2, total)


if __name__ == '__main__':
    main()
