def get_grid(filename):
    with open(filename) as file:
        grid = [line.rstrip() for line in file]
    
    return grid

def get_roll_positions(grid):
    positions = set()
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char == '@':
                positions.add((row, col))
    
    return positions

def get_total_removable_rolls(rolls):
    total_removed = 0
    
    while True:
        # find which rolls are currently accessible
        _, accessible = get_accessible_rolls(rolls)
        
        if not accessible:
            break
        
        # remove the accessible rolls
        rolls -= accessible
        total_removed += len(accessible)
    
    return total_removed

def get_accessible_rolls(rolls):
    # get all possible directions in a grid
    directions = [
        (-1, 0), (-1, 1), (0, 1), (1, 1),
        (1, 0), (1, -1), (0, -1), (-1, -1)
    ]
    
    accessible = 0
    accessible_positions = set()
    # go through the set of roll positions
    for row, col in rolls:
        neighbour_count = 0
        # go through all the possible directions
        for dr, dc in directions:
            # if there is a neighbour around the roll add it to the count
            if (row + dr, col + dc) in rolls:
                neighbour_count += 1
        
        # if there are fewer than 4 rolls around the roll increment the accessible count
        # and add the coordinates of roll to the positions set
        if neighbour_count < 4:
            accessible += 1
            accessible_positions.add((row, col))
    
    # return number of accessible rolls and accessible rolls positions
    return accessible, accessible_positions

def main():
    grid = get_grid('input.txt')
    rolls = get_roll_positions(grid)
    
    # part 1
    accessible, _ = get_accessible_rolls(rolls)
    print(accessible)
    
    # part 2
    total = get_total_removable_rolls(rolls)
    print(total)
    
if __name__ == "__main__":
    main()