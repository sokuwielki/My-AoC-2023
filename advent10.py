temp = []
f = open("input10.txt", "r")
for lines in f:
    temp.append(lines.strip('\n'))


for i in temp:
    if "S" in i:
        start_point = [temp.index(i), i.index("S")]

search_pos = []

step_count = 0
vertices = ["L", "J", "7", "F"]

def connects(char):
    match char:
        case "|":
            return "NS"
        case "-":
            return "EW"
        case "L":
            return "NE"
        case "J":
            return "NW"
        case "7":
            return "SW"
        case "F":
            return "SE"
        case ".":
            return ""
        case "S":
            return "X"

def opposite(char):
    match char:
        case "N":
            return "S"
        case "S":
            return "N"
        case "E":
            return "W"
        case "W":
            return "E"

#determine where it connects to "S"

if "S" in connects(temp[start_point[0]-1][start_point[1]]):
    search_pos.append("S")
    
    if "N" in connects(temp[start_point[0]+1][start_point[1]]):
        search_pos.append("N")

    elif "E" in connects(temp[start_point[0]][start_point[1]+1]):
        search_pos.append("E")

    else: #"W"
        search_pos.append("W")

elif "N" in connects(temp[start_point[0]+1][start_point[1]]):
    search_pos.append("N")

    if "E" in connects(temp[start_point[0]][start_point[1]+1]):
        search_pos.append("E")

    else: #"W"
        search_pos.append("W")

elif "W" in connects(temp[start_point[0]][start_point[1]-1]):
    search_pos.append("W")

    if "E" in connects(temp[start_point[0]][start_point[1]+1]):
        search_pos.append("E")

    elif "S" in connects(temp[start_point[0]+1][start_point[1]]):
        search_pos.append("S")

    else: #"N"
        search_pos.append("N")

#print(search_pos)

#save previous pos, check according to the instructions where to go

current_dir = [search_pos[0], search_pos[0]]

cur_pos = []

cur_pos += start_point

#prev_pos_a = current_pos.strip(prev_pos_a)

directions={"N":[-1, 0], "S":[1,0], "E":[0,1], "W":[0,-1]}

cur_pos[0] += directions[current_dir[0]][0]
cur_pos[1] += directions[current_dir[0]][1]
#print(directions[current_dir[0]][0])
#print(start_point, cur_pos)

vertex = []

while cur_pos != start_point:
    step_count +=1

    next_pos = connects(temp[cur_pos[0]][cur_pos[1]])
    next_pos = next_pos.strip(opposite(current_dir[0]))

    if temp[cur_pos[0]][cur_pos[1]] in vertices:
        vertex.append(list(cur_pos))
        #print(vertex[-1])
        #print(cur_pos)


    current_dir[1] = current_dir[0]
    current_dir[0] = next_pos
    cur_pos[0] += directions[current_dir[0]][0]
    cur_pos[1] += directions[current_dir[0]][1]
    #print(vertex)
    #print(cur_pos)

print(step_count)
print(step_count/2) #round up
#print(vertex)

#PART 2, FIND TILES, THE SYMBOLS, WITHIN THE LOOP
tile_count = 0

def polygon_area(vertices):
    n = len(vertices)
    area = 0

    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]

    area = abs(area) / 2
    return area

# Example usage
polygon_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
print("Area of the polygon:", polygon_area(vertex))
print(polygon_area(vertex) - step_count/2) # round up

    

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""