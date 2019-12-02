import socket
import traceback
import re
import threading

import pynmea2

message = ""

class ShareGPS():

    def __init__(self):

        self.host = '0.0.0.0'
        self.port = 5555

        #Flag de parada para o server
        self.flag = True

        #Configura o server para conexão UDP
        print("Servidor configurado para UDP/IP")
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        self.regex_sentence = r"([1-9]{2})([0-9.]+)"
         

    
    def _listen(self):

        global message
        print("Iniciando Server UDP/IP no IP {}:{}".format(self.host, self.port))
        self.server.bind((self.host, self.port))

        #Mantem o servidor ativo até mudar a Flag de parada
        while self.flag:

            self.message, self.addr = self.server.recvfrom(8192)
            self.message = self.message.decode('utf-8').split('\n')

            #faz o parse da mensagem para o protocolo nmea
            self.parse = pynmea2.parse(self.message[0])
            print(self._regex(self.parse.lat), self._regex(self.parse.lon))
            
            

    def run(self):

        threading.Thread(target=self._listen())


    def _regex(self, string):

        self.phrase = str(string)
        self.matches = re.finditer(self.regex_sentence, self.phrase, re.MULTILINE)

        for match in self.matches:

            self.degrees = match.group(1)
            self.minutes = match.group(2)

            self.minutes = float(self.minutes)/60
            
            self.coord = int(self.degrees) + self.minutes

            return round(self.coord*(-1), 7)

        

if __name__ == "__main__":

        gps = ShareGPS()
        gps.run()