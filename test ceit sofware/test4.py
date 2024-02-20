def prime_factors(n):
    factors = ''
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors += str(divisor) + ''
            n //= divisor
        divisor += 1
    
    return factors.strip()

input_number = 87492774 
output_factors = prime_factors(input_number)

print(f"Prime Factors ของ {input_number} คือ: {output_factors}")


