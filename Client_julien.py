'''
    Auteur : CHMARA Julien
    Date : 01/03/2024
    Script client python
'''

import socket

def main():
    # Initialisation du socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Numéro de port déterminé par votre âge
    base_port = 50000
    age = 21  
    port = base_port + age

    # Adresse du serveur
    server_address = ('localhost', port)
# https://upload.wikimedia.org/wikipedia/commons/0/01/Julien_Clerc_2011.jpg  
    try:
        # Connexion au serveur
        client_socket.connect(server_address)

        # Message à envoyer au serveur
        while True:
            # Message à envoyer au serveur
            print("Pour sortir du programme entrer le message \nje sui a laeropor bisouuuu je manvol \n pour voir la date mettre = date")
            date = "date"
            message = input("Votre message : ")
            client_socket.sendall(message.encode())
            # Réception de la réponse du serveur
            data = client_socket.recv(1024)
            print("Réponse du serveur :", data.decode())

            # On verifie si le message reçu est correct 
            if data.decode() == "je sui a laeropor bisouuuu je manvol":
                print("Fin de la connexion.")
                break
            # On verifie si le message reçu est correct 
            elif data.decode() == "date":
                print("La date et l'heure du serveur : ", data[10:])

    finally:
        # Fermeture de la connexion
        client_socket.close()

if __name__ == "__main__":
    main()