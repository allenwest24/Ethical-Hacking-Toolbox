# Clipboard-Logger

### Overview
Checks what is on the target machine's clipboard every 5 seconds and if it's new, it adds it to a log. This log is emailed to the specifed address every 5 minutes.

### Discussion
Most cyber security professionals are familiar with keyloggers. The basic concept is logging every keystroke on the machine it is running on within a certain amount of 
time and then exporting somehow (mine emails me). The other day I was thinking over if anything else could be extrapalated the same way. Keyloggers only work for 
grabbing credentials if you type in the password by hand. Since everyone uses password managers these days (or at least should be) it would stand to reason that if you 
could get to someone's clipboard within the time it takes for that clipboard to get wiped by the password manager, you could get their password. By checking the 
clipboard for a new entry every five seconds and treating everything else about it like a normal keylogger, this "tool" will grab those passwords. It will also grab any 
other text you happen to add to your clipboard while this program is running. This was shockingly easy to make, and combined with a keylogger, covers the majority of 
situations where someone would be entering credentials. You could also just use a sniffer...

### Usage
Just clone, switch the exfil email and password to where you'd like it to be sent, and presto, you're surveiling yourself.
Alternately, you can change the checking time (5 secs) and email frequency (every 5 mins) to whatever you'd like. 
Additionally, you can comment out the emailing function call and just have it print to the console. 

Enjoy.
