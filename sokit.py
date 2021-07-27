import socket, ip

api_key = '23c518e4-e589-46da-98cf-3b39102dda6c'
PORT = 5050

PR_ip = socket.gethostbyname(socket.gethostname())
PU_ip = ip.ip.ip_address(self=1 ,api_key=api_key)

def com():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((PU_ip, PORT))
        s.listen()
        conn, addr = s.accept()
    return conn,addr