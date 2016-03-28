#!/usr/bin/env python3

import urllib.request, os, re, time, urllib.error

while True:
    try:
        html_dump = str(urllib.request.urlopen('https://www.rgpv.ac.in/').read())
        string_match = re.findall('B.E. 5th Semester'.strip(), html_dump)
        if len(string_match) == 0:
            os.system("notify-send 'Enjoy!, No need to worry' 'Result is not declared yet'")
            time.sleep(900)
        else:
            os.system("notify-send 'Shit just got real!' 'Result Declared'")
            quit()
    except urllib.error.URLError:
        os.system ("notify-send 'Network Error!!' 'Unable to connect'")
        quit()
