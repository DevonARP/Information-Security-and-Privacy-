#Command to run: python lab4.py
from collections import OrderedDict 

sample_list = [1, 5, 3, 6, 3, 5, 6, 1, 2,7,7,9,0,0,11,-5,-3]

set_list = list(set(sample_list))
set_list.sort()
print("Using sets: " + str(set_list))

loop_list = []
for i in sample_list:
    if i not in loop_list:
        loop_list.append(i)
loop_list.sort()
print("Using a for loop: " + str(loop_list))

dict_list = list(OrderedDict.fromkeys(sample_list)) 
dict_list.sort()
print("Using a dictionary: " + str(dict_list))

comp_list = [] 
[comp_list.append(x) for x in sample_list if x not in comp_list] #Slightly faster than using a for loop due to different appends being used
comp_list.sort()
print("Using list comprehension: " + str(comp_list))

enum_list = [i for n, i in enumerate(sample_list) if i not in sample_list[:n]]
enum_list.sort()
print("Using enumeration: " + str(enum_list))