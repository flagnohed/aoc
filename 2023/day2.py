MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
LINE_START = "Game "

def sum_id(fname):
    id_sum = 0
    id = 0
    with open(fname, 'r') as file:
        for line in file:
            # Games are 1-indexed
            id += 1
            failed = False
            max_count = {"blue": 14, "green": 13, "red": 12}
            info = line.split(': ')[1]
            game = info.split('; ')
            sets = [x.split(', ') for x in game]
            
            for s in sets:

                for c in s:
                    count, color = c.split()
                    if color[-1] == '\n':
                        color = color[:-1]
                    if int(count) > max_count[color]:
                        failed = True
                        break
            
            if not failed:
                id_sum += id

    return id_sum

def sum_power(fname):
    power_sum = 0
    id = 0
    with open(fname, 'r') as file:
        for line in file:
            id += 1
            info = line.split(': ')[1]
            game = info.split('; ')
            sets = [x.split(', ') for x in game]
            m = {"blue": 0, "green": 0, "red": 0}
            for s in sets:
                for c in s:
                    count, color = c.split()
                    count = int(count)
                    if color[-1] == '\n':
                        color = color[:-1]
                    if count > m[color]:
                        m[color] = count
            power_sum += m["blue"] * m["green"] * m["red"]
    
    return power_sum
            


if __name__ == "__main__":
    print(sum_id("day2.txt"))
    print(sum_power("day2.txt"))