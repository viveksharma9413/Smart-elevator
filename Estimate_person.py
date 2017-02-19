import math





def display():
    result =[]
    result.extend(can_accomodate(1000,980))
    if len(result)==1:
        print("Lift full, Can't accomodate more persons")
    else:
        print(result[1],"persons can board the lift")
