from rich.console import Console
from time import sleep

class Load:

    def __init__(self):
        self.ric = Console()
        self.dat = [1, 2]

    def cek_coki(self):
        with self.ric.status("[bold white] mengecek cookie...") as d:
            while self.dat:
                self.dat.pop(0)
                sleep(1)

    def ubah_taa(self):
        with self.ric.status("[bold white] mengubah data...") as d:
            while self.dat:
                self.dat.pop(0)
                sleep(1)

    def cek_modul(self):
        with self.ric.status("[bold white] tunggu sedang install modul...") as d:
            while self.dat:
                self.dat.pop(0)
                sleep(3)