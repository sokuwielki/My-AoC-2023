import math

class node:
    def __init__(self, name, lnode, rnode):
        self.name  = name
        self.lnode = lnode
        self.rnode = rnode

    def next_node(self, direction):
        if direction == "R":
            return self.rnode
        else:
            return self.lnode

    def ends_with_Z(self):
        return self.name[-1] == "Z"
    
    def __str__(self):
        return f"Name:{self.name}, L:{self.lnode}, R:{self.rnode}"

file = open("input08.txt", "r")

raw = []

for i in file:
    raw.append(i)

instruction_count = 0
instructions = raw[0].strip('\n')

documents = raw[2:]
documents.sort()
for i in range(len(documents)):
    documents[i] = documents[i].strip('\n')

list_of_nodes = []

for i in documents:
    list_of_nodes.append(node(i[:3], i[7:10], i[12:15]))

def step_counter(nodes, instructions):
    count = 0
    steps = 0
    current_index = 0
    
    while nodes[current_index].name != "ZZZ":

        steps += 1
        current = nodes[current_index].next_node(instructions[count])
        
        count += 1
        if count == len(instructions):
            count = 0

        for j in nodes:
            if j.name == current:
                current_index = nodes.index(j)
    
    print(steps) #14406 too low

#step_counter(list_of_nodes, instructions)

#part 2 
#start at the same time at all the nodes ending with A
#stop when all those nodes end at a node ending with Z


def step_counter_2_brute_force(nodes, instructions):
    count = 0
    steps = 0

    starting = []

    #find all the nodes ending with 'A'
    for a in nodes:
        if a.name[-1] == "A":
            starting.append(a)

    while False in list(map(node.ends_with_Z, starting)):
        #print(list(map(node.ends_with_Z, starting)))    the idea is to use maths and find the smallest common multiple
        for i in range(len(starting)):
            current = starting[i].next_node(instructions[count])
            
            for j in nodes:
                if j.name == current:
                    current_index = nodes.index(j)
            
            starting[i] = nodes[current_index]

        steps += 1
        count += 1
        if count == len(instructions):
            count = 0
    print(steps) #14406 too low
    
    
def step_counter_2(nodes, instructions):
    count = 0
    steps = 0

    starting = []

    #find all the nodes ending with 'A'
    for a in nodes:
        if a.name[-1] == "A":
            starting.append(a)
    
    z_values = list(map(node.ends_with_Z, starting))
    
    them_values = []

        

    while False in z_values:
        #print(list(map(node.ends_with_Z, starting)))    the idea is to use maths and find the smallest common multiple
        steps += 1
        for i in range(len(starting)):
            current = starting[i].next_node(instructions[count])
            
            for j in nodes:
                if j.name == current:
                    current_index = nodes.index(j)
            
            starting[i] = nodes[current_index]

        count += 1
        if count == len(instructions):
            count = 0
    
        z_values = list(map(node.ends_with_Z, starting))

        if True in z_values:
            #z_values = list(filter(True, z_values))
            them_values.append(steps)

            for i in range(len(starting)):
                if z_values[i] == True:
                    starting.pop(i)

    
    
    print(z_values)
    print(starting)
    print(steps)
    print(them_values)
    
    return them_values

#print(list_of_nodes[0])
#penis = list(map(node.ends_with_Z, list_of_nodes))
#print(penis)
def my_lcm(nums):
    my_max = 0 
    my_max += nums[0]

    a = False
    temp = 0

    while a == False:
        for b in nums[1:]:
            if (my_max % b == 0):
                temp += 1
        if temp == (len(nums)-1):
            a = True
        else:
            temp = 0
            my_max += nums[0]

    print(my_max)
    

print(math.lcm(*step_counter_2(list_of_nodes, instructions)))
#3281928401395895474160 too much

#regular expression
#data structures\
#functional programming
#algorithmic optimisation