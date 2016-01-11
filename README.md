SMS Search
======
**SMS Search** is a quick script which displays messages backed up by the Android app [SMS Backup & Restore](https://play.google.com/store/apps/details?id=com.riteshsahu.SMSBackupRestore&hl=en) for a particular contact.

Mesages sent by you will be printed in blue, and messages from your specified contact will be printed in green.

---

####Usage:

```
$ ./search.py my_backup.xml
Enter name to search: Chris
[Messages to/from 'Chris'...]
$ 
```

####TODO:
* Improve interface with curses?
* Allow further searching within messages