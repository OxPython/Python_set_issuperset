'''
Created on Jul 7, 2014

@author: viejoemer

How to test if the element from a set is in other in Python?

¿Cómo comprobar si los elemento de un set estan en otro set en Python?

issuperset(other)
set >= other
Test whether every element in other is in the set.

set > other
Test whether the set is a proper superset of other, that is, 
set >= other and set != other.
'''

#Create a set with values.
s = {0,1,2,3,4,5,6,7,8,9}
print(s)

s2 = {1,2}
print(s2)

#Verify if the item from a set is in other.
r = s.issuperset(s2)
print(r)

#Verify if the item from a set is in other.
r = s2.issuperset(s)
print(r)

#Verify if the item from a set is in other with a if.
if s >= s2:
    print('Verify with a if s >= s2: True')
else:
    print('Verify with a if s >= s2: False')

#Verify if the item from a set is in other with a if.
if s2 >= s:
    print('Verify with a if s2 >= s: True')
else:
    print('Verify with a if s2 >= s: False')
    
#Verify if the item from a set is in other with a if.
if s2 > s:
    print('Verify with a if s2 > s: True')
else:
    print('Verify with a if s2 > s: False')
    
#Verify if the item from a set is in other with a if.
if s > s2:
    print('Verify with a if s > s2: True')
else:
    print('Verify with a if s > s2: False')