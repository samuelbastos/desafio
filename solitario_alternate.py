# -*- coding: utf-8 -*-
flag = True 

while flag:
    
    chosen = 0
    number_counter_dict = {}
    
    b = raw_input()

    if b == '0':
        break

    a = raw_input().split()

    if int(b) != len(a):
        print("Entradas não dão match")
        continue

    for x in a:

      if number_counter_dict.get( x ) == None:
	number_counter_dict.setdefault( x, 1 )
      else:
	number_counter_dict[ x ] = number_counter_dict[ x ] + 1

    for y in number_counter_dict.keys():
      if number_counter_dict[ y ]%2 == 1:
	chosen = y

    if flag:
        print (chosen)
