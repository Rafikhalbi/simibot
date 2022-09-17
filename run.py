import os
from colorama import init,Fore,Back,Style
from requests import get
import re 

init()
def echo(text):
    print(text)

class SimiBot:
    def __init__(self) -> None:
        pass
    def message_simi(self):
        echo(
                f'{Fore.GREEN}TYPE: {Fore.YELLOW}stopchat{Fore.GREEN} FOR EXIT{Fore.RESET}\n'
                )
        while True:
            mess = input(
                    f'{Fore.RED}message{Fore.BLUE}:{Fore.RESET} '
                    )
            if mess in['stopchat','Stopchat','STOPCHAT']:exit(
                    f'{Fore.YELLOW}simi{Fore.BLUE}: {Fore.WHITE}Byeee....'
                    )
            get_chat = get(f'https://api.simsimi.net/v2/?text={mess}&lc=id&cf=false')
            result = re.search(r'{"methods":"GET","success":"(.*?)","noti":"MeoCop#5555"',get_chat.text)[1]
            echo(
                    f'{Fore.YELLOW}simi{Fore.BLUE}: {Fore.WHITE}{result}'
                    )
    def costum_appearance(self):
        echo(
                f'''{Fore.CYAN}  _________.__        .__ 
 /   _____/|__| _____ |__|
 \_____  \ |  |/     \|  |
 /        \|  |  Y Y  \  |
/_______  /|__|__|_|  /__|
        \/          \/    
        {Fore.RED}{Style.BRIGHT}{Back.WHITE}-====( BOT CHAT Simi {Style.NORMAL}\n{Fore.RESET}{Back.RESET}'''
                )
        return self.message_simi()

if __name__ == '__main__':
    simi = SimiBot()
    simi.costum_appearance()


