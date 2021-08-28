# SMTPY
This is a script coded in python, for sending a email using SMTP to multiple recipients.
to run the script use this commande: 

while read -r EMAIL; do python script.py "$EMAIL"; done < maillist.txt

Notice: dont rename the file name (script.py) and add your mailist in same folder of the script with the name maillist.txt
