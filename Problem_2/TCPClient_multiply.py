from socket import *

def main():
    serverIP = '127.0.0.1'
    serverPort = 12345
    serverAddress = (serverIP, serverPort)
    
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(serverAddress)
    
    message = input("Enter a list of comma-separated numbers: ")
    clientSocket.send(message.encode())
    
    modifiedMessageBytes = clientSocket.recv(1024)
    print("From Server:", modifiedMessageBytes.decode())
    
    clientSocket.close()

if __name__ == "__main__":
    main()