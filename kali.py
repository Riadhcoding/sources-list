import os

def clear():
    os.system('clear')

clear()
print ('\033[1;31m{1}\033[1;32m solved  sources list')
print ('\003[1;31m{2}\033[1;32m Find Me in instagram')
ask = int(input ('\033[1;31m{?}\033[1;36m Choose : '))

if ask == 1:
    os.chdir('/etc/apt')
    os.system('sudo rm -rf sources.list')
    os.system('sudo cp /$HOME/kali/main/sources.list /etc/apt')
    print ('\033[1;32msources list updated\n')
    print ('\033[1;32mNow Run This Command\n\033[1;31m$\033[1;36m sudo apt update && sudo apt -y full-upgrade -y && sudo reboot')
else:
    print ('\033[1;31mPelase Choose 1 ')
