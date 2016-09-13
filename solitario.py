# -*- coding: utf-8 -*-
flag = True 

while flag:

    b = input()

    if b == '0':
        break

    a = input().split()
    a = [int(x) for x in a]

    if int(b) != len(a):
        print("Entradas não dão match")
        continue

    a.sort()

    counter = 0
    iterator = 0

    for x in a:

        current = x
        successor = iterator + 1
        counter = counter + 1
        rest = counter % 2

        if successor < len(a):
            if current != a[successor]:
                if rest != 0:
                    chosen = current
                    break

        #se for o último número
        if counter == len(a):
            chosen = current

        iterator = iterator + 1

    if flag:
        print (chosen)
