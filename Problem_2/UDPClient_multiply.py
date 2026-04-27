import socket

def main():
    serverIP = '127.0.0.1'
    serverPort = 12345
    
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    messageContent = input("Enter a list of comma-separated numbers: ")
    clientSocket.sendto(messageContent.encode(), (serverIP, serverPort))
    
    serverResponse, serverAddress = clientSocket.recvfrom(2048)
    print("From Server:", serverResponse.decode())
    
    clientSocket.close()

if __name__ == "__main__":
    main()