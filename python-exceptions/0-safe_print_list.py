#!/usr/bin/python3
def safe_print_list(my_list=[1,2,3,4,],x= len(my_list):
    count = 0
    try:
        for i in range(x):
            print(my_list[i] ,end=' ')
            count += 1
    except IndexError:
         pass
     print()
     return count
