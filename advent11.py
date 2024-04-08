class galaxy:
    def __init__(self, coor, name):
        self.name = name
        self.posx = coor[0]
        self.posy = coor[1]
        self.distance = []
        self.is_paired = []
    
    def nearest(self, other):
        if not(other in self.is_paired):
            self.distance.append( abs(self.posx - other.posx) + abs(self.posy - other.posy) )
            self.is_paired.append(other.name)
            

file = open("input11.txt", "r")

raw = []

for line in file:
    raw.append(line.strip())


columns = []
temp = 0
j = 0
columns_update = []


for a in range(len(raw[0])):
    temp_column = ""
    for i in range(len(raw)):
        temp_column = temp_column + raw[i][a]
    
    columns.append(temp_column)




for col in range(len(columns)):
    if all(list(map(lambda a :a==".", columns[col]))):
        columns_update.append(col)# + temp)
        #temp += 1



#for q in range(len(raw[0])):
#    for w in columns_update:
#        raw[q] = raw[q][:w] + "." + raw[q][w:]


galaxies = []
temp = 0

row_update = []

for row in range(len(raw)):
    if all(list(map(lambda a : a == '.', raw[row]))):
        row_update.append(row)# + temp)
        #temp += 1


#the idea: add the millions to the coordinates, instead of creating actual million character long lists



temp_name = 0

for x in range(len(raw)):
    for z in range(len(raw[x])):
        temp_name += 1
        if raw[x][z] == "#":

            galaxies.append(galaxy([z, x], temp_name))


print(galaxies[0].posx)
print(row_update)
print(columns_update)


temp_row = 0
temp_col = 0

for i in range(len(galaxies)):
    
    for row in range(len(row_update)):
        if galaxies[i].posy > row_update[row]:

           temp_row += 1
    
    galaxies[i].posy += temp_row*999999
    temp_row = 0

    for column in range(len(columns_update)):
        if galaxies[i].posx > columns_update[column]:
            temp_col += 1
    galaxies[i].posx += temp_col*999999
    temp_col = 0


for i in range(len(galaxies)):
    for z in range(len(galaxies)-i):
        if galaxies[i] != galaxies[i+z]:
            galaxies[i].nearest(galaxies[i+z])


res = 0

used_temp = []

for g in galaxies:
    res += sum(g.distance)
    #used_temp += g.distance

#for b in raw:
    #print(b)  

print(galaxies[0].posx)
#print(len(galaxies))
print(res)
#        9 222 626 too low
#  298 932 923 702
#1 232 996 989 637 too high

#the updated row values make no desired effect
#because the values in galaxies are made using the original seed
#the plan:
# create the normal ass galaxies
# use the original column and row values
# don't forget that column is responsible for x values
# and rows are for y values
#
# then, if the galaxy pos value is bigger then the value in update columns/row
# increase it's value by index+1 (index of the value in columns/row)
