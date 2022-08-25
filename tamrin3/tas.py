import random
sum = 0
count = 1
number = random.randint(1,6)
print("number--->",number)
sum += number
while number != 6 :
    number = random.randint(1,6)
    print("number",count,":",number)
    count += 1
    sum += number
    continue
print("sum :",sum)
    

