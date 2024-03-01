'''
    Auteur : CHMARA Julien
    Date : 01/03/2024
    Script serveur python
'''

import datetime
import socket

def search_port(baseport):
    port = baseport
    while True: #on boucle pour trouver un port disponible
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(('localhost', port))
            s.close()
            return port
        except OSError:
            port += 100

def main():
    #Déterminer le port à utiliser en fonction de l'âge
    base_port = 50000
    age = 21  
    port = search_port(base_port + age)

    # Instancier le socket d'écoute
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)  #Limite le nombre de connexions en attente à 1

#https://upload.wikimedia.org/wikipedia/commons/0/01/Julien_Clerc_2011.jpg  
    try:    
        while True:
            #On essaye de se connecter a l'adresse
            client_socket, client_address = server_socket.accept()
            print(f"Connexion établie avec {client_address}")

           #Attendre de recevoir un message du client
            message = client_socket.recv(1024).decode()
            print(f"Message reçu du client : {message}")
            
            #On verifie le message reçu est date si oui on va chercher la date et l'heure
            if message == "date":
                current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                response = "date du serveur:" + current_datetime
                client_socket.send(response.encode())
            else:
            #Envoyer une réponse au client avec un message supplémentaire
                response = message + "\nJe suis là !"
                client_socket.send(response.encode())

            #Fermer la connexion avec le client
            client_socket.close()
    finally:
            #Fermer le socket du serveur lorsque le travail est terminé
            server_socket.close()        

if __name__ == "__main__":
    main()
  