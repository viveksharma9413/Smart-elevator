import socket
import pickle


def fetch_input_panel_in():
    input_floor = input("press the floor no. button ")
    return int(input_floor)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 50007
s.connect((host, port))
while True:
    panel_in = []
    floor = fetch_input_panel_in()
    data_string = pickle.dumps([floor, 'in'])
    s.send(data_string)
    #print(data_string)

    data = s.recv(4096)
    #print(data)
    data_arr = pickle.loads(data)
    #print(data_arr)
    if(data_arr[-1]=='in'):
        print('Inside panel register', repr(data_arr))

s.close()
