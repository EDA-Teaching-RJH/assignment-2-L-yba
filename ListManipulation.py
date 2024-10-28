### Part Three -- your code goes here. 

numbers = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3)

numbers = sorted(numbers)

while 1 in numbers:
  numbers.remove(1)
  
numbers.extend([7, 8])

print("Final list:", numbers)