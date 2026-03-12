def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

print("Thats all prime numbers from 1 to 100")

print(*(n for n in range(1, 100) if is_prime(n)))

