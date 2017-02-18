from Panel_Manager import generate_panel_out
from Managing_Panels import generate_panel_in
b=generate_panel_in()
a=generate_panel_out()
def union(a, b):
    return list(set(a) | set(b))


#print(union(list_in,list_out))