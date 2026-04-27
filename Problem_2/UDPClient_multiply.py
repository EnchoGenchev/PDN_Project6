from socket import *

def main():
    serverIP = '127.0.0.1'
    serverPort = 12345
    
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    
    message = input("Enter a list of comma-separated numbers: ")
    messageBytes = message.encode()
    clientSocket.sendto(messageBytes, (serverIP, serverPort))
    
    modifiedMessageBytes, serverAddress = clientSocket.recvfrom(2048)
    print("From Server:", modifiedMessageBytes.decode())
    
    clientSocket.close()

if __name__ == "__main__":
    main()