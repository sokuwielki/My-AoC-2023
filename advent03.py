'''temp_string = []
special_list = ["@", "#", "$", "%", "^", "&", "*", "/", "+", "-", "="]
temp_int = []
temp = ""
iteration = 0

f = open("input03.txt", "r")

length_file = 0
for lines in f:
    if length_file == 0:
        temp_string.append("." + lines[:-1] + ".")
    temp_string.append("." + lines[:-1] + ".")
    length_file +=1

temp_string.append(temp_string[-1])

row_count = 1
for row in temp_string[1:len(temp_string)-1]:
    i=1
    while (i<len(row)):
        temp = ""
        area = ""
        iteration = 0
        if row[i].isdigit():
            temp = temp + row[i]
            area = row[i-1] + temp_string[row_count-1][i-1:i+2] + temp_string[row_count+1][i-1:i+2]

            if row[i+1].isdigit():
                iteration = 1
                temp = temp + row[i+1]

                if row[i+2].isdigit():
                    iteration = 2
                    temp = temp + row[i+2]
                    area = area + row[i+3] + temp_string[row_count-1][i+2:i+4] + temp_string[row_count+1][i+2:i+4]

                else:
                    area = area + row[i+2] + temp_string[row_count-1][i+2] + temp_string[row_count+1][i+2]

            else:
                area = area + row[i+1] + temp_string[row_count-1][i+1] + temp_string[row_count+1][i+1]

        i+=1
        i+=iteration
        if temp != "":
            if row_count == 1:
                print(temp, area)
            temp_int.append((temp, area))
            #print(temp_int[-1])
    row_count+=1

result = 0
result_list = []
for x in temp_int:
    for j in x[1]:
        if j in special_list:
            result_list.append(int(x[0]))
            result+=int(x[0])
print(result_list)
print(result)'''

temp_string = []
special_list = ["@", "#", "$", "%", "^", "&", "*", "/", "+", "-", "="]
temp_int = []
temp = ""
iteration = 0
temp_1 = ""
temp_2 = ""
temp_bool = True

gears = []

f = open("input03.txt", "r")

length_file = 0
for lines in f:
    if length_file == 0:
        temp_string.append("." + lines[:-1] + ".")
    temp_string.append("." + lines[:-1] + ".")
    length_file +=1

temp_string.append(temp_string[-1])

row_count = 1
for row in temp_string[1:len(temp_string)-1]:
    i=1
    while (i<len(row)):
        temp_bool = True
        temp = ""
        temp_1 = ""
        temp_2 = ""
        area = ""
        iteration = 0
        if row[i] == "*":
            temp = temp + temp_string[row_count-1][i-3:i+4]
            temp_1 = temp_1 + row[i-3:i+4]
            temp_2 = temp_2 + temp_string[row_count+1][i-3:i+4]
            temp_tuple = [temp, temp_1, temp_2]
            print(temp_tuple)
            #UPPER LINE
            if temp_tuple[0][2] == ".":
                temp_tuple[0] = "..." + temp_tuple[0][3:]

            if temp_tuple[0][4] == ".":
                temp_tuple[0] = temp_tuple[0][:5] + ".."

            #MIDDLE
            if temp_tuple[1][2] == ".":
                temp_tuple[1] = "..." + temp_tuple[1][3:]

            if temp_tuple[1][4] == ".":
                temp_tuple[1] = temp_tuple[1][:5] + ".."

            #LOWER LINE
            if temp_tuple[2][2] == ".":
                temp_tuple[2] = "..." + temp_tuple[2][3:]

            if temp_tuple[2][4] == ".":
                temp_tuple[2] = temp_tuple[2][:5] + ".."

            #if star alone
            if temp_tuple[0][2:5] == "..." and (temp_tuple[2][2] == "." or temp_tuple[2][2] == "."):
                if temp_tuple[1][2] == "." or temp_tuple[1][4] ==".":
                    temp_bool = False




            if temp_bool:
                gears.append(temp_tuple)   

            print(gears[-1])


        i+=1
        i+=iteration

    row_count+=1

#print(gears)

results = []
first_gear  = 0
second_gear = 0
#print(gears[7])
for i in range(len(gears)):
    first_gear  = 0
    second_gear = 0
    
    for j in range(len(gears[0])):
        #first gear
        while (not(gears[i][j][-1].isdigit()) and gears[i][j] != "."):
            gears[i][j] = gears[i][j][:len(gears[i][j])-1]
        if len(gears[i][j]) > 3:
            gears[i][j] = gears[i][j][1:]


        while not(gears[i][j][0].isdigit()) and gears[i][j] != ".":
            gears[i][j] = gears[i][j][1:]

        if  gears[i][j] != ".":
            try:
                if gears[i][j][3] == ".":
                    first_gear = int(gears[i][j][:3])
                    second_gear = int(gears[i][j][4:])
            except IndexError:
                if first_gear == 0:
                    first_gear = int(gears[i][j])
                else:
                    second_gear = int(gears[i][j])
    if second_gear == 0:
        
        for j in range(3):
            if len(gears[i][j]) > 3:
                for g in range(len(gears[i][j])):
                    if not(gears[i][j][g].isdigit()):
                        results.append(int(gears[i][j][:g]) * int(gears[i][j][g+1:]))

    results.append(first_gear * second_gear)
    print(gears[i])
    

print(sum(results))

