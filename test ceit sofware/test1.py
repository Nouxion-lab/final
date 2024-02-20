def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_and_sum(limit):
    primes = [num for num in range(limit) if is_prime(num)]
    sum_of_primes = sum(primes)
    return primes, sum_of_primes

limit = 1000
prime_numbers, sum_of_primes = find_primes_and_sum(limit)

print(f"Prime Numbers: {prime_numbers}")
print(f"Sum of Prime Numbers: {sum_of_primes}")