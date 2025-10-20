from time import sleep
from rich.console import Console
from rich.panel import Panel


class RESULIT:

    def cek_result(self):
        Console(width=50, style="bold green").print(Panel("[italic white]1. Hasil [bold green]OK[italic white]\n2. Hasil [bold red]CP[italic white]",subtitle="╭───",subtitle_align="left"))
        x = Console().input("[bold green]   ╰─> ")
        try:
            if x == "1":
                with open("RESULT/OK.txt", "r") as file:
                    Console(width=50, style="bold green").print(Panel(f"[bold green]{file.read()}[italic white]"))
            elif x == "2":
                with open("RESULT/CP.txt", "r") as file:
                    Console(width=50, style="bold green").print(Panel(f"[bold red]{file.read()}[italic white]"))
            else:
                print(f"input hanya dengan angka,jangan kosong.")
                sleep(2)
                exit()
        except FileNotFoundError:
            print("File Tidak Ditemukan")
            exit()