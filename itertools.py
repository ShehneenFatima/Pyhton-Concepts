#itertools
#itertools module provides powerful iterators for handling large data sets efficiently
#  1 ] itertools.count(start,step)
#creates infinite counter
from itertools import count

for num in count(5,2): #starts at 5 with the increment of 2
    print(num)
    if num >= 15:
       break
#itertools.cycle(iterable)
from itertools import cycle

colours = ["REd" , "Yellow" , "Green"]
cycler=cycle(colours)

for i in range(6):
   print(next(cycler)) #cycles through the list

#itertools.permutations(iterable,r)
#finds all possible ordering of elements

from itertools import permutations

letters = ["w" ,"r" ,"t" , "g"]
print(list(permutations(letters,2))) #2-element permutation

#itertools.combinations(itertools,r)
from itertools import combinations
letters = ["W" ,"l" ,"k"]
print(list(combinations(letters,2)))
  

#Lambda Function(small ,unnamed functions)
square = lambda x: x**2
print(square(77))

#Lambda in sorting
students = [("Shehneen",21), ("Sara",16),("Fahad",21)]
students.sort(key=lambda x:x[1])
print(students)


#Maps(Transform a sequence)
#the map() function,applies a function to every element of an iterable
nums = [1,2,3,4,5]
squared=list(map(lambda x:x**2,nums))
print(squared)


#Filter() [Filters functions based on a condition]
nums = [1,2,3,4,5,6,7,8,9]
evens = list(filter(lambda x:x%2 == 0, nums))
print(evens)
