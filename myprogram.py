'''print("Hello, World")
print(1)
print("Hello, World " + str(1))

name = input("Give me your name")

print("You are a nice person " + name)

number = int(input("Give me a number"))

print(number + 1)

print(15/4)

print(15//4)

print(15%4)

print(5**200)

number = 2000000000

print(number*2)

counter = 1
sign = 1
sum = 0.0

while(counter<10000000):
    sum += sign/counter

    sign *= -1

    counter += 2

print(sum*4)

def squareroot(number):
    guess = 0.1

    newguess = 1.0

    while(abs(guess - newguess) > 0.00000000001):
        guess = newguess

        newguess = (guess + number/guess)/2

    return(newguess)

counter = 2

while(counter<=100):
    print(squareroot(counter))

    counter += 1'''

def gcd(first,second):
    remainder = 1

    while(remainder > 0):
        remainder = first%second

        first = second
        second = remainder

    return(first)

print(gcd(42,9

          ))

