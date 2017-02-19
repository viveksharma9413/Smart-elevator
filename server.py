import socket
import pickle
import _thread
import simulator
import time
HOST = socket.gethostname()
PORT = 50007
panel_in = []
panel_out = []
floor_register = []


def simulate_lift():
    print("Can Accommodate : ", simulator.can_accomodate())
    while True:
        time.sleep(0.5)
        if floor_register.__len__() != 0:
            simulator.lift_simulator(floor_register,panel_in,panel_out)


def on_new_client(clientsocket,addr):
    while True:
        data = clientsocket.recv(4096)
        if not data:
            break
        data = pickle.loads(data)
        if data[1] == 'in':
            if data[0] not in panel_in:
                panel_in.append(data[0])
                panel_in.sort()

            panel_in.append('in')
            data_string = pickle.dumps(panel_in)
            panel_in.pop()
            clientsocket.send(data_string)

        elif data[1] == 'out':
            if data[0] not in panel_out:
                panel_out.append(data[0])
                panel_out.sort()
            panel_out.append('out')
            data_string = pickle.dumps(panel_out)
            panel_out.pop()
            clientsocket.send(data_string)
        # print(panel_in)
        # print(panel_out)
        global floor_register
        floor_register=list(set(panel_in) | set(panel_out))
        estimated_time_to_arrive ={}
        if panel_out.__len__()!=0:
            for floor in panel_out:
                estimated_time_to_arrive[floor] = simulator.estimated_time_of_arrival(simulator.CURR_FLOOR,floor_register, floor)
            print(estimated_time_to_arrive)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)
_thread.start_new_thread(simulate_lift, ())

while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    _thread.start_new_thread(on_new_client, (conn,addr))