import socket
import pickle


def fetch_input_panel_out():
    input_floor = input("Enter the floor no. you are at ")
    return int(input_floor)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 50007
s.connect((host, port))
while True:
    panel_in = []
    floor = fetch_input_panel_out()
    data_string = pickle.dumps([floor, 'out'])
    s.send(data_string)

    data = s.recv(4096)
    data_arr = pickle.loads(data)
    if(data_arr[-1]=='out'):
        print('Outside panel register', repr(data_arr))

s.close()