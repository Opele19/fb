import os
from rich.console import Console
from time import sleep
from rich.panel import Panel


###----- BAGIAN ANIMASI FOlDER -----###
from AMY import loading,logo,res
from METHODE import validate
from COKES.cok import COOU as coky

class Menu:

    def tampil_menu(self):
        try:
            open('.cok.txt','r').read()
            open('.tok.txt','r').read()
        except(IOError,KeyError,FileNotFoundError):
            os.system('cls' if os.name == 'nt' else 'clear')
            loading.Load().cek_coki()
            Console(width=50, style="bold green").print(Panel("[bold red]Cookies Mati...[italic white]"))
            sleep(3)
            coky().login_cok()
        os.system('cls' if os.name == 'nt' else 'clear')
        logo.LOGE().logo_ku()
        Console(width=50, style="bold green").print(Panel("[italic white]1. Crack Akun Facebook    3. Cek Hasil Crack\n2. Crack Dump ID Facebook   0. Keluar[italic white]",subtitle="╭───",subtitle_align="left"))
        x = Console().input("[bold green]   ╰─> ")
        if x in ["1", "01"]:validate.VALIDATE().dump_massal()
        elif x in ["2", "02"]:validate.VALIDATE().crack_file()
        elif x in ["3", "03"]:res.RESULIT().cek_result()
        elif x in ["0", "00"]:os.system("rm -rf .cok.txt");os.system("rm -rf .tok.txt");print('Keluar Berhasil');exit()
        else:print('Pilihan Yang Bener');sleep(2);self.tampil_menu()
