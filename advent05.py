seeds = [3169137700, 271717609, 3522125441, 23376095, 1233948799, 811833837,
        280549587, 703867355, 166086528, 44766996, 2326968141, 69162222, 2698492851,
        14603069, 2755327667, 348999531, 2600461189, 92332846, 1054656969, 169099767]

temp_converter = []

#seed (i[1]+n) corresponds to (i[0]+n)  
# the destination range start, the source range start, and the range length.

seed_to_soil = """404519244 291909660 232498813
1320269465 1130502191 53088254
3383428636 3839037267 267181273
0 667785713 35892165
1373357719 524408473 98619504
2581158120 2457172776 306553547
80649901 971363049 35482565
2330985014 3113014199 250173106
637018057 1006845614 54766591
1010187739 1061612205 68889986
851189485 132911406 158998254
718278079 0 132911406
1079077725 730171309 241191740
2887711667 2392582028 64590748
3321831622 2330985014 61597014
3650609909 4106218540 188748756
2952302415 3363187305 20241331
368073252 1183590445 36445992
3839358665 3383428636 455608631
35892165 623027977 44757736
2972543746 2763726323 349287876
691784648 703677878 26493431
116132466 1220036437 251940786""".split('\n')

soil_to_fertilizer = """1392321439 1575423106 1147080465
261871322 2722503571 622657242
884528564 768981668 507792875
3152000765 0 514557996
2539401904 3607032135 247383303
2786785207 3854415438 110791886
2897577093 514557996 254423672
3666558761 1276774543 298648563
0 3345160813 261871322""".split('\n')

fertilizer_to_water = """385494683 1437201590 374714893
3894452006 2756513635 124929297
1389571244 1299917000 137284590
3267934068 2881442932 9378230
4140946106 2602492445 154021190
760209576 585965354 629361668
1948388381 1832044460 70164711
170741915 176668131 214752768
3570093835 2531499423 70993022
2647843344 3421511423 399466167
1832044460 3124261283 116343921
3458218517 2890821162 111875318
1721400289 1215327022 84589978
1526855834 391420899 194544455
4019381303 3002696480 121564803
3641086857 4041602147 253365149
2018553092 1902209171 629290252
3047309511 3820977590 220624557
1805990267 170741915 5926216
3277312298 3240605204 180906219""".split('\n')

water_to_light = """3186854896 2955619881 216294813
1320085115 3394507929 25016085
1300936985 1818141535 19148130
3620767971 560782805 39686383
2121550779 2395592136 95582251
3594740149 4260270958 26027822
1138228493 3171914694 34259798
823736132 600469188 55727065
3049715340 2803112532 137139556
0 461804882 98977923
2217133030 1416346841 282474073
1225320767 1742525317 75616218
3481284141 3206174492 113456008
1172488291 656196253 52832476
1980983454 2662545207 140567325
182051501 2121838778 15960124
1788572787 256566375 2332800
881662118 0 256566375
3769058535 899106596 517240245
157917514 3851650114 24133987
564440564 1937530266 107354197
2527210819 4090588051 169682907
1790905587 709028729 190077867
2499607103 3824046398 27603716
1585667080 258899175 202905707
671794761 3419524014 51700770
3403149709 2491174387 62766639
228474519 2044884463 76954315
3660454354 2553941026 108604181
305428834 2137798902 257793234
879463197 3875784101 2198921
2696893726 3471224784 352821614
1345101200 3319630500 74877429
98977923 4031648460 58939591
1541962677 1698820914 43704403
3465916348 2940252088 15367793
1419978629 3909664412 121984048
723495531 1837289665 100240601
563222068 3908445916 1218496
198011625 3877983022 30462894""".split('\n')

light_to_temp = """2138957924 2867100637 394375633
1108145028 3261476270 27971395
2732973434 712143665 259385506
642453123 1589178663 51870752
316125718 164593015 67732689
0 145842404 18750611
1861017768 2758655274 29719920
2130609825 2858752538 8348099
828190830 2187066385 73864838
18750611 0 126160197
144910808 376698573 26842041
383858407 126160197 19682207
2533333557 3337386080 199639877
1507332395 1950588856 215367909
3619117542 3537025957 51848058
1740303803 1763491162 21707209
3793407347 4140330531 154636765
477829952 3588874015 164623171
1722700304 1432603163 17603499
1890737688 493381148 218762517
4255326359 1549537726 39640937
1408001331 1450206662 99331064
2992358940 2260931223 497724051
429891537 3289447665 47938415
3670965600 1641049415 122441747
171752849 232325704 144372869
3504169105 3753497186 114948437
2109500205 2165956765 21109620
4113434597 1290711401 141891762
3490082991 1070535927 14086114
1136116423 3868445623 271884908
757813486 2788375194 70377344
3948044112 1785198371 165390485
694323875 429891537 63489611
1762011012 971529171 99006756
902055668 1084622041 206089360""".split('\n')

