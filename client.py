import socket

def client(server_ip='127.0.0.1', server_port=65432):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    with server:
        try:
            server.connect((server_ip, server_port))  
            print(f"Connected to {server_ip}:{server_port}. \nCommand \nType 'exit' to quit. Type 'shutdown' to shoudown server ")
        except ConnectionRefusedError:
            print("Connection failed. Is the server running?")
            return

        while True:
            message = input("Write something: ")
            if message.lower() == 'exit':  #exit the loop
                print("Exiting client.")
                break

            server.sendall(message.encode('utf-8'))  # Send the message to the server
            
            if message.lower() == 'shutdown':
                print("Sending shutdown command to server...")
                break  # Exit the client after sending the shutdown command
            
            data = server.recv(1024)  # Receive the response from the server
            print(f"Received: {data.decode('utf-8')}")



if __name__ == "__main__":
    client()
