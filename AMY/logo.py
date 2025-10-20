import os
from rich.console import Console
from rich.panel import Panel

class LOGE:

    def logo_ku(self):
        os.system("cls" if os.name == "nt" else "clear")
        Console(width=50, style="bold green").print(Panel("""[bold red]●[bold yellow] ●[bold green] ●[italic white]
                                                          
      \r██    ██  ██████   ██████  ███████ 
      \r██    ██ ██    ██ ██       ██      
      \r██    ██ ██    ██ ██   ███ █████   
      \r ██  ██  ██    ██ ██    ██ ██      
      \r  ████    ██████   ██████  ███████ 
                                                          
      \rAuthor : [bold green]Asep Yusup[/]  Version : [bold green]6.0[/]"""))