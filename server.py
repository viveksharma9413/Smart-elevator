import socket
import pickle
import _thread

HOST = socket.gethostname()
PORT = 50007
panel_in = []
panel_out = []
floor_register = []

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
        print(panel_in)
        print(panel_out)
        floor_register=list(set(panel_in) | set(panel_out))
        print(floor_register)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)
while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    _thread.start_new_thread(on_new_client,(conn,addr))

    print(panel_in)
    print(panel_out)
