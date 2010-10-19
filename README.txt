				Maildir-notify version 0.1

Introduction:
-------------
Maildir-notify is a small python program for watching selected maildir folders.
If it found new messages it will notify in Ubuntu notification applet. This
is usefull if you want to use notification applet but your mail client can
only read local maildir (for example mutt).

Installation:
-------------
Copy src/maildir-notify.py to the /usr/bin, src/maildir-notify.desktop to the
/usr/share/applications and res/maildir-notify.xpm to the /usr/share/pixmaps.

Configuration:
--------------
Configuration is written in ~/.maildir-notify file. Example config file you
can find in res/maildir-notify.conf. In global section specify check_interval -
interval how often maildir-notify will read maildir and scans new messages.
In maildir_folders section then specify each folder that you want monitor.
Each specified folder should have new, cur and tmp subfolders. Keys are written
as dir_X where X is order number for displaying messages in applet.

Dependencies:
-------------
- python (>= 2.6.0)
- python-indicate (>= 0.4.0)
- python-gtk (>= 2.21)
- python-gobject (>= 2.21)

Thanks:
-------
to Naf71 for Web0 icon theme 
(http://gnome-look.org/content/show.php/Web0?content=133506) - mail icon comes
from this set.

Contact:
--------				
Homesite: http://www.spamik.cz
E-mail: spm@spamik.cz
Primary git repository: http://git.spamik.cz/ubuntu-maildir-notify.git
Github page: http://github.com/spamik/maildir-notify

GPG Public key:
http://www.spamik.cz/sites/default/files/spm.asc
or search "spm@spamik.cz" on ubuntu key server.
Finger print: DC47 0DA1 D270 EEE4 1BB2 A297 AD9E C8F4 9E0B 61C2

