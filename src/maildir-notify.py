#!/usr/bin/python
# -*- coding: utf-8 -*-

# ubuntu-maildir-notify - notification about new emails in local maildir using Ubuntu notification applet

import os
import re
import time
import ConfigParser
from email.parser import Parser
from email.header import decode_header
import indicate
import gobject
import gtk

active_msg = []

def loadFolders(folders):
	# parse specified maildir folders and sort them
	res = []
	p = re.compile("dir_(?P<num>[\d]+)")
	for i, j in folders:
		m = p.match(i)
		if(m):
			res.append((m.group('num'), os.path.expanduser(j) + '/new'))
	res.sort(reverse = True, key = lambda x: x[0])
	return res

def scanNew(folders):
	# delete current items
	global active_msg
	for i in active_msg:
		i.hide()
	active_msg = []
	# find new messages in folders
	for i, j in folders:
		if(not os.path.isdir(j)):
			print "Folder num", i, "is not a valid maildir folder."
			continue
		dirname = j.split('/')[-2].split('.')[-1]
		dir = os.listdir(j)
		for k in dir:
			f = open(j + '/' + k, 'r')
			msg = f.read()
			f.close()
			headers = Parser().parsestr(msg)
			sender = decode_header(headers['from'])[0]
			if(sender[1]):
				sender = unicode(sender[0], sender[1])
			else:
				sender = sender[0]
			subject = decode_header(headers['subject'])[0]
			if(subject[1]):
				subject = unicode(subject[0], subject[1])
			else:
				subject = subject[0]
			label = '[' + dirname + '] ' + subject + ' (' + sender + ')'
			indicator = indicate.Indicator()
			indicator.set_property('draw-attention', 'true')
			indicator.set_property('subtype', 'mail')
			indicator.set_property('name', label)
			indicator.show()
			active_msg.append(indicator)
	return True
			
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
	try:
		check_interval = int(cfg.get('global', 'check_interval'))
	except ConfigParser.NoSectionError, ConfigParser.NoOptionError:
		check_interval = 15
	# notification server
	server = indicate.indicate_server_ref_default()
	server.set_type('message.mail')
	server.set_desktop_file('/usr/share/applications/ubuntu-maildir-notify.desktop')
	server.show()
	# run periodic check
	gobject.timeout_add_seconds(60*check_interval, scanNew, folders)
	gtk.main()

main()
