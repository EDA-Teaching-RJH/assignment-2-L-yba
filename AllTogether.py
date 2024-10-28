### Part Four -- your code goes here. 

import random
secret_number = [random.randint(1, 100) for _ in range(10)]
print("original list:", secret_number)

x = 0 
while x<len(secret_number):
    if secret_number[x] % 2 == 0:
        secret_number.pop(x)
    else: 
      x += 1 
    print("Remaining odd numbers:", secret_number)
