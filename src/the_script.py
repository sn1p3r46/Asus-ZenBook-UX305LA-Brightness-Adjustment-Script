#!/usr/bin/env python3

# This code comes without warranty and without license!
# Use it at your own risk
#
# USAGE: 	python3 /path/to/script.py '<name>' '<command>' '<key_combination>'
# EXAMPLE: 	python3 /path/to/script.py 'open gedit' 'gedit' '<Alt>7'
#



import subprocess
import sys

USAGE = "        python3 /path/to/script.py '<name>' '<command>' '<key_combination>'"
EXAMPLE = "        python3 /path/to/script.py 'open gedit' 'gedit' '<Alt>7'"


if(len(sys.argv)!=4):
    print("Error.. USAGE: \n" + USAGE + "\n" + EXAMPLE +"\n" )
    sys.exit()

# defining keys & strings to be used
key = "org.gnome.settings-daemon.plugins.media-keys custom-keybindings"
subkey1 = key.replace(" ", ".")[:-1]+":"
item_s = "/"+key.replace(" ", "/").replace(".", "/")+"/"
firstname = "custom"

# get the current list of custom shortcuts
get = lambda cmd: subprocess.check_output(["/bin/bash", "-c", cmd]).decode("utf-8")
current = eval(get("gsettings get "+key))

# make sure the additional keybinding mention is no duplicate
n = 1
while True:
    new = item_s+firstname+str(n)+"/"
    if new in current:
        n = n+1
    else:
        break
# add the new keybinding to the list
current.append(new)

# create the shortcut, set the name, command and shortcut key
cmd0 = 'gsettings set '+key+' "'+str(current)+'"'
cmd1 = 'gsettings set '+subkey1+new+" name '"+sys.argv[1]+"'"
cmd2 = 'gsettings set '+subkey1+new+" command '"+sys.argv[2]+"'"
cmd3 = 'gsettings set '+subkey1+new+" binding '"+sys.argv[3]+"'"

for cmd in [cmd0, cmd1, cmd2, cmd3]:
    subprocess.call(["/bin/bash", "-c", cmd])


# ORIGINAL CODE http://askubuntu.com/questions/597395/how-to-set-custom-keyboard-shortcuts-from-terminal
# THANKS 2 JacobVlijm
