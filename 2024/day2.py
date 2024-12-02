def check_safe(levels):
    increasing = levels[0] < levels[1]
    for i in range(len(levels) - 1):
        if levels[i] == levels[i + 1]:
            return False
        if increasing and levels[i] > levels[i + 1]:
            return False
        if not increasing and levels[i] < levels[i + 1]:
            return False
        diff = abs(levels[i] - levels[i + 1])
        if diff > 3 or diff < 1:
            return False
    return True


def num_safe_reports(fname):
    count = 0
    with open(fname, 'r') as file:
        for report in file:
            levels = [int(c) for c in report.split()]

            if check_safe(levels):
                count += 1
            else:
                # Try to remove one level at a time, see
                # if it would make the report safe.
                for i in range(len(levels)):
                    rest = levels[:i] + levels[i + 1:]
                    if check_safe(rest):
                        count += 1
                        break

    return count


if __name__ == "__main__":
    print(num_safe_reports("day2.txt"))
