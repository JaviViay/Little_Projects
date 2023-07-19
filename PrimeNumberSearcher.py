currentN = str(input("Do you have a number to start or start from zero (y/n): "))

if currentN == "y":
    currentN = int(input("Enter the starting number: "))
elif currentN == "n":
    currentN = 0

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def search_prime(currentN):
    while True:
        if is_prime(currentN):
            print(currentN)
        currentN += 1

search_prime(currentN)