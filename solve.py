#solve RITSEC intro to networking (hard) challenge
#oct 1, 2023
#by cayden Wright
import socket
import re

HOST = "127.0.0.1"
INITIAL_PORT = 2048

def main():
    output=""
    port = INITIAL_PORT
    while(True):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, port))
        output = s.recv(4096).decode()
        if(re.match("RS{.*}", output)):
            print("FOUND FLAG: "+output)
            break
        print(output)
        port = re.findall("\d{5}", output)[0]
        print("going to port: "+port)
        port=int(port)
        s.close()
if __name__=="__main__":
    main()
