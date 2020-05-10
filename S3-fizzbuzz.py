def fizzbuzz(n):
    Fizzbuzz = 0
    Fizz = 0
    Buzz = 0
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('Fizzbuzz')
            Fizzbuzz += 1
        elif i % 3 == 0:
            print('Fizz')
            Fizz += 1
        elif i % 5 == 0:
            print('Buzz')
            Buzz += 1
        else:
            print(i)
    result = str(Fizzbuzz) + ' of Fizzbuzz, ' + str(Fizz) + ' of Fizz, ' + str(Buzz) + ' of Buzz'
    return result


def main():
    num = int(input('Number to count to: '))
    a = fizzbuzz(num)
    print(a)

if __name__ == "__main__":
    main()
