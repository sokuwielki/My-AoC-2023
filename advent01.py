def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
        
def read_double_digit(string):
    double_digit = 0
    digits = []
    alphabet = ['o', 'n', 'f', 's', 't', 'e']
    list_of_numbers_spelled = ["nine", "eight", "seven", "six", "five", "four", "three", "two", "one"]
    #w sumie part 1
    for i in range(len(string)):
        if is_integer(string[i]):
            digits.append(int(string[i]))
#tutaj part 2
        elif string[i] in alphabet:
            for word in list_of_numbers_spelled:
                #to +5 ważne wchuj
                if string.find(word, i, i+5) != -1:
                    if string[i] == word[0]: #bez tego to kurwa przy literce f łapie np. two więc gshhvf5twodqgdseven8fourfoursix to 26 zamiast 56
                        digits.append(9-list_of_numbers_spelled.index(word))
                        break
#ustawianie poprawnie liczb
    double_digit = digits[0] * 10
    double_digit += digits[-1]
    return double_digit

my_answer = 0
f = open("input01.txt", "r")
for lines in f:
    my_answer += read_double_digit(lines)

print(my_answer)