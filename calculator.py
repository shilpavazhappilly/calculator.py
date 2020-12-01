import math
while True:
    print("\n Choose the math operation\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Modulo\n6. Power\n7. Square Root\n8. Logarithm\n9. Sine\n10. Cosine\n11. Tangent")
    oper = input("\n Your Option From Menu :")
    
    #Addtion
    if oper == "1":
        num1 = float(input("\nEnter your First number:"))
        num2 = float(input("\nEnter your Second number:"))
        print("\nThe sum is :"+str(num1+num2)+"\n")
        back = input("\nGo back to main menu?(y/n)")
        if back == "y":
            continue
        else:
            break
    
    
    #Substraction
    elif oper == "2":
        num1 = float(input("\nEnter your First number:"))
        num2 = float(input("\nEnter your Second number:"))
        print("\nThe difference is :"+str(num1-num2) +"\n")
        back = input("\nGo back to main menu?(y/n)")
        if back == "y":
            continue
        else:
            break
    
    
    #Multiplication
    elif oper == "3":
        num1 = float(input("\nEnter your First number:"))
        num2 = float(input("\nEnter your Second number:"))
        print("\nThe product is :"+str(num1*num2) +"\n")
        back = input("\nGo back to main menu?(y/n)")
        if back == "y":
            continue
        else:
            break
    
    
    #Division
    elif oper == "4":
        num1 = float(input("\nEnter your First number:"))
        num2 = float(input("\nEnter your Second number:"))
        print("\nThe quotient is :"+str(num1/num2) +"\n")
        back = input("\nGo back to main menu?(y/n)")
        if back == "y":
            continue
        else:
            break
    
    
    #Modulo
    elif oper == "5":
        num1 = float(input("\nEnter your First number:"))
        num2 = float(input("\nEnter your Second number:"))
        print("\nThe Modulo is :"+str(num1%num2) +"\n")
        back = input("\nGo back to main menu?(y/n)")
        if back == "y":
            continue
        else:
            break
            
            
    #Power
    elif oper == "6":
        num1 = float(input("\nEnter your Base number:"))
        num2 = float(input("\nEnter your Power number:"))
        print("\nThe result is :"+str(math.pow(num1,num2)) +"\n")
        back = input("\nGo back to main menu?(y/n)")
        if back == "y":
            continue
        else:
            break
   
    
    #Square Root 
    elif oper == "7":
        num1 = float(input("\nEnter your number for extracting square root:"))
        print("\nThe square root is :"+str(math.sqrt(num1)) +"\n")
        back = input("\nGo back to main menu?(y/n)")
        if back == "y":
            continue
        else:
            break
    
    
    #Logarithm
    elif oper == "8":
        num1 = float(input("\nEnter your number for finding logarithm:"))
        print("\nThe  Logarithm is :"+str(math.log(num1,2)) +"\n")
        back = input("\nGo back to main menu?(y/n)")
        if back == "y":
            continue
        else:
            break
   
    
    #Sine
    elif oper == "9":
        num1 = float(input("\nEnter your Degrees for extracting sine:"))
        print("\nThe sine value is :"+str(math.sin(math.radians(num1))) +"\n")
        back = input("\nGo back to main menu?(y/n)")
        if back == "y":
            continue
        else:
            break
    
    #COSINE
    elif oper == "10":
        num1 = float(input("\nEnter your Degrees for extracting cosine:"))
        print("\nThe sine value is :"+str(math.cos(math.radians(num1))) +"\n")
        back = input("\nGo back to main menu?(y/n)")
        if back == "y":
            continue
        else:
            break
    
    #Tangent
    elif oper == "11":
        num1 = float(input("\nEnter your Degrees for extracting Tangent:"))
        print("\nThe sine value is :"+str(math.tan(math.radians(num1))) +"\n")
        back = input("\nGo back to main menu?(y/n)")
        if back == "y":
            continue
        else:
            break
    
    
    #Wrong option
    else:
        print("The input is wrong")
        continue
