
filename = "input.txt"

with open(filename, 'r') as file:
    lines = file.readlines()

count_valid = 0

for line in lines:
    sides = tuple(map(int, line.split()))
    if len(sides) == 3:
        a, b, c = sides
        if (a + b > c) and (a + c > b) and (b + c > a):
            count_valid += 1

print(f"Number of valid triangles: {count_valid}")



