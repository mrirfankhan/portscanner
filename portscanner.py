import socket
import threading

host="pythonprogramming.net"

def main(port):
    main=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    main.settimeout(0.5)
    try:
        con=main.connect((host,port))
        print("port is opne ",port)
        main.close()
    
    except:
        pass


if __name__=="__main__":
    for i in range(1,100):
        t=threading.Thread(target=main,kwargs={'port':i})
        t.start()
