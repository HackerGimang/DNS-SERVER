import os, sys, time

a = '\033[31;1m'
b = '\033[32;1m'
c = '\033[33;1m'
d = '\033[34;1m'
e = '\033[35;1m'
f = '\033[36;1m'
g = '\033[37;1m'

def banner():
    print(f'''{d}
 ██████╗ ███╗   ██╗███████╗  ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗                                                                 ██╔══██╗████╗  ██║██╔════╝  ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
 ██║  ██║██╔██╗ ██║███████╗  ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
 ██║  ██║██║╚██╗██║╚════██║  ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
 ██████╔╝██║ ╚████║███████║  ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═══╝╚══════╝  ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝
''')

def pilih():
    os.system('clear')
    banner()
    print(f'{d}                                 {d}╭──────────╮                     ')
    print(f'{d}                                ╭┤{a} DNS LIST {d}├╮                 ')
    print(f'{d}                                │{d}╰──────────╯{d}│                 ')                                                           print(f'{d}╭───┬───────────────────────────┴────────────┴───────────────────────────────╮')
    print(f'{d}├{g}[{f}+{g}]{d}│{f}AUTHOR : Hacker Gaming                                                  {d}│')
    print(f'{d}├───┼────────────────────────────────────────────────────────────────────────┤')                                                  print(f'{d}├{g}[{e}1{g}]{d}│{e}CloudFlare                                                              {d}│')
    print(f'{d}├───┼────────────────────────────────────────────────────────────────────────┤')
    print(f'{d}├{g}[{e}2{g}]{d}│{e}Google                                                                  {d}│')
    print(f'{d}├───┼────────────────────────────────────────────────────────────────────────┤')
    print(f'{d}├{g}[{e}3{g}]{d}│{e}Keluar                                                                  {d}│')
    print(f'{d}├───┴────────────────────────────────────────────────────────────────────────╯')
    plh = input(f'{d}╰{g}[{c}+{g}] {c}Pilihanmu : {b}')
    if plh == '2':
        os.system('clear')
        print(f'''{b}
 ██████╗  ██████╗  ██████╗  ██████╗ ██╗     ███████╗
██╔════╝ ██╔═══██╗██╔═══██╗██╔════╝ ██║     ██╔════╝
██║  ███╗██║   ██║██║   ██║██║  ███╗██║     █████╗
██║   ██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝
╚██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗
 ╚═════╝  ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
''')
        os.system('ping -s9000 8.8.4.4')
        print(f'{g}')
    if plh == '1':
        os.system('clear')
        print(f'''{b}
 ██████╗███████╗
██╔════╝██╔════╝
██║     █████╗
██║     ██╔══╝
╚██████╗██║
 ╚═════╝╚═╝
''')
        os.system('ping -s9000 1.1.1.1')
        print(f'{g}')
    if plh == '3':
        os.system('clear')
        print(f'''{b}
██╗  ██╗███████╗██╗     ██╗   ██╗ █████╗ ██████╗
██║ ██╔╝██╔════╝██║     ██║   ██║██╔══██╗██╔══██╗
█████╔╝ █████╗  ██║     ██║   ██║███████║██████╔╝
██╔═██╗ ██╔══╝  ██║     ██║   ██║██╔══██║██╔══██╗
██║  ██╗███████╗███████╗╚██████╔╝██║  ██║██║  ██║
╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
''')
        print(f'{g}')


if __name__ == '__main__':
        pilih()
