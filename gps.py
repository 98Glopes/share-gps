import socket
import re
from datetime import datetime as dt

import pynmea2

class ShareGPS():

    def __init__(self):

        self.host = '0.0.0.0'
        self.port = 5000

        #Flag de parada para o server
        self.flag = True

        #Configura o server para conexão UDP
        print("Servidor configurado para UDP/IP")
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        self.regex_sentence = r"([1-9]{2})([0-9.]+)"
         

    
    def listen(self):


        print("Iniciando Server UDP/IP no IP {}:{}".format(self.host, self.port))
        self.server.bind((self.host, self.port))

        print("Timestamp; latitude; longitude")
        #Mantem o servidor ativo até mudar a Flag de parada
        while self.flag:

            self.message, self.addr = self.server.recvfrom(8192)
            self.message = self.message.decode('utf-8').split('\n')
            self.timestamp = dt.now().strftime("%d/%m/%Y, %H:%M:%S")
            #faz o parse da mensagem para o protocolo nmea

            self.parse = pynmea2.parse(self.message[0])

            try:
                
                self.latitude = round(self.parse.latitude, 6)
                self.longitude = round(self.parse.longitude, 6)
                print("{}; {}; {}".format(self.timestamp, self.latitude, 
                                          self.longitude))

            except:
                pass
        

        

if __name__ == "__main__":

        gps = ShareGPS()
        gps.listen()
