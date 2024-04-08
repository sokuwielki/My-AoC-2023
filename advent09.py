#check the difference between every number in the line
#if it's always zero then ignore
#else:
#repeat until they're all zero
#when they're all zero you add a placeholder at the end of every step
#so storing every list is important
#and then you work backwwards to the number
#so if last number is 0, that means the difference between last number and placeholder is 0
#so last number and placeholder are the same
#repeat until initial list is reached and find the next value in the set
#and then sum all the extrapolated values


file = open("input09.txt", "r")

my_values = []

for a in file:
    my_values.append(list(map(int, a.split(" "))))

temp_list = []


def extrapolate(my_values):
    temp = []
    last_values = 0
    for d in range(len(my_values)):
        last_values += my_values[d][-1]
        temp_list = []
        for b in range(len(my_values[d])-1):
            temp_list.append(my_values[d][b+1]-my_values[d][b])
        while False in list(map(lambda c : c==0, temp_list)):
            print(temp_list)
            for e in range(len(temp_list)-1):
                temp_list[e] = temp_list[e+1]-temp_list[e]
            
            last_values += temp_list[-1]
            temp_list.pop(-1)
    print(last_values)


    #temp.append(last_values)


#part 1
#extrapolate(my_values)
#ans 1898776583


#part 2
def extrapolate_r_bad(my_values):

    values_sorted = [[]]
    temp_list_stored =[]
    for d in range(len(my_values)):
        temp_list = []
        
        for b in range(len(my_values[d])-1):
            temp_list.append(my_values[d][b+1]-my_values[d][b])

        
        while False in list(map(lambda c : c==0, temp_list)):
            print(temp_list)
            values_sorted[-1].append(temp_list[0])
        
            for e in range(len(temp_list)-1):
                temp_list[e] = temp_list[e+1]-temp_list[e]
        
            temp_list.pop(-1)
        
        if d != len(my_values)-1:
            values_sorted.append([])

    for h in range(len(values_sorted)):
        temp = 0
        values_sorted[h].reverse()
        temp += my_values[h][0]
        for i in values_sorted[h]:
            temp -= i
        #print(temp)

    last_values = 0
    #print(values_sorted)
    print(temp_list_stored)

    for f in range(len(values_sorted)):
        
        for g in range(len(values_sorted[f])-1):
            values_sorted[f][0] -= values_sorted[f][g+1]
        
        last_values += (my_values[f][0] - values_sorted[f][0])

    print(last_values)

def my_recursion(list_of_lists, count=-1):
    #print(list_of_lists)
    count += 1
    if len(list_of_lists)==count:
        return 0
    else:
        #print(list_of_lists[count][0])
        return list_of_lists[count][0] - my_recursion(list_of_lists, count)
        #return list_of_lists[len(list_of_lists)-count][0] - my_recursion(list_of_lists, count)

def extrapolate_r(my_values):
    initial_values = []
    new_temp = []

    for j in range(len(my_values)):
        initial_values.append(my_values[j][0])
    
    for k in range(len(my_values)):
        temp_list = []

        for l in range(len(my_values[k])-1):
            temp_list.append(my_values[k][l+1]-my_values[k][l])
            #print(temp_list)
        #print(new_temp)
        new_temp += [[]]
        for n in temp_list:
           # print(n)
            new_temp[-1].append(n)
            #print(new_temp)
        
        while False in list(map(lambda c : c==0, temp_list)):
            #print(temp_list)
            for l in range(len(temp_list)-1):
                temp_list[l] = (temp_list[l+1]-temp_list[l])
            temp_list.pop(-1)
            #print(new_temp)
            new_temp += [[]]
            #print(new_temp)
            for n in temp_list:
                new_temp[-1].append(n)
            
        filter(new_temp, [])
        #print(new_temp)


    temp_zip = []
    bound = 0
    for p in range(len(new_temp)):
        if False in list(map(lambda q : q==0, new_temp[p])):
            pass
        else:
           temp_zip.append(new_temp[bound:p])
           bound = p+1
           
    #print(temp_zip)

    #IDEA IS: GET ALL THE ITERATIONS IN A LIST
    #SORT THEM LIST-WISE
    #RUN MY_RECURSION
    #PROFIT

    
    res = 0
    #for o in new_temp:
    for r in range(len(temp_zip)):
        res += initial_values[r] - my_recursion(temp_zip[r])
    print(res)

            

    


#list_of_lists = [[10,13,16,21,30,45],[3,3,5,9,15],[0,2,4,6],[2,2,2]]

#print(my_recursion(list_of_lists))
    #for i in range(len(list_of_lists)):
    #    list_of_lists[i+3][0] - (list_of_lists[i+2][0] - (list_of_lists[i+1][0]- (list_of_lists[i][0] - 0)))


extrapolate_r(my_values)
#ans, 15001 too high
