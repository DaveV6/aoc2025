def parse_ranges(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()
    
    ranges = []
    for pair in content.split(','):
        start, end = pair.split('-')
        ranges.append((int(start), int(end)))
    
    return ranges

def is_invalid_id(n):
    s = str(n)
    length = len(s)

    # pattern can be maximum half the entire length
    for pattern_length in range(1, length // 2 + 1):
        # pattern must be divided evenly if not go to next pattern
        if length % pattern_length != 0:
            continue
        
        # slice the number and take only the pattern
        pattern = s[:pattern_length]
        
        # calculate how many times the pattern appears in the number
        repetitions = length // pattern_length
        
        # if the pattern * repetitions equals the number we found the invalid id
        if pattern * repetitions == s:
            return True
        
    return False

def count_invalid_ids(ranges):
    invalid_ids = 0

    # take the starting and ending number
    for start, end in ranges:
        # go through each number of this range
        for num in range(start, end + 1):
            if is_invalid_id(num):
                # add the number if its invalid
                invalid_ids += num

    return invalid_ids

def main():
    ranges = parse_ranges('input.txt')
    invalid_ids = count_invalid_ids(ranges)
    print(invalid_ids)

if __name__ == "__main__":
    main()