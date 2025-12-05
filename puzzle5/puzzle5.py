def parse_input(filename):
    with open(filename) as f:
        content = f.read()
    
    parts = content.strip().split('\n\n')
    
    ranges = []
    for line in parts[0].strip().split('\n'):
        start, end = line.split('-')
        ranges.append((int(start), int(end)))
    
    ids = [int(line) for line in parts[1].strip().split('\n')]
    
    return ranges, ids

def merge_ranges(ranges):
    # merge overlapping ranges
    merged = [ranges[0]]
    for start, end in ranges[1:]:
        # get the last range from merged list
        last_start, last_end = merged[-1]
        
        # if overlapping extend the last range to cover both
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        # not overlapping add as a separate range
        else:
            merged.append((start, end))
    
    return merged

def main():
    ranges, ids = parse_input('input.txt')
    
    sorted_ranges = sorted(ranges)
    merged = merge_ranges(sorted_ranges)
    
    fresh_ids = 0
    for start, end in merged:
        fresh_ids += end - start + 1
    
    print(fresh_ids)
        

if __name__ == "__main__":
    main()