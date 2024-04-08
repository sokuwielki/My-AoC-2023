import math
# 1 milisecond hold = 1 milimeter per milisecond more speed

# determine, how many ways there are to win each race
# then multiply those numbers together

time = [54, 94, 65, 92]
distance = [302, 1476, 1029, 1404]



def part_1():
    ways = []
    for i in range(len(time)):
        temp = 0
        speed = 0
        for j in range(time[i]):
            if speed * (time[i] - j) > distance[i]:
                temp += 1
            speed += 1
        ways.append(temp)

    print(ways)

#part_1()
#part 2

time = 54946592
distance = 302147610291404


def part_2(time, distance):
    temp = 0
    speed = 0
    #for i in range(1, time):
    #    speed += 1
    #    if speed * (time-i) > distance:
    #        temp += 1
    #print(temp)
    
    for i in range(1, time):
        speed += 1
        if speed * (time-i) > distance:
            print(time - i * 2 + 1)
            return

#part_2(time, distance)
