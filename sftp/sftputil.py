#!/usr/bin/python
# coding=utf-8

import paramiko, datetime, os

hostname = '10.10.1.254'
port = 22
username = 'war'
password = 'wAr@2017'

local_dir = '/Users/haining/Desktop/sftp/'
remote_dir = '/war/tianhaining/'
t = paramiko.Transport((hostname, port))
t.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(t)
files = os.listdir(local_dir)
for f in files:
    sftp.put(os.path.join(local_dir, f), os.path.join(remote_dir, f))
t.close()
