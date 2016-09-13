# -*- coding: utf-8 -*-

def mergeSort(alist):

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

flag = True 

while flag:

    b = input("Defina o tamanho do vetor: ")

    if b == '0':
        break

    a = input("Digite o vetor: ").split()

    if int(b) != len(a):
        print("Entradas não dão match")
        continue

    mergeSort(a)

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