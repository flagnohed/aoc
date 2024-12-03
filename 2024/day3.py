def sum_mul(fname):
    # test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    # test2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    lines = []
    with open(fname, 'r') as file:
        lines = file.readlines()
    
    m = "mul("
    enabled = True
    sum = 0
    for line in lines:
        for i in range(len(line)):
            found_m = False

            if line[i:].startswith("do()"):
                enabled = True

            elif line[i:].startswith("don't()"):
                enabled = False

            elif line[i:].startswith(m) and enabled:
                found_m = True
                i += len(m)
                x = ""
                y = ""

                # Get X
                while line[i] != ',':
                    if not line[i].isdigit():
                        found_m = False
                        break
                    x += line[i]
                    i += 1

                # Skip ','
                i += 1

                # Get Y
                while line[i] != ')':
                    if not line[i].isdigit():
                        found_m = False
                        break
                    y += line[i]
                    i += 1

                # If all went well, add it to sum
                if found_m:
                    x = int(x)
                    y = int(y)
                    sum += x * y

    return sum


if __name__ == "__main__":
    print(sum_mul("day3.txt"))