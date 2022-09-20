import os, sys, time

x = 'ping_stabilizer'
k = 'keluar'
a = '1'
b = '2'
c = '3'
d = '4'

def pilih():
    os.system('clear')
    os.system('toilet -f big -F gay PILIH')
    print('')
    print('\033[37;1m[\033[32;1m1\033[37;1m] \033[32;1mGoogle¹')
    print('\033[37;1m[\033[32;1m2\033[37;1m] \033[32;1mGoogle²')
    print('\033[37;1m[\033[32;1m3\033[37;1m] \033[32;1mCloudFlare')
    print('\033[37;1m[\033[32;1m4\033[37;1m] \033[32;1mKeluar')
    print('')
    pilih = input('\033[37;1m[\033[35;1m+\033[37;1m] \033[35;1mMasukan pilihanmu :\033[36;1m ')
    if pilih == a:
        os.system('clear')
        os.system('toilet -f big -F gay Google¹')
        print('')
        os.system('ping -s9000 8.8.8.8')
    if pilih == b:
        os.system('clear')
        os.system('toilet -f big -F gay Google²')
        print('')
        os.system('ping -s9000 8.8.4.4')
    if pilih == c:
        os.system('clear')
        os.system('toilet -f big -F gay CloudFlare')
        print('')
        os.system('ping -s9000 1.1.1.1')
    if pilih == d:
        os.system('clear')
        os.system('figlet Keluar')
        print('')
        os.system('cd')
        time.sleep(2)

def login():
    os.system('clear')                                                                                                                           print('\033[37;1mToken : https://bit.ly/3RWmdh3')
    print('')
    time.sleep(1)
    token = input('\033[37;1m[\033[33;1m+\033[37;1m] \033[33;1mMasukan token :\033[32;1m ')
    if token == x:
        print('\033[32;1m[!] Token benar')
        time.sleep(2)
        os.system('clear')
        sys.exit
        pilih()
    else:
         print('\033[31;1m[!] Token salah')
         time.sleep(1)
         login()


if __name__ == '__main__':
         login()
