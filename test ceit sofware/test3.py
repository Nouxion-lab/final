import hashlib

def find_smallest_integer(secret_key):
    target_prefix = "000000"  

    i = 0
    while True:
        candidate = f"{secret_key}{i}"
        hash_value = hashlib.md5(candidate.encode()).hexdigest()

        if hash_value.startswith(target_prefix):
            return i
        i += 1

secret_key = "iqwjasdirjuwjq"
result = find_smallest_integer(secret_key)
print(f"The smallest integer for the given secret key is: {result}")