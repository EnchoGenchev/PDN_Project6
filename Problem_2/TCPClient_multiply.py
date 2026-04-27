import socket

def main():
    serverIP = '127.0.0.1'
    serverPort = 12345
    
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverIP, serverPort))
    
    userInput = input("Enter a list of comma-separated numbers: ")
    clientSocket.send(userInput.encode())
    
    serverResponse = clientSocket.recv(1024)
    print("From Server:", serverResponse.decode())
    
    clientSocket.close()

if __name__ == "__main__":
    main()