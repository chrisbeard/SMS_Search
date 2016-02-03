#! /usr/bin/env python3

import xml.etree.ElementTree as ET
import sys

if len(sys.argv) == 1:
    print("Usage: ./search.py <XML_FILE> [option(s)]")
    print()
    print("Options:")
    print("   --keyword    search messages by keyword")
    print("   --exact      perform exact match")
    sys.exit(1)

# Parse options
exact_match = "--exact" in sys.argv
keyword = None
if "--keyword" in sys.argv:
    keyword = input("Enter keyword to search: ")
else:
    name = input("Enter name to search: ")

# Prepare xml file for parsing
f = sys.argv[1]
tree = ET.parse(f)
root = tree.getroot()

# Pretty-printing
HEADER = '\033[95m'
GREEN = '\033[92m'
BLUE  = '\033[94m'
END  = '\x1b[0m'


def print_message(child):
    message = HEADER + "{}\n  " + END + "{}: {}{}"
    contact = child.get('contact_name')
    date = child.get('readable_date')
    msg = child.get('body')

    if child.get('type') == '1':
        print(message.format(date, contact, GREEN, msg))
    else:
        print(message.format(date, "Me", BLUE, msg))

# Print all matching messages
for child in root:
    contact = child.get('contact_name')
    message = child.get('body')

    if keyword:
        if exact_match:
            if keyword in message.split():
                print_message(child)
        elif keyword in message:
                print_message(child)
    else:
        if exact_match:
            if name in contact.split():
                print_message(child)
        elif name in contact:
                print_message(child)
