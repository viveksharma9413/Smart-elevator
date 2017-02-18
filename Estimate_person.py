import math
def can_accomodate(overloaded_limit,current_weight):
    additional_persons=math.floor((overloaded_limit-current_weight)/65);
    if additional_persons == 0 :
        return False,additional_persons# print("Lift is full")
    else:
        return True,additional_persons# print("Current capacity ="+additional_persons)


