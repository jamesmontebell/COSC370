from socket import *
# import socket module
import sys  # In order to terminate the program

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections
while True:
    print('Ready to serve ...')
    connectionSocket, addr = serverSocket.accept()

    try:
        """
        Fill in code to receive a request message from the client.
        """
        message = connectionSocket.recv(1024).decode()
        # Extract the path (which is the second part of HTTP header)
        # of the requested object from the message.
        # assuming message holds the data from the previous line(s) of code
        filename = message.split()[1]
        print(filename)
        # Because the extracted path of the HTTP request includes
        # a character ‘\’, we read the path from the second character
        f = open(filename[1:])
        # Store the entire content of the requested file in a temporary buffer
        outputdata = f.read()
        """
        Fill in code to send the the HTTP response header line
        ("HTTP /1.1 200 OK\r\n\r\n") to the connection socket.
        """
        response = "HTTP /1.1 200 OK\r\n\r\n"
        connectionSocket.send(response.encode())
        # Send the content of the requested file to the client
        # Assuming connectionSocket has been created above
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i]. encode())
        connectionSocket.send("\r\n". encode())
        connectionSocket.close()
    except IOError:

        error = "HTTP /1.1 404 Not Found\r\n\r\n"
        connectionSocket.send(error.encode())

        e = open("/error.html")
        outputError = e.read()
        for i in range(0, len(outputError)):
            connectionSocket.send(outputError[i]. encode())
        connectionSocket.send("\r\n". encode())
        connectionSocket.close()

    connectionSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data
