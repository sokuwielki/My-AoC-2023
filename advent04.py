f = open("input04.txt", "r")

winning_numbers = []
possible_numbers = []

for a in f:
    winning_numbers.append(a[10:40])
    if a[-1] == '\n':
        #inputs.append(a[9:-1])
        possible_numbers.append(a[42:-1])
    else:
        possible_numbers.append(a[42:])

winning_numbers_int = []
possible_numbers_int = []

for i in range(len(winning_numbers)):
    temp = ""
    temp_list = []

    for j in range(len(winning_numbers[i])):

        if winning_numbers[i][j].isdigit():
            temp = temp + winning_numbers[i][j]
        elif winning_numbers[i][j] == " " and temp != "":
            temp_list.append(int(temp))
            temp = ""

    winning_numbers_int.append(temp_list)
    temp_list = []
    
    for g in range(len(possible_numbers[i])):
        if possible_numbers[i][g].isdigit():
            temp = temp + possible_numbers[i][g]
            if g == (len(possible_numbers[i])-1):
                temp_list.append(int(temp))
                temp = ""

        elif (possible_numbers[i][g] == " ") and temp != "":
            temp_list.append(int(temp))
            temp = ""
    
    possible_numbers_int.append(temp_list)
    temp_list = []

points = 0
powers_in_order = []

#points

for i in range(len(winning_numbers_int)):
    temp = 0
    for j in winning_numbers_int[i]: 
        if j in possible_numbers_int[i]:
            temp+=1
    powers_in_order.append(temp)

for i in powers_in_order:
    if i > 0:
        points += 2**(i-1)

print(points)

#scratchcards
scratch_cards_copies_index = []
for i in winning_numbers:
    scratch_cards_copies_index.append(1)

result_list = []

#skoro mam jedną kopie jedynki, chcę dodać jeden do liczb od 2 do 8
#w ten sposób mam 2 kopie dwójki, więc chce dodać 2 do liczb od 3 do 12
#w ten sposób mam 4 kopie trójki, więc chce dodać 4 do liczb od 4 do 5

for i in range(len(scratch_cards_copies_index)):
    for j in range(scratch_cards_copies_index[i]):
        for b in range(powers_in_order[i]):
            scratch_cards_copies_index[i+1+b] += 1

print(sum(scratch_cards_copies_index))
print(scratch_cards_copies_index)
