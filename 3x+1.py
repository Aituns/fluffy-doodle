def devide_by_three_add_one(n):
    return 3*n+1

def devide_by_two(n):
    return n/2

#values = int(input("Input highest range: "))
number = 1
i = 0
#for i in range(values):
while True:
    number = i + 1
    steps = 0
    ognum = number

    while (number != 1):
        if (number % 2) == 0:
            number = devide_by_two(number)
            steps += 1
        else:
            number = devide_by_three_add_one(number)
            steps += 1

    print(str(ognum) + " has reached oneness in " + str(steps) + " steps")
    i += 1
