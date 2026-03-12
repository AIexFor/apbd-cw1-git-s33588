def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

print("Thats all prime numbers from 1 to 100")

print(*(n for n in range(1, 100) if is_prime(n)))

def CalculateMax(values):
    max = 0
    for value in values:
        if value > max:
            max = value

def CalculateMin(values):
    min = 0
    for value in values:
        if value < min:
            min = value

