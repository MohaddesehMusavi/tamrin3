import random
small_number = 0
big_number = 99
count = 0
while True :
    computer_number = random.randint(small_number,big_number)
    print(computer_number,"??")
    answer = (input("true?? \n 1) yes \n 2) no  \n which?"))
    if answer == '1' :
        print("I win :)")
        break
    elif answer == '2' :
       number = (input("number is bigger or smaller ?? \n 1) bigger \n 2) smaller \n which??"))
       if number == '1' :
            small_number = computer_number 
            computer_number = random.randint(small_number+1,big_number-1)
            count += 1
            
       elif number == '2' :
            big_number = computer_number 
            computer_number = random.randint(small_number+1,big_number-1)
            count += 1
       else :
            answer=input("please select just from options.")
            count -=  1
            continue
    else :
        answer=input("please select just from options \n  1) yes     2) no \n ---- " )
        count -=  1
        
   
          
