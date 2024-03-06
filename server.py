import socket
from datetime import datetime

def format_message(message, addr):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"[{timestamp}] Message from {addr}: {message}"

def start_server(host='127.0.0.1', port=65432):
    
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    with sock:
        sock.bind((host, port))  # Bind to the specified host and port
        sock.listen()  # Listen for incoming connections
        print(f"Server started, listening on {host}:{port}")
        
        while True:  # Keep running to accept multiple connections
            conn, addr = sock.accept()  # Accept a new connection
            with conn:
                print(f"Connection established with {addr}")
                while True:
                    data = conn.recv(1024)  # Receive data from the client
                    
                    if not data:
                        break  # If no data, exit the loop
                    
                    message = data.decode('utf-8')
                    formatted_message = format_message(message, addr)
                    print(formatted_message)  # Print the formatted message
                    
                    if message.lower() == "shutdown":
                        print("Shutdown command received. Shutting down server.")
                        break  # Break out of the loop to shut down the server
                    conn.sendall(data)  # Echo back the received data

if __name__ == "__main__":
    start_server()
