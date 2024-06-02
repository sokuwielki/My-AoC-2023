import re


file = open("input12.txt", "r")


# # damaged
# . works
# ? unknown

raw = []

for line in file:
    raw.append(line.strip())

class constelation:
    def __init__(self, length):
        self.length = length


def spring_is_valid(spring):
    #find all the "?"
    documentation = []    
    question_marks = []
    temp = []

    for row in spring:       
        temp.append(row.split())
    


    spring = []

    for i in temp:
        documentation.append(list(map(int, i[1].split(','))))
        spring.append(i[0])
    
    for line in spring:
        question_marks.append([m.start() for m in re.finditer('\?', line)])



    temp_len = []
    length = []

    for a in range(len(spring)):
        temp_len.append(spring[a].split('.'))
    
    for i in temp_len:
        while '' in i:
            i.pop(i.index(''))

    #if there is an object, that consists only of 3 and is of a length that has been described in documentation
    #delete that object, and the number from documentation
    
    pop_from_doc = []
    pop_from_len = []

    for b in range(len(documentation)):
        
        #like, the following until dick should be a separate function

        temp1 = []
        temp2 = []
        for z in range(len(temp_len)):
            for a in range(len(temp_len[z])):    
                if len(temp_len[z][a]) in documentation[b] and all(list(map(lambda a : a == '#', temp_len[z][a]))):
                    
                    documentation[b].pop(temp_len[z][a])
                    temp_len[z][a] = ""
                    # like check up how many full # are there and then delete those from documentation
                    #temp1.append((b, documentation[b].index(len(temp_len[z][a]))))
                    #temp2.append(a)               
            filter("", temp_len[z])

        #dick


        for z in range(len(temp_len)):
            for a in range(len(temp_len[z])): 
                if '?' in temp_len[z][a]:
                    q_pos = (temp_len[z][a].index('?')) 
                    temp_len[z][a][q_pos] = '#'
                    #if temp_len[z][a].fullfils():
                    #number_of_question_marks choose len(documentation[i])-1 * documentation[i][j]! * documentation[i][j+1]! etc until documentation[i][-1]! is hit
                    
                    #start with checking how many valid positions for . are there

temp_len[z][a].split('.')
if len(temp[z][a]) == len(documentation):
    for i in len(temp[z][a]):
        if len(temp[z][a][i]) != documentation[i]:
            for q in range(documentation[i]-len(temp[z][a][i])):
                temp[z][a][i][temp[z][a][i].index('?')] = '#'
        #/\ to chyba kurwa nie zadziała, bo szuka rozwiązania, ale nie wszystkich rozwiązań



#replace ? in the string with either # or .
#the split('.') and if there are as many elements as in doc
#check whether length of those lists is the same as the number in doc
#if so increase res_temp by 1 and multiply with the other because you need combinations

#in the ?? string, find the first ?, change it into #, look whether the string fullfils now the doc[0]
#if yes,
#if no, 

spring_is_valid(raw)
