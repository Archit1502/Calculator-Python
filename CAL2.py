# CALCI
print("\t\t\t--------------------------------------------------------------")
print("\t\t\t-------------------    CALCULATOR    -------------------")
print("\t\t\t--------------------------------------------------------------")

# Begin
a='Y'

while  a=="Y":
    print('''(1)ADDITION
(2)SUBSTRACTION
(3)MULTIPLICARION
(4)DIVISION
(5)PERCENTAGE
(6)To the Power
(7)Square Root
(8) ''X'' Under-root
(9)FACTORIAL
(0)EXIT''')
    x=int(input("Choose the Mathematical Operation: "))
    
    if x==1:
        q=int(input("Enter first value : "))
        w=int(input("Enter second value : "))
        print("Sum of the numbers is: ",(q+w))
        print ("-------------------------------------------<<<<<<<<<<<<")
        continue
    
    elif x==2:
        q=int(input("Enter first value : "))
        w=int(input("Enter second value : "))
        print("Substraction of the numbers is: ",(q-w))
        print ("-------------------------------------------<<<<<<<<<<<<")
        continue
    
    elif x==3:
        q=int(input("Enter first value : "))
        w=int(input("Enter second value : "))
        print("Multiplication of the numbers is: ",(q*w))
        print ("-------------------------------------------<<<<<<<<<<<<")
        continue

    elif x==4:
        q=int(input("Enter first value : "))
        w=int(input("Enter second value : "))
        print("Division  of the numbers is: ",(q/w))
        print ("-------------------------------------------<<<<<<<<<<<<")
        continue

    elif x==5:
        q=int(input("Enter value : "))
        w=int(input("What %  is required:  "))
        e =  (w/100)*q
        print( w  ,"% of ", q ,"is : " ,e)
        print ("-------------------------------------------<<<<<<<<<<<<")
        continue

    elif x==6:
        q=int(input("Enter value : "))
        w=int(input( "Race to the power of : "))
        print(q," race to the power ",w," is: ",(q**w))
        print ("-------------------------------------------<<<<<<<<<<<<")
        continue

    elif x==7:
        q=int(input("Enter value : "))
        w= (q**(1/2))
        print("Square root of ",q," is: ", w)
        print ("-------------------------------------------<<<<<<<<<<<<")
        continue
    
    elif x==8:
        q=int(input("Enter value : "))
        w=int(input( "Under Root of degree : "))
        e= (q**(1/w))
        print(w,"th root of ",q," is: ", e)
        print ("-------------------------------------------<<<<<<<<<<<<")
        continue
    
    elif x==9:
        q=int(input("Enter the number : "))
        fact = 1
        if q >= 1 :
            for i in range (1 , (q+1)):
                             fact = fact*i
        print("Factorial of the given number is: ",fact)
        print ("-------------------------------------------<<<<<<<<<<<<")
        continue

    elif x==0:
        print('''\t\t-->>>>>>>>>>----------------- THANK YOU -----------------<<<<<<<<<<--''')
        break

    else:
        print("!!!!!!   Wrong Input - Please select from Given Options only.   !!!!!!")



                
