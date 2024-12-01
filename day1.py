def get_lists(fname):
    left = []
    right = []
    
    with open(fname, 'r') as file:
        for line in file:
            nums = line.split()
            left += [int(nums[0])]
            right += [int(nums[1])]

    return sorted(left), sorted(right)

def smallest_dist(fname):
    left, right = get_lists(fname)
    total = 0

    for i in range(len(left)):
        total += abs(left[i] - right[i])
    
    return total

def similarity_score(fname):
    left, right = get_lists(fname)
    total = 0

    for i in range(len(left)):
        total += left[i] * right.count(left[i])
    
    return total


if __name__ == "__main__":
    print(smallest_dist("input/day1.txt"))
    print(similarity_score("input/day1.txt"))