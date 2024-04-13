from ntpath import join
import random


list1 = ['A', 'B', 'C', 'D']
list2 = ['a', 'b', 'c', 'd']
list3 = ['*', '+', '?']
list4 = ['1', '2', '3', '4']
passw = []

for i in range(0, len(list1)):
  passw.append(list1[random.randint(0, len(list1)-1)])
  passw.append(list2[random.randint(0, len(list2)-1)])
  passw.append(list3[random.randint(0, len(list3)-1)])
  passw.append(list4[random.randint(0, len(list4)-1)])
  joinpassw = ' '.join(passw)
  print(joinpassw.replace(' ', ''))
  break