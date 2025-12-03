START = 50
TOTAL_NUMBERS = 100

def get_rotations(filename):
    with open(filename) as file:
        rotations = [line.rstrip() for line in file]
    
    return rotations

def main():
    rotations = get_rotations('input.txt')
    
    position = START
    zero_amount = 0

    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        
        if direction == 'R':
            # count how many times we pass zero going right
            zero_amount += (position + distance) // TOTAL_NUMBERS
            position = (position + distance) % TOTAL_NUMBERS
        else:
            # count how many times we pass zero going left
            zero_amount += (position + (TOTAL_NUMBERS - 1)) // TOTAL_NUMBERS - (position - distance + (TOTAL_NUMBERS - 1)) // TOTAL_NUMBERS
            position = (position - distance) % TOTAL_NUMBERS

    print(zero_amount)
    
if __name__ == "__main__":
    main()