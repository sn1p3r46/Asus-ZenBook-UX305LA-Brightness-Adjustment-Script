# ASUS ZenBook UX305LA Brightness adjustment scripts


**AUTHOR:** Andrea Galloni ([Twitter](https://twitter.com/andreagalloni92))

**E-Mail:** andrea [dot] galloni [at] studenti [dot] unitn [dot] it

---


This couple of scripts helps me to control the brightness of my UltraBook

**DEPENDENCES:**
  + Ubuntu 14.04
  + Python3
  + gsettings


I managed to create some key-bindings in order to do not have to open a console every time.

The core script is the `src/brightness` file, to use it you need root privileges.
In order to make it executable from a shortcut without asking for the root password
you need to edit the `/etc/sudoers` file (details in code comments).

The `src/the_script.py` is a Python3 script that create the shortcut in Ubuntu environment using `gsettings`.

The whole code in this repository comes without any kind of warranty or license, use it at your own risk.

If you have some improvements or suggestions, please create a pull request or write to me at: andreagalloni92{at}gmail[dot]com
