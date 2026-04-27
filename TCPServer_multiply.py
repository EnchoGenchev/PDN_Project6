import socket

def solve():
    serverPort = 12345
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    
    print("TCP Server is ready to receive on port 12345...")
    
    while True:
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024).decode()
            if not message:
                continue
            
            numStrings = [x.strip() for x in message.split(',')]
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
        except Exception as e:
            result = f"Error: {str(e)}"
            
        connectionSocket.send(result.encode())
        connectionSocket.close()

if __name__ == "__main__":
    solve()