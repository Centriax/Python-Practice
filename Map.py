#!/usr/bin/env python3

import webbrowser
import sys
import pyperclip

sys.argv

if len(sys.argv) > 1:
  address = ' '.join(sys.argv[1:])
else:
  address = pyperclip.paste()
  
webbrowser.open('www.google.com/maps/place/' + address)
           

