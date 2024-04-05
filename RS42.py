import socket
import os
import threading

def handle_client_connection(client_socket, save_dir):
    try:
        photo_path = client_socket.recv(1024).decode('utf-8')
        if not photo_path:
            return
        
        # Receive and save the photo data
        save_path = os.path.join(save_dir, os.path.basename(photo_path))
        with open(save_path, 'wb') as file:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)

        print(f"Photo '{photo_path}' received and saved successfully.")
    except Exception as e:
        print(f"Error handling client connection: {e}")
    finally:
        client_socket.close()

def start_server(save_dir, host='127.0.0.1', port=9000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)  # Maximum number of queued connections

        print(f"Server listening on port {port}...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            # Create a new thread to handle the client connection
            client_thread = threading.Thread(target=handle_client_connection, args=(client_socket, save_dir))
            client_thread.start()

if __name__ == "__main__":
    save_directory = 'received_photos'
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    start_server(save_directory)