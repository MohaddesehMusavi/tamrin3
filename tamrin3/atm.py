password = 3025
reverse_password = 5203
count = 1

while count <= 3 :
    Number = int(input("Enter your password just 3 time:"))
    number = Number
    digit = number / 1000
    if 1 <= digit < 10 :
        if number == password :
            print("your wellcome")
            break
        elif number == reverse_password :
            print("we called by Police")
            break
        else :
            print("try again ")
            count += 1
            
            
    else :
        print("password just be 4 digit ")

if count == 4 :
    print("your account is locked")



           
           
        

   



   

