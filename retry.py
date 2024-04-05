import os
import socket
import time

def send_photos_from_folder(folder_path, server_host='127.0.0.1', server_port=9000):
    try:
        # Iterate through the specified folder and send each image to the server
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                photo_path = os.path.join(folder_path, filename)
                send_photo(photo_path, server_host, server_port)
                time.sleep(0.5)  # Add a small delay between sending photos

        print("All photos from the folder sent to the server.")
    except Exception as e:
        print("Error:", e)

def send_photo(photo_path, server_host='127.0.0.1', server_port=9000, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            # Establish a connection with the server and send the photo
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((server_host, server_port))
                client_socket.sendall(photo_path.encode('utf-8'))

                with open(photo_path, 'rb') as file:
                    while True:
                        data = file.read(1024)
                        if not data:
                            break
                        client_socket.sendall(data)

            print(f"Photo '{photo_path}' sent successfully.")
            return  # Exit the function on successful transfer
        except Exception as e:
            retries += 1
            print(f"Error sending photo '{photo_path}':", e)
            print(f"Retrying ({retries}/{max_retries})...")
            time.sleep(1)  # Wait before retrying

    print(f"Failed to send photo '{photo_path}' after {max_retries} retries.")

if __name__ == "__main__":
    dcim_folder_path = '/sdcard/DCIM/Camera'  # Replace with the actual path to the DCIM folder
    remote_server_host = '127.0.0.1'  # Replace with the IP or hostname of the remote server
    remote_server_port = 9000  # Replace with the port number the server is listening on

    send_photos_from_folder(dcim_folder_path, remote_server_host, remote_server_port)