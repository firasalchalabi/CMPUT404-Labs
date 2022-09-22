#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process

#importing from client.py
from client import create_tcp_socket, get_remote_ip, send_data

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def recieve_and_forward_data(listening_connection, sending_socket):
    payload = b""
    while True:
        data = listening_connection.recv(BUFFER_SIZE)
        if not data:
             break
        payload += data
    sending_socket.sendall(payload)
    sending_socket.shutdown(socket.SHUT_WR)

    full_data = b""
    while True:
        data = sending_socket.recv(BUFFER_SIZE)
        if not data:
             break
        full_data += data
    time.sleep(0.5)
    listening_connection.sendall(full_data)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listening_socket:

        #QUESTION 3
        listening_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        #bind socket to address
        listening_socket.bind((HOST, PORT))
        #set to listening mode
        listening_socket.listen(2)

        remote_host = 'www.google.com'
        remote_port = 80
        remote_ip = get_remote_ip(remote_host)

        #continuously listen for connections
        while True:
            conn, addr = listening_socket.accept()
            print("Connected by", addr)

            sending_socket = create_tcp_socket()
            sending_socket.connect((remote_host, remote_port))
            try:
                p = Process(target=recieve_and_forward_data, args=(conn, sending_socket))
                p.daemon = True
                p.start()
            except Exception as e:
                print(e)
            finally:
                sending_socket.close()

            conn.close()
            
if __name__ == "__main__":
    main()
