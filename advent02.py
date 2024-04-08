#part 1
"""games = []

f = open("input02.txt", "r")

for lines in f:
    okay = True
    for x in range(lines.find(":"), len(lines)-5):
        try:
            if int(lines[x]+lines[x+1]) > 12:
                
                if lines[x+3:x+6].find("red") != -1:
                    okay = False
                    break

                elif lines[x+3:x+6].find("gre") != -1:
                    if int(lines[x]+lines[x+1]) > 13:
                        okay = False
                        break

                elif lines[x+3:x+6].find("blu") != -1:
                    if int(lines[x]+lines[x+1]) > 14:
                        okay = False
                        break

        except ValueError:
            pass
    
    if okay == True:
        games.append(int(lines[4:(lines.index(":"))]))

print(games)
print(sum(games))"""

red = 0
blue = 0
green = 0
powers_sum = []
f = open("input02.txt", "r")

for lines in f:

    for x in range(lines.find(":"), len(lines)-5):
        try:
            value = int(lines[x]+lines[x+1])
            if value > 0:
                if lines[x+3:x+6].find("red") != -1:
                    if value > red:
                        red = value

                elif lines[x+3:x+6].find("gre") != -1:
                    if value > green:
                        green = value

                elif lines[x+3:x+6].find("blu") != -1:
                    if value > blue:
                        blue = value
    
        except ValueError:
            pass
    powers_sum.append(red*green*blue)
    red = 0
    green = 0
    blue =0 

print(powers_sum)
print(sum(powers_sum))