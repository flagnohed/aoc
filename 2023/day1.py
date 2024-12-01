def calibration_sum(fname):
    total = 0
    with open(fname, 'r') as file:
        digits = []
        for line in file:
            digits = [c for c in line if c.isdigit()]
            total += int(digits[0] + digits[-1])
    
    return total

def calibration_sum_2(fname):
    total = 0
    spelled_out = {"one": '1', "two": '2', "three": '3', "four": '4',
                   "five": '5', "six": '6', "seven" : '7',
                   "eight": '8', "nine": '9'}
    with open(fname, 'r') as file:
        for line in file:
            digits = []
            for i in range(len(line)):
                if line[i].isdigit():
                    digits += [line[i]]
                else:
                    for num in spelled_out.keys():
                        if line[i:].startswith(num):
                            digits += [spelled_out[num]]
                            i += len(num)
                            break
            total += int(digits[0] + digits[-1])
    
    return total


if __name__ == "__main__":
    print(calibration_sum("day1.txt"))
    print(calibration_sum_2("day1.txt"))