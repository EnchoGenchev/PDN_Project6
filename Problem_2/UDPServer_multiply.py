from socket import *

def solve():
    serverPort = 12345
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverIP = '127.0.0.1'
    serverPort = 12345
    serverAddress = (serverIP, serverPort)
    serverSocket.bind(serverAddress)
    
    print("server ready to receive on port 12345")
    
    while True:
        messageBytes, clientAddress = serverSocket.recvfrom(2048)
        message = messageBytes.decode()
        
        #print recieved message
        print(f"Received from {clientAddress}: {message}")

        try:
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
                
            
        serverSocket.sendto(result.encode(), clientAddress)

if __name__ == "__main__":
    solve()