temp_to_humid = """480269915 557576190 100117705
2489408207 1585236324 410693151
2900101358 422045351 135530839
666327594 779006907 28457451
1945409298 807464358 543998909
96132998 2440771002 3096292
1295929224 2746460169 2283706
1298212930 2022055443 99310345
3547441134 3503466915 344864128
1659646920 325230280 96815071
4125576596 3928494543 169390700
3035632197 1351463267 233773057
1397523275 2592671813 109157546
1032938960 2748743875 109076238
1756461991 2276586008 92935317
3968917823 4097885243 156658773
595077917 2369521325 71249677
1593864657 3027700045 65782263
850005265 657693895 121313012
1506680821 2505487977 87183836
1186646008 0 109283216
1849397308 3389340328 96011990
3496945571 4254544016 40423280
3898826606 3858403326 70091217
99229290 3189615306 199725022
468834244 1995929475 11435671
3269405254 109283216 215947064
580387620 2007365146 14690297
0 3093482308 96132998
971318277 2443867294 61620683
3892305262 3496945571 6521344
298954312 2857820113 169879932
1142015198 2701829359 44630810
694785045 2121365788 155220220
3537368851 3848331043 10072283""".split('\n')

humid_to_loc = """3490144003 1623866227 218040905
1709610578 1620839197 3027030
105449249 586389428 113279526
1899604338 2167886292 348178199
1712637608 2678624215 186966730
218728775 0 245776251
2472992580 923734334 143670388
2616662968 3670169885 15297294
2247782537 1395629154 225210043
0 480940179 105449249
4113852846 3959729057 159909096
3322784653 1067404722 167359350
923734334 4119638153 175329143
1534964496 2516064491 162559724
2631960262 3496028440 140849733
2862695906 1234764072 97988355
1697524220 3636878173 12086358
2985646048 1332752427 62876727
1099063477 2970241510 435901019
4009202281 2865590945 104650565
2960684261 2142924505 24961787
2772809995 3406142529 89885911
4273761942 3648964531 21205354
3708184908 1841907132 301017373
464505026 245776251 235163928
3048522775 3685467179 274261878""".split('\n')

list_of_all = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temp, temp_to_humid, humid_to_loc]

def convert_strings(string):
    for i in range(len(string)):
        string[i] = string[i].split(" ")

for i in list_of_all:
    convert_strings(i)
#part 1

seeds = [3169137700, 3169137700+271717609]

for map in list_of_all:
    temp_converter = []
    for i in map:
        for seed_number in range(len(seeds)):
            if seed_number not in temp_converter:
                if int(i[1]) <= seeds[seed_number] < (int(i[1]) + int(i[2])):
                    seeds[seed_number] = int(i[0]) + (seeds[seed_number] - int(i[1]))
                    temp_converter.append(seed_number)
                    
print(seeds)
print(min(seeds))       

#part 2

seeds_2 = [[3169137700, 271717609], [3522125441, 23376095], [1233948799, 811833837],
        [280549587, 703867355], [166086528, 44766996], [2326968141, 69162222], [2698492851,
        14603069], [2755327667, 348999531], [2600461189, 92332846], [1054656969, 169099767]]
seeds = []

for i in seeds_2:
    seeds.append([i[0], i[0]+i[1]])

for m in list_of_all:
    for j in range(len(m)):
        for t in range(len(m[j])):
            m[j][t] = int(m[j][t])

