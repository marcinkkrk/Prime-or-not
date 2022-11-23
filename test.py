def primeOrNot(number):
    divisors = []
    if number > 0:
        a = number
        while a != 0:
            if number % a == 0:
                divisors.append(a)
            a-=1
        if len(divisors) == 2:
            print("This number is prime")

        else:
            print("This number is not prime")
    elif number == 0:
        "0 is not prime number"
    else:
        print('Number below 0 is not prime')

numberchoice = int(input("Give me number: "))
primeOrNot(numberchoice)