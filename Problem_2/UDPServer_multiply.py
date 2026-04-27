import socket

def solve():
    serverPort = 12345
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    
    print("UDP Server is ready to receive on port 12345...")
    
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        decodedMsg = message.decode()
        
        #print recieved message
        print(f"Received from {clientAddress}: {decodedMsg}")

        try:
            numStrings = [x.strip() for x in decodedMsg.split(',')]
            nums = [float(x) for x in numStrings if x]
            
            if not nums:
                result = "Invalid input"
            else:
                productValue = 1.0
                for n in nums:
                    productValue *= n
                result = str(productValue)
                
        except ValueError:
            result = "Invalid input"
            
        serverSocket.sendto(result.encode(), clientAddress)

if __name__ == "__main__":
    solve()