
from classe_whats import WhatsappBot
import getpass

usuario = getpass.getuser()

if __name__ == "__main__":

    print('\n-- ROBÔ BAIXADOR DE ARQVIOS DO WHATSAPP --')
    print('O objetivo deste bot é, de formar automática, baixar arquivos .pdf de um contato ou grupo do WhatsApp.')
    print('(Para encerrar, pressione ESC)\n')

    print("Hey {},".format(usuario))

    bot = WhatsappBot()
    bot.BaixarArquivos()