#!/usr/bin/python

import csv
import datetime
import hashlib
import os
from builtins import any as search_array

nogo = ['/dev', '/proc', '/run', '/sys', '/tmp', '/var/lib', '/var/run', '/var/ossec' '/usr', '/bin', '/boot', '/etc']

def hash_the_file(filepath):
    hasher = hashlib.sha256()
#    bytes = bytearray(128*1024)
    with open(filepath, 'rb') as file_p:
        while True:
            info = file_p.read(4096)
            if not info: break
            hasher.update(info)
        return hasher.hexdigest()


def walk():
    with open('hashedinfo.csv') as file:
        L = file.readlines()
    l = list()
    f = open('hashedinfo.csv', 'w')
    for root, dirs, files in os.walk('/'):
        #print(root)
        #path = root.split(os.sep)
        #for path in [os.path.join(root, file_n) for file_n in files]:
        if root in nogo:
            dirs[:] = []
            files[:] = []
            pass
        for file_n in files:
            #print(file_n)
            file_n = os.path.join(root, file_n)
            try:
                fp = os.path.join(root, file_n)
                hashed = hash_the_file(fp)
                filename = os.path.relpath(fp, '/')
                date = str(datetime.datetime.now())
                line_str = str(fp) + ', ' + str(hashed) + ', ' + str(date) + '\n'

                #changed
                if search_array(hashed in i for i in L) == False:
                    l.append(line_str)

                f.write(line_str)

            except:
                continue
    f.close()
    for i in l:
        print(i + "changes\n")

def main():
    walk()

main()
