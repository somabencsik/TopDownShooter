import socket
from _thread import *
import pickle
import random as r

from code.Client import Player as p


class Server:
    def __init__(self):
        self.server = "192.168.1.43"
        self.port = 5555
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nextPlayer = 0
        self.players = []

        try:
            self.soc.bind((self.server, self.port))
        except socket.error as e:
            print(e)

        self.soc.listen(4)
        print("Server started\nWaiting for connection...")

    def threadClient(self, conn, player):
        if player < len(self.players):
            self.players[player] = p.Player(r.randint(0, 1230), r.randint(0, 670), 50, 50, (0, 200, 0))
        else:
            self.players.append(p.Player(r.randint(0, 1230), r.randint(0, 670), 50, 50, (0, 200, 0)))

        conn.send(pickle.dumps(self.players[player]))
        while True:
            try:
                data = pickle.loads(conn.recv(2048 * 10))

                self.players[player] = data

                if not data:
                    print("Disconnected")
                    break
                else:
                    reply = self.players

                conn.sendall(pickle.dumps(reply))
            except Exception as e:
                print(e)

        print("Lost connection")
        try:
            self.players[player] = p.Player(0, 0, 0, 0, (0, 0, 0))
            self.players[player].currentWeapon.bullets.clear()
            self.players[player].currentWeapon = None
        except Exception as e:
            print(e)
        conn.close()

    def run(self):
        while True:
            conn, address = self.soc.accept()
            print("Connected to:", address)

            for player in self.players:
                if player.width == 0:
                    self.nextPlayer = self.players.index(player)
                    break

            if self.nextPlayer <= len(self.players):
                start_new_thread(self.threadClient, (conn, self.nextPlayer))
                self.nextPlayer = self.nextPlayer + 1
            else:
                start_new_thread(self.threadClient, (conn, len(self.players)))


s = Server()
s.run()
