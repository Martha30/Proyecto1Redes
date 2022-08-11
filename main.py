
import slixmpp
import asyncio
import logging
from getpass import getpass
from argparse import ArgumentParser
from slixmpp.exceptions import IqError, IqTimeout
from slixmpp import ClientXMPP

# Ideally use optparse or argparse to get JID,
# password, and log level.
logging.basicConfig(level=logging.DEBUG, format='%(levelname)-8s %(message)s')

class Client(slixmpp.ClientXMPP):
#You start describing and define all the things you need
    def __init__(self,Uid,passWord):
        slixmpp.ClientXMPP.__init__(self,Uid,passWord)
        self.Uid = Uid
        self.passWord = passWord
        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.message)
        self.add_event_handler("register", self.registro)

        # Here's how to access plugins once you've registered them:
        # self['xep_0030'].add_feature('echo_demo')

    async def session_start(self, event):
        self.send_presence()
        await self.get_roster()

        # Most get_*/set_* methods from plugins use Iq stanzas, which
        # are sent asynchronously. You can almost always provide a
        # callback that will be executed when the reply is received.

        def contact():
            contacto = self.client_roster.amigos()
            for c in contacto:
                for lista in contacto[c]:
                    usuario = self.client_roster[lista]['nombre']
                    if self.client_roster[lista]['nombre']:
                        print(usuario, lista)
                    else:
                        print(lista) 




    def message(self, msg):
        if msg['type'] in ('chat', 'normal'):
            msg.reply("Thanks for sending\n%(body)s" % msg).send()



    # Ideally use optparse or argparse to get JID,
    # password, and log level.


    xmpp = EchoBot('somejid@example.com', 'use_getpass')
    xmpp.connect()
    xmpp.process()