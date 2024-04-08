class hand:
    def __init__(self, cards, bids):
        self.hand = cards
        self.bid = int(bids)
        self.rank = 1
        self.hand_type = 0
        self.hand_type_check()

    def compare_value(self, other_hand):
        global cards_dic
        if hands_power[self.hand_type] > hands_power[other_hand.hand_type]:
            self.rank += 1
        elif self.hand_type == other_hand.hand_type:
            pos = 0
            while pos < len(self.hand):
                if cards_dic[self.hand[pos]] > cards_dic[other_hand.hand[pos]]:
                    self.rank+=1
                    return
                elif cards_dic[self.hand[pos]] == cards_dic[other_hand.hand[pos]]:
                    pos+=1
                else:
                    return
        #print(other_hand.hand, self.rank)

    def hand_type_check(self):
        global cards_types
        temp_max = []
        joker_count = 0 # part 2
        for i in range(len(cards_types)):
            temp_max.append(self.hand.count(cards_types[i]))
            joker_count = self.hand.count("J")# part 2



#no jokers
#        match max(temp_max):
#            case 5:
#                self.hand_type = 6
                
#            case 4:
#                self.hand_type = 5
                
#            case 3:
#                temp = 0
#                for j in range(len(cards_types)):
#                    if self.hand.count(cards_types[j]) == 2:
#                        temp = 2
#                if temp == 2:
#                    self.hand_type = 4
#                else:
#                    else:
#                        self.hand_type = 3
                
            #case 2:
            #    if temp_max.count(2) == 2:
            #        self.hand_type = 2
            #    else:
            #        self.hand_type = 1
                
            #case other:
             #   self.hand_type = 0



        #implement jokers
        match (max(temp_max) + joker_count):
            case 5:
                self.hand_type = "Five of a Kind"
                
            case 4:
                self.hand_type = "Four of a Kind"
                
            case 3:
                if (joker_count == 0 and temp_max.count(2) == 1) or (temp_max.count(2) == 2): # if joker >0 and two pairs, then full house, if joker == 0 and 1 pair
                    self.hand_type = "Full House"
                else:
                    self.hand_type = "Three of a Kind"

            case 2:
                if temp_max.count(2) == 2:
                    self.hand_type = "Two Pair"
                else:
                    self.hand_type = "One Pair"
                
            case other:
                self.hand_type = "High Card"        
                     


hands_power = {"Five of a Kind":10, "Four of a Kind":8, "Full House":7, "Three of a Kind":5, 
                "Two Pair":4, "One Pair":3, "High Card":1}
                
cards_types = ["A", "K", "Q",
 #part 2    "J",
     "T", "9", "8", "7", "6", "5", "4", "3", "2"]
list_of_hands = []
f = open("input07.txt", "r")
for line in f:
    list_of_hands.append(hand(line[:5], line[6:]))

'''
cards_dic = {"A":14, "K":13, "Q":12, "J":11, "T":10, "9":9, "8":8, "7":7, "6":6, "5":5,
                "4":4, "3":3, "2":2}

#just store the cards as a list of cards and bids
#and then instance the hand
#directly when creating, append them to the list of hands

results = []
for a in range(len(list_of_hands)):
    for b in list_of_hands:
        list_of_hands[a].compare_value(b)
    results.append(list_of_hands[a].rank * list_of_hands[a].bid)

print(results)
print(max(results))
print(sum(results))
'''
####################^^^    PART 1 ^^^###################################
####################\/\/\/ PART 2 \/\/\/###################################

cards_dic = {"A":14, "K":13, "Q":12, "J":1, "T":10, "9":9, "8":8, "7":7, "6":6, "5":5,
                "4":4, "3":3, "2":2}

results = []
for a in range(len(list_of_hands)):
    if list_of_hands[a].hand.count("J") > 0:
        print(list_of_hands[a].hand_type, list_of_hands[a].hand)
    for b in list_of_hands:
        list_of_hands[a].compare_value(b)
    results.append(list_of_hands[a].rank * list_of_hands[a].bid)

#print(results)
#print(max(results))
print(sum(results))

"""

my_hand_1 = hand("JJ234", 1)
my_hand_2 = hand("J2234", 10)

my_hand_1.compare_value(my_hand_2)
my_hand_2.compare_value(my_hand_1)

print(my_hand_1.rank, my_hand_2. rank)

sum = my_hand_1.bid * my_hand_1.rank + my_hand_2.bid * my_hand_2.rank
print(sum)
"""

#JOKERY STAJĄ SIĘ TYM CO NAJLEPSZE DLA RĘKI