'''
for new in seeds_2:
    for a in range(new[0], new[0] + new[1]):
        seeds.append(a)

# Since even doing this optimised approach takes over 11 GB of RAM (seeds is at over 13871937 elements) We just gotta divide it into smaller executable
# zamiast robić wszystkie range'e naraz zrób jeden na raz przez wszystkie mapy 

for map in list_of_all:
    for i in range(len(map)):
        for seed_number in seeds:
            left_within_range = map[i][1] <= seed_number[0]
            right_within_range = map[i][1] + map[i][2] >= seed_number[0] + seed_number[1]
            temp = 0
            if left_within_range:
                
                if right_within_range:  # seed is within the range, so we just transform beggining and the end
                    temp = 2
                    temp_converter.append( [ map[i][0] + seed_number[0] - map[i][1], map[i][0] + seed_number[1] - map[i][1]] )

                if temp != 2:   # only the beggining of the seed is within the range, so we need to create 2 seeds
                    temp_converter.append( [map[i][0] + seed_number[0] - map[i][1], map[i][0] + map[i][2] - 1 ] )   # transformed beggining, the end of the range - 1
                    temp_converter.append( [map[i][0] + map[i][2], seed_number[1]] ) # end of the range, end of the seed

            else:
                if right_within_range:  # only the end of the seed is within the range, so wee need to create two seeds
                    temp = 1
                    temp_converter.append( [map[i][1], map[i][0] + seed_number[1] - seed_number[0] ] )  # beginning of the range, transformed end of the seed
                    temp_converter.append([seed_number[0], map[i][1] - 1]) # beginning of the seed, beggining of the range - 1
                else:
                    if left_within_range > map[i][1] + map[i][2]  or  right_within_range < map[i][1]: # seed is to the right of the range, or seed if to the left of the range
                        temp_converter.append(seed_number)
                        
                    else: # range is within the seed, so need to create 3 new ranges
                        temp_converter.append([seed_number[0], map[i][1] - 1]) #from start of the seed, to the start of the range - 1
                        temp_converter.append([map[i][0], map[i][0] + map[i][2] - 1])#from the start of the range, to the end of the range -1
                        temp_converter.append([map[i][1] + map[i][2], seed_number[1]])# from the end of the range, to the end of the seed
                                
  #  seeds = temp_converter
  #  print(len(seeds))
   # temp_converter = []
'''#list_of_all = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temp, temp_to_humid, humid_to_loc]
seed_number = 0
#for seed_number in range(len(seeds)):
state = ""
my_dic = {"soil":0, "fert":1, "water":2, "light":3, "temp":4, "humid":5, "loc":6}
my_dic_r = ["soil", "fert", "water", "light", "temp", "humid", "loc"]

while seed_number < len(seeds)-1:
    for map in list_of_all:
        if seed_number == len(seeds)-1:
            break
        if map == list_of_all[0]:
            state = "soil"
        elif map == list_of_all[1]:
            state = "fert"
        elif map == list_of_all[2]:
            state = "water"
        elif map == list_of_all[3]:
            state = "light"
        elif map == list_of_all[4]:
            state = "temp"
        elif map == list_of_all[5]:
            state = "humid"
        elif map == list_of_all[6]:
            state = "loc"

        for i in range(len(map)):
            left_within_range = map[i][1] <= seeds[seed_number][0]
            right_within_range = map[i][1] + map[i][2] >= seeds[seed_number][0] + seeds[seed_number][1]
            temp = 0
            if left_within_range:
                
                if right_within_range:  # seed is within the range, so we just transform beggining and the end
                    temp = 2
                    seeds[seed_number][0] =  map[i][0] + seeds[seed_number][0] - map[i][1]
                    seeds[seed_number][1] =  map[i][0] + seeds[seed_number][1] - map[i][1]
                    seed_number +=1
                    break
                
                if temp != 2:   # only the beggining of the seed is within the range, so we need to create 2 seeds
                    seeds[seed_number][0] = map[i][0] + seeds[seed_number][0] - map[i][1]
                    temp_converter.append([map[i][0] + map[i][2], seeds[seed_number][1], state])
                    seeds[seed_number][1] = map[i][0] + map[i][2] - 1
                    seed_number +=1
                    break
                    # transformed beggining, the end of the range - 1
                    # end of the range, end of the seed

            else:
                if right_within_range:  # only the end of the seed is within the range, so wee need to create two seeds
                    temp = 1
                    temp_converter.append([seeds[seed_number][0], map[i][1] - 1, state]) # beginning of the seed, beggining of the range - 1
                    seeds[seed_number][0] =  map[i][0]
                    seeds[seed_number][1] =  map[i][0] + seeds[seed_number][1] - seeds[seed_number][0]
                    seed_number +=1
                    break
                    # beginning of the range, transformed end of the seed

                else:
                    if left_within_range > map[i][1] + map[i][2]  or  right_within_range < map[i][1]: # seed is to the right of the range, or seed if to the left of the range
                        seed_number +=1
                        break
                        
                    else: # range is within the seed, so need to create 3 new ranges
                        temp_converter.append([seeds[seed_number][0], map[i][1] - 1, state]) #from start of the seed, to the start of the range - 1
                        temp_converter.append([map[i][1] + map[i][2], seeds[seed_number][1], state])# from the end of the range, to the end of the seed
                        
                        seeds[seed_number][0] =  map[i][0]
                        seeds[seed_number][1] =  map[i][0] + map[i][2] - 1
                        seed_number +=1
                        break
    
    state = ""

