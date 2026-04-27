from socket import *

def solve():
    serverIP = '127.0.0.1'
    serverPort = 12345
    serverAddress = (serverIP, serverPort)
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(serverAddress)
    serverSocket.listen(1)
    
    print("server is ready to receive on port 12345")
    
    while True:
        connectionSocket, clientAddress = serverSocket.accept()
        clientIP, clientPort = clientAddress

        #try catch since some invalid inputs mess up numstrings
        try:
            message = connectionSocket.recv(1024).decode()
            if not message:
                continue

            #print recieved message
            print(f"message from {clientIP}:{clientPort} = {message}")
            
            numStrings = [x.strip() for x in message.split(',')]
            nums = [float(x) for x in numStrings if x]
            
            if not nums:
                result = "Invalid input"
            else:
                product = 1.0
                for n in nums:
                    product *= n
                result = str(product)
                
        except ValueError:
            result = "Invalid input"
            
        connectionSocket.send(result.encode())
        connectionSocket.close()

if __name__ == "__main__":
    solve()