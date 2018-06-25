import socket
import sys
import threading
from queue import Queue

threadsNum = 2
threadID = [1,2]
queue = Queue()
connectionList = []
addressList = []



#By creating a socket you can connect to 2 computers

def createSocket():
    try:
        global host
        global port
        global sc
        host = ''
        port = 11111
        sc = socket.socket()
    except socket.error as errMsg:
        print("Something went wrong while creating a socket : " + str(errMsg))


# Socket must be bind to a port and wait for the client to connect
def bindSocket():
    try:
        global host
        global port
        global sc
        print('The socket will be bind at port : '+str(port))
        sc.bind((host,port))
        sc.listen(5)    #5 bad attempts allowed
    except socket.error as errMsg:
        print("Something went wrong while binding socket : " + str(errMsg) +"\n\n\t" + "Trying again... Wait" )
        bindSocket()

#Establish a connection with the client(Socket must be listening)
def acceptSocket():
    conn, address = sc.accept()
    print("Connected ... \n IP : \t" +address[0] + "Port : \t" + str(address[1]))
    sendCommands(conn)
    conn.close()

def sendCommands(conn):
    while True:
        cmd_Input = input()
        if cmd_Input.lower() == 'quit' or cmd_Input.lower() == 'exit':
            conn.close()
            sc.close()
            sys.exit()
        if len(str.encode(cmd_Input)) > 0:
            conn.send(str.encode(cmd_Input))
            clientResponse = str(conn.resc(1024), "utf-8")
            print(clientResponse, end="|")


#multiple Connection List
def AcceptConnections():
    for conn in connectionList:
        conn.close()
    del connectionList[:]
    del addressList[:]

    while True:
        try:
            conn, address = sc.accept()
            conn.setblocking(True)
            connectionList.append(conn)
            addressList.append(address)
            print('connection Establish : '+address[0])
        except:
            print("Error Encountered while accepting connections")





def main():
    createSocket()
    bindSocket()
    acceptSocket()


if __name__ == "__main__":
    print('Lets Begin... ')
    main()