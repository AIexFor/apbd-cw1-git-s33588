numbers = []

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

print("Thats all prime numbers from 1 to 100")

for i in range(1, 100):
    if is_prime(i):
        numbers.append(i)

print(numbers)

def CalculateMax(values):
    max = -1
    for value in values:
        if value > max:
            max = value
    return max

def CalculateMin(values):
    min = 101
    for value in values:
        if value < min:
            min = value
    return min

def CalculateAverage(values):
    avg = 0
    for value in values:
        avg += value

    return avg / len(values)


print("thats lowest prime numbers from 1 to 100: ", CalculateMin(numbers))
print("thats highest prime numbers from 1 to 100: ", CalculateMax(numbers))

