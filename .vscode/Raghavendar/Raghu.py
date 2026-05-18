def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

prime_numbers = [num for num in range(1, 101) if is_prime(num)]
print("Prime numbers from 1 to 100:")
print(prime_numbers)
