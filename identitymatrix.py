import numpy as np

identity_mat = np.eye(4) #Diagonal will one and everything will be zero

print(identity_mat)



#now making a mini project

user_input = input("Do you  need identity matrix :-").lower()

if user_input == "yes":
    
    user_input = int(input("Please give a value:-"))
    
    iden_mat = np.eye(user_input)
    
    print(iden_mat)
    
elif user_input == "no":
    
    print("Thank you")
    
    exit()
    
else:
    print("Invalid expression")