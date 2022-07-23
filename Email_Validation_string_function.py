
# Email Validation Using Python (Using String Function)

'''Condition to follow:
1. Minimum characters should be 6
2. Email Should start with Alphabet
3. "@" must be one in email
4. Dot "." must be at 3rd or 4th position from the end
5.  Email should not have space between them and no upper case allowed, special character like ( @ . _) are allowed. 
'''
print("Email Validation Using Python")

email=input("Enter your Email :")  

k,j,d=0,0,0

if len(email)>=6:                                              #1st Condition

    if email[0].isalpha():                                     #2nd Condition
    
        if ("@" in email) and (email.count("@")==1):           #3rd Condition
    
            if (email[-3]==".") ^ (email[-4]=="."):            #4th Condition              
                                                            #Ex-or opertor(^) is used because if any of the conditon is TRUE the answer will be TRUE. 
                                                            #WE are not using OR operator because if both the condition is TRUE then the answer will show TRUE which is Wrong as per our requirement that dot "." should be only in 3rd or 4th position from last
    
                for i in email:                                #5th Condition
    
                    if i==i.isspace(): 
                        k=1
                    elif i.isalpha():
                        if i==i.upper():                       # w--- w==W or W--- W==W
                            j=1
                    elif i.isdigit(): 
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1

                if k==1 or j==1 or d==1:
                    print("Wrong Email 5 ")
                else:
                    print("Right Email")
    
            else:
                print("Wrong Email 4 ")
    
        else:
            print("Wrong Email 3 ")
    
    else:
        print("Wrong Email 2 ")

else:
    print("Wrong Email 1 ")

