with open('input.txt') as file:
    rotations = [line.rstrip() for line in file]
    
position = 50
zero_amount = 0

for rotation in rotations:
    direction = rotation[0]
    distance = int(rotation[1:])
    
    if direction == 'R':
        zero_amount += (position + distance) // 100
        position = (position + distance) % 100
    else:
        zero_amount += (position + 99) // 100 - (position - distance + 99) // 100
        position = (position - distance) % 100

print(zero_amount)