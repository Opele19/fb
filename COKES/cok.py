import os,re,requests
from time import sleep
from rich.console import Console
from rich.panel import Panel

from AMY import logo

class COOU:

    def login_cok(self):
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            logo.LOGE().logo_ku()
            Console(width=50, style="bold green").print(Panel("[italic white]Masukan Cookies Facebook,Saran jangan Menggunkan Cookies Pribadi[italic white]",subtitle="╭───",subtitle_align="left"))
            cok = Console().input("[bold green]   ╰─> ")
            open('.cok.txt','w').write(cok)
            with requests.Session() as r:
                try:
                    r.headers.update({'Accept-Language': 'id,en;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Referer': 'https://www.instagram.com/','Host': 'www.facebook.com','Sec-Fetch-Mode': 'cors','Accept': '*/*','Connection': 'keep-alive','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Dest': 'empty','Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate',})
                    response = r.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/_vogee/', cookies={'cookie':cok})
                    if  '"access_token":' in str(response.headers):
                        token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1);open('.tok.txt','w').write(token)
                        self.login_sukses(cok,token)
                    else:Console(width=50, style="bold green").print(Panel("[italic red]Cookies Invalid...[italic white]"));exit()
                except Exception as e:print(e);exit()
            sleep(2);exit()
        except Exception as e:os.system('rm -rf .cok.txt');os.system('rm -rf .tok.txt');print(e);exit()

    def login_sukses(self,cok,token):
        open('.cok.txt','w').write(cok)
        open('.tok.txt','w').write(token)
        Console(width=50, style="bold green").print(Panel("[italic white]Login Berhasil[italic white]"))
        sleep(2);exit()