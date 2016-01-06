import logging
import os

tokenpath = os.path.dirname(os.path.realpath(__file__)) + "/token"

logging.basicConfig( level=logging.INFO)

import requests


class Bot:
    def __init__(self):
        try:
            tokenFile = open(tokenpath,'r')
            self.token = tokenFile.read().strip()
            tokenFile.close()
        except IOError: 
            logging.error("Non ho trovato il file di token. E' necessario creare un file 'token' con la token telegram per il bot. In ogni caso questo file NON deve essere tracciato da git - viene ignorato perche' menzionato nel .gitignore.")
            exit()


        logging.info("caricata token.")

        self.chat_id = -94452612 # magic number: chat_id del gruppo termostato antonelli
        
        self.queue = []


    def request(self,command,params = {}):
        url = "https://api.telegram.org/bot" + self.token + "/" + command
        req = requests.get(url,params = params)
        json = req.json()

        try:
            logging.info("status of request: " + str(json[u'ok']))
        except KeyError:
            logging.warning("no u'ok' entry in return json... ???")

        return json

    def sendMessage(self,s):
        params = {
                'chat_id':self.chat_id,
                'text':s
                }
        ret = self.request("SendMessage",params)
    


# GUIDA
#
# questo e' un modulo che gestisce esclusivamente il bot di telegram.
# Non bisogna svolgere nessun tipo di calcolo o parsing relativo al termostato qui.
# Questo modulo e' solo per inviare/ricevere messaggi

# per usarlo bisogna caricarlo, e poi creare un istanza della classe bot:

# import thermogram
# bot = thermogram.Bot()

# attenzione a maiuscole e minuscole. Per mandare un messaggio, basta

# bot.sendMessage("testo del messaggio")
