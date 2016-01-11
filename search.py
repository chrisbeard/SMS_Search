#! /usr/bin/env python3

import xml.etree.ElementTree as ET
import sys

if len(sys.argv) == 1:
    print("Usage: ./search.py XML_FILE")
    sys.exit(1)

HEADER = '\033[95m'
GREEN = '\033[92m'
BLUE  = '\033[94m'
END  = '\x1b[0m'
 
f = sys.argv[1]
tree = ET.parse(f)
root = tree.getroot()

name = input("Enter name to search: ")

for child in root:
    contact = child.get('contact_name')
    if name in contact:
        t = child.get('readable_date')
        m = child.get('body')
        # message = HEADER + "{}\n  " + END + "{}: {}{}\n"
        message = HEADER + "{}\n  " + END + "{}: {}{}"

        if child.get('type') == '1':
            print(message.format(t, contact, GREEN, m))
        else:
            print(message.format(t, "Me", BLUE, m))
