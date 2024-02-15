
# Day 1
def day_one(filepath):
    results = []
    with open(filepath) as input:
        lines = input.readlines()
        for line in lines:
            print(line)
            chars = list(line)
            first_num = 0
            last_num = 0
            for char in chars:
                if char.isdigit():
                    first_num = char
                    break
            for char in chars[::-1]:
                if char.isdigit():
                    last_num = char
                    break

            results.append(int(str(first_num)+str(last_num)))

    return sum(results)

print(day_one("day1_input.txt"))