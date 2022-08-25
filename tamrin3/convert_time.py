select = input("select convert unit : \n 1) hour----> Seconds \n 2) Seconds---->hour \n select :")
if select == '1' :
        h_time =int(input("Enter hour  :"))
        m_time =int(input("Enter min   :"))
        s_time =int(input("Enter sec   :"))
        time = print("time :",h_time,":",m_time,":",s_time)
        new_time = ( h_time * 3600 ) + ( m_time * 60 ) +  s_time 
        print("time convert :",new_time,"seconds")
elif select == '2' :
        sec =int(input("Enter sec   :"))
        h_time = sec // 3600
        m_time = (sec % 3600) // 60
        s_time = (sec % 3600) % 60
        print("time convert :",h_time,":",m_time,":",s_time,)
else :
    print("please select from just options")
    
    