import os,sys
from time import sleep
from AMY import loading
from MENU.menu_ku import Menu

###----WARNA COLOR----###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m' # WARNA MATI

def AsepGanteng(yusup):
   for e in yusup + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      sleep(0.05)

if __name__ == "__main__":
   try:os.mkdir("RESULT")
   except:pass
   try:os.mkdir("DUMP")
   except:pass
   try:os.system("git pull")
   except:pass
   os.system('cls' if os.name == 'nt' else 'clear')
   #AsepGanteng(f"{H}GUNAKAN SCRIPT DENGAN BIJAK,SC INI GRATIS OPEN SOURCE,KALU DAPET IJO ATAU NGGA DAPET HASIL,TETEPLAH PAMER ANG ANG ANG,BIAR GW SEMANGAT UPDATE SC NYA {N}...")
   sleep(3)
   menu = Menu()
   menu.tampil_menu()