import math


def can_accomodate(overloaded_limit,current_weight):
    additional_persons=math.floor((overloaded_limit-current_weight)/65);
    if additional_persons == 0 :
        return [False]
    else:
        return [True,additional_persons]


def display():
    result =[]
    result.extend(can_accomodate(1000,980))
    if len(result)==1:
        print("Lift full, Can't accomodate more persons")
    else:
        print(result[1],"persons can board the lift")
