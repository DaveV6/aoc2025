def get_combinations(filename):
    with open(filename) as file:
        combinations = [line.rstrip() for line in file]
   
    return combinations

def get_joltage(s, nums=12):
    res = []
    start = 0
    
    # go through the number of digits we need
    for i in range(nums):
        # how many digits we still need to pick
        remaining = nums - i
        # the latest position we can pick from
        end = len(s) - remaining + 1
        
        # find the largest digit in the range
        max_digit = '0'
        max_pos = start
        for j in range (start, end):
            if s[j] > max_digit:
                max_digit = s[j]
                max_pos = j
        res.append(max_digit)
        # move start to the next digit
        start = max_pos + 1
    
    return int(''.join(res))
    
def main():
    combinations = get_combinations('input.txt')
    joltage_sum = 0
    nums = 12
    
    for s in combinations:
        joltage = get_joltage(s, nums)
        joltage_sum += joltage
    
    print(joltage_sum)

if __name__ == "__main__":
    main()