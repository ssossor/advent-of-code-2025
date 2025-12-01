# Part 1

f = [x.strip() for x in open("input_1.txt").readlines()]

count = 0

number = 50

for i in f:

    if i[0] == "L":
        number = (number - int(i[1:])) % 100
    else:
        number = (number + int(i[1:])) % 100

    if number == 0:
        count += 1

print(count)

# Part 2

count = 0

number = 50

for i in f:

    if i[0] == "L":
        next_number = (number - int(i[1:]))
        count += abs((next_number - 1) // 100)

        if number == 0:
            count -= 1

    else:
        next_number = (number + int(i[1:]))
        count += next_number // 100
    
    number = next_number % 100

print(count)