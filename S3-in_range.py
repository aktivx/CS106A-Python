
def in_range(n, low, high):
    if n <= low <= high or high <= low <= n:
        return True
    else:
        return False


def main():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    num3 = int(input('Enter third number: '))
    if in_range(num1, num2, num3):
        print(str(num2) + ' is in between ' + str(num1) + ' and ' + str(num3))
    else:
        print(str(num2) + ' is not in between ' + str(num1) + ' and ' + str(num3))

if __name__ == "__main__":
    main()
