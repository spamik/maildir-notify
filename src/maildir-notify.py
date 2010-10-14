#!/usr/bin/python
# -*- coding: utf-8 -*-

# ubuntu-maildir-notify - notification about new emails in local maildir using Ubuntu notification applet

import os
import re
import ConfigParser

def loadFolders(folders):
    # parse specified maildir folders and sort them
    res = []
    p = re.compile("dir_(?P<num>[\d]+)")
    for i, j in folders:
        m = p.match(i)
        if(m):
            res.append((m.group('num'), os.path.expanduser(j) + '/new'))
    res.sort(key = lambda x: x[0])
    return res

def scanNew(folders):
    # find new messages in folders
    for i, j in folders:
        print "Scanning folder", i
        if(not os.path.isdir(j)):
            print "Folder num", i, "is not a valid maildir folder."
            continue
        dir = os.listdir(j)
        for k in dir:
            print "Found message", k

def main():
    path = os.path.expanduser("~/.maildir-notify.conf")
    if(not os.path.isfile(path)):
        print "Configuration file ~/.maildir-notify.conf does not exists."
        print "Please create your configuration first."
        return
    cfg = ConfigParser.RawConfigParser()
    cfg.read(path)
    if(not cfg.has_section('maildir_folders')):
        print "You haven't specified any maildir folders to watch."
        print "Please edit your config file first."
        return
    folders = loadFolders(cfg.items('maildir_folders'))
    scanNew(folders)

main()

