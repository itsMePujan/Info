
import requests
import os
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
url = "https://checkiph.one/meid/"
def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
get_imei = 0;
intro="""
************************https://github.com/itsMePujan*********************************

██╗██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗    ██╗███╗   ██╗███████╗ ██████╗
██║██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝    ██║████╗  ██║██╔════╝██╔═══██╗
██║██████╔╝███████║██║   ██║██╔██╗ ██║█████╗      ██║██╔██╗ ██║█████╗  ██║   ██║
██║██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝      ██║██║╚██╗██║██╔══╝  ██║   ██║
██║██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗    ██║██║ ╚████║██║     ╚██████╔╝
╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝

*******************https://www.facebook.com/icloudunlocknepal************************

*************************Easy-Info BY PUJAN******************************************
"""
screen_clear()
while get_imei != "exit":
    print(intro)
    get_imei = input("Enter Imei or  exit : ")
    data_to_site = {
    "imei" : get_imei,
    }
    if len(get_imei) == 15:
        with requests.Session() as s:
            r=s.get(url , headers = headers)
            soup = BeautifulSoup(r.content, 'html5lib')
            r=s.post(url, data=data_to_site , headers = headers)
            final_content = BeautifulSoup(r.content, 'html.parser')
            aa=(final_content.find("div", class_="form-label-group").get_text()).strip()
            x = aa.split(":")
            xx = x[1]
            imei = xx[:-5].strip()
            yy = x[2]
            model = yy[:-4].strip()
            zz = x[3]
            meid = zz.strip()
            if meid == "KHÔNG CÓ MEID" :
                    meid = "Network Not Supported After Bypass"
            else:
                    meid = "Network Support After Bypass"
            result = """
            *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            -
            *   Imei    : """+imei+"""
            -   Model   : """+model+"""
            *   Network : """ + meid +"""
            -
            *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """
            print(result)
            blc = input("Enter Any key to Continue... ")
            screen_clear()
    else:
        screen_clear()

else :
    screen_clear()
    tx = """

   ▄▄▄▄▀ ▄  █ ██      ▄   █  █▀    ▀▄    ▄ ████▄   ▄
▀▀▀ █   █   █ █ █      █  █▄█        █  █  █   █    █
    █   ██▀▀█ █▄▄█ ██   █ █▀▄         ▀█   █   █ █   █
   █    █   █ █  █ █ █  █ █  █        █    ▀████ █   █
  ▀        █     █ █  █ █   █       ▄▀           █▄ ▄█
          ▀     █  █   ██  ▀                      ▀▀▀
               ▀
 """
    print(tx)
