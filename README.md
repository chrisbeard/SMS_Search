#SMS Search


##Description
**SMS Search** is a quick script which displays messages backed up by the Android app [SMS Backup & Restore](https://play.google.com/store/apps/details?id=com.riteshsahu.SMSBackupRestore&hl=en) for a particular contact.

Mesages sent by you will be printed in blue, and messages from your specified contact will be printed in green.


##Usage

####General format
```
$ ./search.py <XML_FILE_PATH> [option(s)]
```

####Search by contact
```
$ ./search.py my_backup.xml
Enter name to search: Chris
[Messages to/from 'Chris'...]
$ 
```

####Search by keyword in message body
```
$ ./search.py my_backup.xml --keyword
Enter keyword to search: hello
[Messages containing 'hello'...]
$ 
```

#####Note: Default matching is done by checking if the provided name/keyword is found as a **substring**. Exact matching can be performed using the flag **--exact**.


##TODO:
* Improve interface with curses?