temp_seeds = seeds
seeds = temp_converter

seed_number = 0

new_seeds = []

for b in seeds:
    if b[2] != "loc":
        new_seeds.append(b)

seeds = new_seeds


while seed_number < len(seeds)-1:
    if seed_number == len(seeds):
            break
    for map in list_of_all[my_dic[seeds[seed_number][2]]+1:]:
        for i in range(len(map)):
            left_within_range = map[i][1] <= seeds[seed_number][0]
            right_within_range = map[i][1] + map[i][2] >= seeds[seed_number][0] + seeds[seed_number][1]
            temp = 0
            if left_within_range:
                
                if right_within_range:  # seed is within the range, so we just transform beggining and the end
                    temp = 2
                    seeds[seed_number][0] =  map[i][0] + seeds[seed_number][0] - map[i][1]
                    seeds[seed_number][1] =  map[i][0] + seeds[seed_number][1] - map[i][1]
                    seeds[seed_number][2] = my_dic_r[my_dic[seeds[seed_number][2]] + 1]
                    seed_number +=1
                    break
                
                if temp != 2:   # only the beggining of the seed is within the range, so we need to create 2 seeds
                    seeds[seed_number][0] = map[i][0] + seeds[seed_number][0] - map[i][1]
                    seeds.append([map[i][0] + map[i][2], seeds[seed_number][1], my_dic_r[my_dic[seeds[seed_number][2]] + 1]])
                    seeds[seed_number][1] = map[i][0] + map[i][2] - 1
                    seeds[seed_number][2] = my_dic_r[my_dic[seeds[seed_number][2]] + 1]
                    seed_number +=1
                    break
                    # transformed beggining, the end of the range - 1
                    # end of the range, end of the seed

            else:
                if right_within_range:  # only the end of the seed is within the range, so wee need to create two seeds
                    temp = 1
                    seeds.append([seeds[seed_number][0], map[i][1] - 1, my_dic_r[my_dic[seeds[seed_number][2]] + 1]]) # beginning of the seed, beggining of the range - 1
                    seeds[seed_number][0] =  map[i][0]
                    seeds[seed_number][1] =  map[i][0] + seeds[seed_number][1] - seeds[seed_number][0]
                    seeds[seed_number][2] = my_dic_r[my_dic[seeds[seed_number][2]] + 1]
                    seed_number +=1
                    break
                    # beginning of the range, transformed end of the seed

                else:
                    if left_within_range > map[i][1] + map[i][2]  or  right_within_range < map[i][1]: # seed is to the right of the range, or seed if to the left of the range
                        seeds[seed_number][2] = my_dic_r[my_dic[seeds[seed_number][2]] + 1]
                        seed_number +=1
                        break
                        
                    else: # range is within the seed, so need to create 3 new ranges
                        seeds.append([seeds[seed_number][0], map[i][1] - 1, my_dic_r[my_dic[seeds[seed_number][2]] + 1]]) #from start of the seed, to the start of the range - 1
                        seeds.append([map[i][1] + map[i][2], seeds[seed_number][1], my_dic_r[my_dic[seeds[seed_number][2]] + 1]])# from the end of the range, to the end of the seed
                        seeds[seed_number][2] = my_dic_r[my_dic[seeds[seed_number][2]] + 1]
                        seeds[seed_number][0] =  map[i][0]
                        seeds[seed_number][1] =  map[i][0] + map[i][2] - 1
                        seed_number +=1
                        break

seeds = temp_seeds + seeds

print(seeds)
result = []
for a in seeds:
    result.append(a[0])
        
print(min(result))